from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import decimal

app = Flask(__name__)
app.secret_key = "7410"  # needed for flashing messages

# --- MySQL Connection (Per-Request) ---
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="7410",  # your password
        database="Electricity_Bill_Management"
    )

@app.route('/')
def dashboard():
    # Per-request DB connection
    db = get_db()
    try:
        cursor = db.cursor()
        
        # KPI Queries
        cursor.execute("SELECT COUNT(*) FROM Customer")
        total_customers = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Bill WHERE status='UNPAID' AND due_date < CURDATE()")
        overdue_bills = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(amount_paid) FROM Payment")
        total_revenue = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM Meter WHERE status='ACTIVE'")
        active_meters = cursor.fetchone()[0]
        
        # Monthly Revenue Query
        cursor.execute("""
            SELECT MONTHNAME(b.billing_date) AS month_name, SUM(p.amount_paid) AS total_paid
            FROM Bill b LEFT JOIN Payment p ON b.bill_id = p.bill_id
            GROUP BY MONTHNAME(b.billing_date), MONTH(b.billing_date)
            ORDER BY MONTH(b.billing_date)
        """)
        monthly_data = cursor.fetchall()
        
        return render_template('dashboard.html', 
                             total_customers=total_customers,
                             overdue_bills=overdue_bills,
                             total_revenue=total_revenue,
                             active_meters=active_meters,
                             monthly_data=monthly_data)
    finally:
        db.close()

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            customer_id = request.form['customer_id']
            name = request.form['name']
            address = request.form['address']
            contact = request.form['contact']
            email = request.form['email']

            query = "INSERT INTO Customer (customer_id, name, address, contact_number, email, credit_balance) VALUES (%s, %s, %s, %s, %s, 0.0)"
            values = (customer_id, name, address, contact, email)
            cursor.execute(query, values)
            db.commit()

            flash("✅ Customer Created Successfully!")
        except mysql.connector.Error as err:
            flash(f"⚠️ Error: {err}")
        finally:
            db.close()
        return redirect(url_for('add_customer'))

    return render_template('add_customer.html')

@app.route('/add_meter', methods=['GET', 'POST'])
def add_meter():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            meter_id = request.form['meter_id']
            customer_id = request.form['customer_id']
            installation_date = request.form['installation_date']
            status = request.form['status']

            query = "INSERT INTO Meter (meter_id, customer_id, installation_date, status) VALUES (%s, %s, %s, %s)"
            values = (meter_id, customer_id, installation_date, status)
            cursor.execute(query, values)
            db.commit()

            flash("✅ Meter Added Successfully!")
        except mysql.connector.Error as err:
            flash(f"⚠️ Error: {err}")
        finally:
            db.close()
        return redirect(url_for('add_meter'))

    # Fetch customers for dropdown
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT customer_id, name FROM Customer")
        customers = cursor.fetchall()
        return render_template('add_meter.html', customers=customers)
    finally:
        db.close()

@app.route('/add_reading', methods=['GET', 'POST'])
def add_reading():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            meter_id = request.form['meter_id']
            reading_value = request.form['reading_value']
            reading_date = request.form['reading_date']

            # Validate meter_id
            cursor.execute("SELECT meter_id FROM Meter WHERE meter_id = %s", (meter_id,))
            if not cursor.fetchone():
                flash("❌ Invalid Meter ID.")
                return redirect(url_for('add_reading'))

            # Insert reading (reading_id is auto-incremented)
            query = "INSERT INTO Meter_Reading (meter_id, reading_value, reading_date) VALUES (%s, %s, %s)"
            values = (int(meter_id), int(reading_value), reading_date)
            cursor.execute(query, values)
            db.commit()
            flash("✅ Meter Reading Recorded Successfully!")
        except mysql.connector.Error as err:
            if err.errno == 1452:
                flash("❌ Invalid Meter ID — foreign key constraint failed.")
            else:
                flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('add_reading'))

    # Fetch meters for dropdown
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT meter_id FROM Meter")
        meters = cursor.fetchall()
        return render_template('add_reading.html', meters=meters)
    finally:
        db.close()

