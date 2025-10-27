from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector
from mysql.connector import Error
import json
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '7410',  # Updated to your MySQL password
    'database': 'Electricity_Bill_Management'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
        else:
            logging.error("Failed to establish database connection")
            return None
    except Error as e:
        logging.error(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def dashboard():
    connection = get_db_connection()
    if connection is None:
        flash('Database connection failed!', 'error')
        return render_template('dashboard.html', total_customers=0, overdue_bills=0, total_revenue=0, active_meters=0, monthly_revenue={})

    cursor = connection.cursor()
    try:
        # Total Customers
        cursor.execute("SELECT COUNT(*) FROM Customer")
        total_customers = cursor.fetchone()[0]

        # Overdue Bills
        cursor.execute("SELECT COUNT(*) FROM Bill WHERE status = 'UNPAID' AND due_date < CURDATE()")
        overdue_bills = cursor.fetchone()[0]

        # Total Revenue
        cursor.execute("SELECT SUM(amount_paid) FROM Payment")
        total_revenue = cursor.fetchone()[0] or 0

        # Active Meters
        cursor.execute("SELECT COUNT(*) FROM Meter WHERE status = 'ACTIVE'")
        active_meters = cursor.fetchone()[0]

        # Daily Revenue
        cursor.execute("""
            SELECT DATE_FORMAT(p.payment_date, '%Y-%m-%d') AS day, SUM(p.amount_paid) AS revenue
            FROM Payment p
            GROUP BY day
            ORDER BY day
        """)
        monthly_revenue = {row[0]: float(row[1]) for row in cursor.fetchall()}
    except Error as e:
        logging.error(f"Error fetching dashboard data: {e}")
        flash(f"Error fetching dashboard data: {e}", 'error')
        return render_template('dashboard.html', total_customers=0, overdue_bills=0, total_revenue=0, active_meters=0, monthly_revenue={})
    finally:
        cursor.close()
        connection.close()

    return render_template('dashboard.html', total_customers=total_customers, overdue_bills=overdue_bills,
                           total_revenue=total_revenue, active_meters=active_meters, monthly_revenue=json.dumps(monthly_revenue))


@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        contact_number = request.form['contact_number']
        email = request.form['email']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Customer (name, address, contact_number, email, credit_balance)
                    VALUES (%s, %s, %s, %s, 0.0)
                """, (name, address, contact_number, email))
                connection.commit()
                flash('✅ Customer Created Successfully!', 'success')
            except Error as e:
                logging.error(f"Error adding customer: {e}")
                flash(f"Error adding customer: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('add_customer'))
    return render_template('add_customer.html')

@app.route('/add_meter', methods=['GET', 'POST'])
def add_meter():
    connection = get_db_connection()
    customers = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT customer_id, name FROM Customer")
            customers = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching customers: {e}")
            flash(f"Error fetching customers: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        installation_date = request.form['installation_date']
        status = request.form['status']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Meter (customer_id, installation_date, status)
                    VALUES (%s, %s, %s)
                """, (customer_id, installation_date, status))
                connection.commit()
                flash('✅ Meter Added Successfully!', 'success')
            except Error as e:
                logging.error(f"Error adding meter: {e}")
                flash(f"Error adding meter: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('add_meter'))
    return render_template('add_meter.html', customers=customers)

@app.route('/add_reading', methods=['GET', 'POST'])
def add_reading():
    connection = get_db_connection()
    meters = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT meter_id, customer_id FROM Meter")
            meters = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching meters: {e}")
            flash(f"Error fetching meters: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        meter_id = request.form['meter_id']
        reading_date = request.form['reading_date']
        reading_value = request.form['reading_value']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Meter_Reading (meter_id, reading_date, reading_value)
                    VALUES (%s, %s, %s)
                """, (meter_id, reading_date, reading_value))
                connection.commit()
                flash('✅ Meter Reading Recorded Successfully!', 'success')
            except Error as e:
                logging.error(f"Error adding reading: {e}")
                flash(f"Error adding reading: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('add_reading'))
    return render_template('add_reading.html', meters=meters)

@app.route('/add_tariff', methods=['GET', 'POST'])
def add_tariff():
    if request.method == 'POST':
        plan_name = request.form['plan_name']
        unit_rate = request.form['unit_rate']
        applicable_from_date = request.form['applicable_from_date']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Tariff (plan_name, unit_rate, applicable_from_date)
                    VALUES (%s, %s, %s)
                """, (plan_name, unit_rate, applicable_from_date))
                connection.commit()
                flash('✅ Tariff Plan Added Successfully!', 'success')
            except Error as e:
                logging.error(f"Error adding tariff: {e}")
                flash(f"Error adding tariff: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('add_tariff'))
    return render_template('add_tariff.html')

@app.route('/bill', methods=['GET', 'POST'])
def bill():
    connection = get_db_connection()
    meters = []
    tariffs = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT meter_id, customer_id FROM Meter")
            meters = cursor.fetchall()
            cursor.execute("SELECT tariff_id, plan_name FROM Tariff")
            tariffs = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching data: {e}")
            flash(f"Error fetching data: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        meter_id = request.form['meter_id']
        tariff_id = request.form['tariff_id']
        billing_date = request.form['billing_date']
        due_date = request.form['due_date']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    SELECT reading_value, reading_date 
                    FROM Meter_Reading 
                    WHERE meter_id = %s 
                    ORDER BY reading_date DESC LIMIT 2
                """, (meter_id,))
                readings = cursor.fetchall()
                if len(readings) < 2:
                    flash('Insufficient readings to generate bill', 'error')
                else:
                    units_consumed = readings[0][0] - readings[1][0]
                    cursor.execute("SELECT unit_rate FROM Tariff WHERE tariff_id = %s", (tariff_id,))
                    unit_rate = cursor.fetchone()[0]
                    amount_due = units_consumed * unit_rate
                    cursor.execute("""
                        INSERT INTO Bill (meter_id, tariff_id, billing_date, due_date, amount_due, status)
                        VALUES (%s, %s, %s, %s, %s, 'UNPAID')
                    """, (meter_id, tariff_id, billing_date, due_date, amount_due))
                    connection.commit()
                    flash('✅ Bill Generated Successfully!', 'success')
            except Error as e:
                logging.error(f"Error generating bill: {e}")
                flash(f"Error generating bill: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('bill'))
    return render_template('bill.html', meters=meters, tariffs=tariffs)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    connection = get_db_connection()
    bills = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT bill_id, meter_id, amount_due FROM Bill WHERE status = 'UNPAID'")
            bills = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching bills: {e}")
            flash(f"Error fetching bills: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        bill_id = request.form['bill_id']
        payment_date = request.form['payment_date']
        amount_paid = float(request.form['amount_paid'])
        payment_method = request.form['payment_method']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT amount_due, meter_id FROM Bill WHERE bill_id = %s", (bill_id,))
                bill = cursor.fetchone()
                if not bill:
                    flash('Bill not found', 'error')
                else:
                    amount_due, meter_id = bill
                    cursor.execute("SELECT customer_id FROM Meter WHERE meter_id = %s", (meter_id,))
                    customer_id = cursor.fetchone()[0]
                    cursor.execute("""
                        INSERT INTO Payment (bill_id, payment_date, amount_paid, payment_method)
                        VALUES (%s, %s, %s, %s)
                    """, (bill_id, payment_date, amount_paid, payment_method))
                    if amount_paid >= amount_due:
                        cursor.execute("UPDATE Bill SET status = 'PAID' WHERE bill_id = %s", (bill_id,))
                    excess = amount_paid - amount_due if amount_paid > amount_due else 0
                    if excess > 0:
                        cursor.execute("""
                            UPDATE Customer SET credit_balance = credit_balance + %s WHERE customer_id = %s
                        """, (excess, customer_id))
                    connection.commit()
                    flash('✅ Payment Recorded Successfully!', 'success')
            except Error as e:
                logging.error(f"Error recording payment: {e}")
                flash(f"Error recording payment: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('payment'))
    return render_template('payment.html', bills=bills)

@app.route('/complaint', methods=['GET', 'POST'])
def complaint():
    connection = get_db_connection()
    customers = []
    technicians = []
    complaints = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT customer_id, name FROM Customer")
            customers = cursor.fetchall()
            cursor.execute("SELECT technician_id, name FROM Technician")
            technicians = cursor.fetchall()
            cursor.execute("""
                SELECT c.complaint_id, c.customer_id, cu.name, c.technician_id, t.name, c.description, c.date_reported, c.status
                FROM Complaint c
                JOIN Customer cu ON c.customer_id = cu.customer_id
                LEFT JOIN Technician t ON c.technician_id = t.technician_id
            """)
            complaints = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching complaint data: {e}")
            flash(f"Error fetching complaint data: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        technician_id = request.form['technician_id'] or None
        description = request.form['description']
        date_reported = request.form['date_reported']
        status = request.form['status']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Complaint (customer_id, technician_id, description, date_reported, status)
                    VALUES (%s, %s, %s, %s, %s)
                """, (customer_id, technician_id, description, date_reported, status))
                connection.commit()
                flash('✅ Complaint Filed Successfully!', 'success')
            except Error as e:
                logging.error(f"Error filing complaint: {e}")
                flash(f"Error filing complaint: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('complaint'))
    return render_template('complaint.html', customers=customers, technicians=technicians, complaints=complaints)

@app.route('/update_complaint/<int:complaint_id>', methods=['GET', 'POST'])
def update_complaint(complaint_id):
    connection = get_db_connection()
    complaint = None
    technicians = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT complaint_id, customer_id, technician_id, description, date_reported, status
                FROM Complaint WHERE complaint_id = %s
            """, (complaint_id,))
            complaint = cursor.fetchone()
            cursor.execute("SELECT technician_id, name FROM Technician")
            technicians = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching complaint data: {e}")
            flash(f"Error fetching complaint data: {e}", 'error')
        finally:
            cursor.close()
            connection.close()

    if request.method == 'POST':
        technician_id = request.form['technician_id'] or None
        status = request.form['status']
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    UPDATE Complaint SET technician_id = %s, status = %s WHERE complaint_id = %s
                """, (technician_id, status, complaint_id))
                connection.commit()
                flash('✅ Complaint Updated Successfully!', 'success')
            except Error as e:
                logging.error(f"Error updating complaint: {e}")
                flash(f"Error updating complaint: {e}", 'error')
            finally:
                cursor.close()
                connection.close()
        else:
            flash('Database connection failed!', 'error')
        return redirect(url_for('complaint'))
    return render_template('update_complaint.html', complaint=complaint, technicians=technicians)

@app.route('/customers_list')
def customers_list():
    connection = get_db_connection()
    customers = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT customer_id, name, address, contact_number, email, credit_balance FROM Customer")
            customers = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching customers: {e}")
            flash(f"Error fetching customers: {e}", 'error')
        finally:
            cursor.close()
            connection.close()
    return render_template('customers_list.html', customers=customers)

@app.route('/active_meters')
def active_meters():
    connection = get_db_connection()
    meters = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT m.meter_id, m.customer_id, c.name, m.installation_date, m.status
                FROM Meter m JOIN Customer c ON m.customer_id = c.customer_id
                WHERE m.status = 'ACTIVE'
            """)
            meters = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching active meters: {e}")
            flash(f"Error fetching active meters: {e}", 'error')
        finally:
            cursor.close()
            connection.close()
    return render_template('active_meters.html', meters=meters)

@app.route('/overdue_bills')
def overdue_bills():
    connection = get_db_connection()
    overdue_customers = []
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT c.customer_id, c.name, c.address, c.contact_number, c.email, b.bill_id, b.amount_due, b.due_date
                FROM Customer c
                JOIN Meter m ON c.customer_id = m.customer_id
                JOIN Bill b ON m.meter_id = b.meter_id
                WHERE b.status = 'UNPAID' AND b.due_date < CURDATE()
            """)
            overdue_customers = cursor.fetchall()
        except Error as e:
            logging.error(f"Error fetching overdue bills: {e}")
            flash(f"Error fetching overdue bills: {e}", 'error')
        finally:
            cursor.close()
            connection.close()
    return render_template('overdue_bills.html', overdue_customers=overdue_customers)

if __name__ == '__main__':
    app.run(debug=True)