@app.route('/add_tariff', methods=['GET', 'POST'])
def add_tariff():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            plan_name = request.form['plan_name']
            unit_rate = request.form['unit_rate']
            applicable_from_date = request.form['applicable_from_date']

            # Validate unit_rate
            try:
                unit_rate = float(unit_rate)
                if unit_rate <= 0:
                    flash("❌ Unit rate must be positive.")
                    return redirect(url_for('add_tariff'))
            except ValueError:
                flash("❌ Invalid unit rate format.")
                return redirect(url_for('add_tariff'))

            # Insert tariff
            query = "INSERT INTO Tariff (plan_name, unit_rate, applicable_from_date) VALUES (%s, %s, %s)"
            values = (plan_name, unit_rate, applicable_from_date)
            cursor.execute(query, values)
            db.commit()

            flash("✅ Tariff Plan Added Successfully!")
        except mysql.connector.Error as err:
            flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('add_tariff'))

    return render_template('add_tariff.html')

@app.route('/bill', methods=['GET', 'POST'])
def generate_bill():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            meter_id = request.form['meter_id']
            tariff_id = request.form['tariff_id']
            billing_date = request.form['billing_date']
            due_date = request.form['due_date']

            # Validate meter_id and get customer_id
            cursor.execute("SELECT meter_id, customer_id FROM Meter WHERE meter_id = %s AND status='ACTIVE'", (meter_id,))
            meter = cursor.fetchone()
            if not meter:
                flash("❌ Invalid or inactive Meter ID.")
                return redirect(url_for('generate_bill'))
            customer_id = meter[1]

            # Validate tariff_id
            cursor.execute("SELECT tariff_id, unit_rate FROM Tariff WHERE tariff_id = %s", (tariff_id,))
            tariff = cursor.fetchone()
            if not tariff:
                flash("❌ Invalid Tariff ID.")
                return redirect(url_for('generate_bill'))
            unit_rate = float(tariff[1])  # Convert Decimal to float

            # Get latest two meter readings
            cursor.execute("""
                SELECT reading_value, reading_date
                FROM Meter_Reading
                WHERE meter_id = %s
                ORDER BY reading_date DESC
                LIMIT 2
            """, (meter_id,))
            readings = cursor.fetchall()

            if len(readings) < 2:
                flash("❌ Not enough meter readings to generate bill.")
                return redirect(url_for('generate_bill'))

            # Calculate units consumed (latest - previous)
            units_consumed = readings[0][0] - readings[1][0]
            if units_consumed < 0:
                flash("❌ Invalid meter readings: Latest reading is less than previous.")
                return redirect(url_for('generate_bill'))

            # Calculate amount due
            amount_due = units_consumed * unit_rate

            # Apply customer's credit balance
            cursor.execute("SELECT credit_balance FROM Customer WHERE customer_id = %s", (customer_id,))
            credit_balance = float(cursor.fetchone()[0] or 0.0)  # Convert Decimal to float
            amount_due = max(amount_due - credit_balance, 0.0)  # Ensure amount_due >= 0

            # Update credit balance (reduce by amount used)
            credit_used = min(credit_balance, units_consumed * unit_rate)
            cursor.execute("UPDATE Customer SET credit_balance = credit_balance - %s WHERE customer_id = %s", (credit_used, customer_id))

            # Insert bill
            query = """
                INSERT INTO Bill (meter_id, tariff_id, billing_date, due_date, amount_due, status)
                VALUES (%s, %s, %s, %s, %s, 'UNPAID')
            """
            values = (int(meter_id), int(tariff_id), billing_date, due_date, amount_due)
            cursor.execute(query, values)
            db.commit()

            flash(f"✅ Bill Generated Successfully! Amount: ₹{amount_due:.2f}")
        except mysql.connector.Error as err:
            if err.errno == 1452:
                flash("❌ Invalid Meter or Tariff ID — foreign key constraint failed.")
            else:
                flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('generate_bill'))

    # Fetch meters and tariffs for dropdowns
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT meter_id FROM Meter WHERE status='ACTIVE'")
        meters = cursor.fetchall()
        cursor.execute("SELECT tariff_id, plan_name FROM Tariff")
        tariffs = cursor.fetchall()
        return render_template('bill.html', meters=meters, tariffs=tariffs)
    finally:
        db.close()

@app.route('/payment', methods=['GET', 'POST'])
def make_payment():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            bill_id = request.form['bill_id']
            amount_paid = request.form['amount_paid']
            payment_date = request.form['payment_date']
            payment_method = request.form['payment_method']

            # Validate bill_id and get customer_id
            cursor.execute("""
                SELECT b.bill_id, b.amount_due, b.status, m.customer_id
                FROM Bill b
                JOIN Meter m ON b.meter_id = m.meter_id
                WHERE b.bill_id = %s AND b.status = 'UNPAID'
            """, (bill_id,))
            bill = cursor.fetchone()
            if not bill:
                flash("❌ Invalid or already paid Bill ID.")
                return redirect(url_for('make_payment'))
            customer_id = bill[3]

            # Validate amount_paid
            try:
                amount_paid = float(amount_paid)
                if amount_paid <= 0:
                    flash("❌ Amount paid must be positive.")
                    return redirect(url_for('make_payment'))
            except ValueError:
                flash("❌ Invalid amount paid format.")
                return redirect(url_for('make_payment'))

            # Insert payment
            query = "INSERT INTO Payment (bill_id, payment_date, amount_paid, payment_method) VALUES (%s, %s, %s, %s)"
            values = (int(bill_id), payment_date, amount_paid, payment_method)
            cursor.execute(query, values)

            # Update bill status and handle overpayment
            cursor.execute("SELECT SUM(amount_paid) FROM Payment WHERE bill_id = %s", (bill_id,))
            total_paid = float(cursor.fetchone()[0] or 0.0)  # Convert Decimal to float
            if total_paid >= float(bill[1]):  # bill[1] is amount_due, convert to float
                cursor.execute("UPDATE Bill SET status='PAID' WHERE bill_id = %s", (bill_id,))
                # Store overpayment in customer credit_balance
                overpayment = total_paid - float(bill[1])
                if overpayment > 0:
                    cursor.execute("UPDATE Customer SET credit_balance = credit_balance + %s WHERE customer_id = %s", (overpayment, customer_id))

            db.commit()
            flash(f"✅ Payment Recorded Successfully! Amount: ₹{amount_paid:.2f}")
        except mysql.connector.Error as err:
            if err.errno == 1452:
                flash("❌ Invalid Bill ID — foreign key constraint failed.")
            else:
                flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('make_payment'))

    # Fetch unpaid bills for dropdown with remaining amount
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("""
            SELECT b.bill_id, (b.amount_due - IFNULL(p.total_paid, 0)) AS remaining
            FROM Bill b
            LEFT JOIN (SELECT bill_id, SUM(amount_paid) AS total_paid FROM Payment GROUP BY bill_id) p
            ON b.bill_id = p.bill_id
            WHERE b.status = 'UNPAID'
        """)
        bills = [(row[0], float(row[1])) for row in cursor.fetchall()]  # Convert remaining to float
        return render_template('payment.html', bills=bills)
    finally:
        db.close()

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            customer_id = request.form['customer_id']
            technician_id = request.form['technician_id']
            description = request.form['description']
            date_reported = request.form['date_reported']
            status = request.form['status']

            # Validate customer_id
            cursor.execute("SELECT customer_id FROM Customer WHERE customer_id = %s", (customer_id,))
            if not cursor.fetchone():
                flash("❌ Invalid Customer ID.")
                return redirect(url_for('complaint'))

            # Validate technician_id (if provided)
            if technician_id:
                cursor.execute("SELECT technician_id FROM Technician WHERE technician_id = %s", (technician_id,))
                if not cursor.fetchone():
                    flash("❌ Invalid Technician ID.")
                    return redirect(url_for('complaint'))

            # Validate description
            if not description.strip():
                flash("❌ Complaint description cannot be empty.")
                return redirect(url_for('complaint'))
            if len(description) > 255:
                flash("❌ Description must be 255 characters or less.")
                return redirect(url_for('complaint'))

            # Insert complaint
            query = """
                INSERT INTO Complaint (customer_id, technician_id, description, date_reported, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (int(customer_id), int(technician_id) if technician_id else None, description, date_reported, status)
            cursor.execute(query, values)
            db.commit()

            flash("✅ Complaint Filed Successfully!")
        except mysql.connector.Error as err:
            if err.errno == 1452:
                flash("❌ Invalid Customer or Technician ID — foreign key constraint failed.")
            else:
                flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('complaint'))

    # Fetch customers, technicians, and all complaints
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT customer_id, name FROM Customer")
        customers = cursor.fetchall()
        cursor.execute("SELECT technician_id, name, role FROM Technician")
        technicians = cursor.fetchall()
        cursor.execute("""
            SELECT c.complaint_id, c.customer_id, cu.name AS customer_name, 
                   c.technician_id, t.name AS technician_name, 
                   c.description, c.status, c.date_reported
            FROM Complaint c
            JOIN Customer cu ON c.customer_id = cu.customer_id
            LEFT JOIN Technician t ON c.technician_id = t.technician_id
            ORDER BY c.date_reported DESC
        """)
        complaints = cursor.fetchall()
        return render_template('complaint.html', customers=customers, technicians=technicians, complaints=complaints)
    finally:
        db.close()

@app.route('/update_complaint/<int:complaint_id>', methods=['GET', 'POST'])
def update_complaint(complaint_id):
    if request.method == 'POST':
        db = get_db()
        try:
            cursor = db.cursor()
            technician_id = request.form['technician_id']
            status = request.form['status']

            # Validate complaint_id
            cursor.execute("SELECT complaint_id FROM Complaint WHERE complaint_id = %s", (complaint_id,))
            if not cursor.fetchone():
                flash("❌ Invalid Complaint ID.")
                return redirect(url_for('complaint'))

            # Validate technician_id (if provided)
            if technician_id:
                cursor.execute("SELECT technician_id FROM Technician WHERE technician_id = %s", (technician_id,))
                if not cursor.fetchone():
                    flash("❌ Invalid Technician ID.")
                    return redirect(url_for('complaint'))

            # Update complaint
            query = """
                UPDATE Complaint 
                SET technician_id = %s, status = %s
                WHERE complaint_id = %s
            """
            values = (int(technician_id) if technician_id else None, status, complaint_id)
            cursor.execute(query, values)
            db.commit()

            flash("✅ Complaint Updated Successfully!")
        except mysql.connector.Error as err:
            if err.errno == 1452:
                flash("❌ Invalid Technician ID — foreign key constraint failed.")
            else:
                flash(f"⚠️ Database Error: {err}")
        finally:
            db.close()
        return redirect(url_for('complaint'))

    # Fetch complaint details, customers, and technicians
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("""
            SELECT c.complaint_id, c.customer_id, cu.name AS customer_name, 
                   c.technician_id, t.name AS technician_name, 
                   c.description, c.status, c.date_reported
            FROM Complaint c
            JOIN Customer cu ON c.customer_id = cu.customer_id
            LEFT JOIN Technician t ON c.technician_id = t.technician_id
            WHERE c.complaint_id = %s
        """, (complaint_id,))
        complaint = cursor.fetchone()
        if not complaint:
            flash("❌ Complaint not found.")
            return redirect(url_for('complaint'))

        cursor.execute("SELECT technician_id, name, role FROM Technician")
        technicians = cursor.fetchall()
        return render_template('update_complaint.html', complaint=complaint, technicians=technicians)
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)