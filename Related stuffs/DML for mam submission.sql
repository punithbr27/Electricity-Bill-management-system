-- DML Statements for Electricity Bill Management System
USE Electricity_Bill_Management;

-- Insert data into Customer
INSERT INTO Customer (customer_id, name, address, contact_number, email)
VALUES
(101, 'Ravi Kumar', 'Rajajinagar, Bangalore', '9876543210', 'ravi.kumar@gmail.com'),
(102, 'Sneha Reddy', 'Indiranagar, Bangalore', '9876501234', 'sneha.reddy@gmail.com'),
(103, 'Amit Singh', 'Whitefield, Bangalore', '9998844221', 'amit.singh@gmail.com');

-- Insert data into Meter
INSERT INTO Meter (meter_id, customer_id, installation_date, status)
VALUES
(201, 101, '2023-01-15', 'Active'),
(202, 102, '2023-03-20', 'Active'),
(203, 103, '2023-04-10', 'Inactive');

-- Insert data into Tariff
INSERT INTO Tariff (tariff_id, plan_name, unit_rate, applicable_from_date)
VALUES
(301, 'Residential Plan', 6.50, '2023-01-01'),
(302, 'Commercial Plan', 8.75, '2023-01-01');

-- Insert data into Meter_Reading
INSERT INTO Meter_Reading (reading_id, meter_id, reading_date, reading_value)
VALUES
(401, 201, '2024-05-01', 250),
(402, 202, '2024-05-01', 400),
(403, 203, '2024-05-01', 150);

-- Insert data into Bill
INSERT INTO Bill (bill_id, meter_id, tariff_id, billing_date, due_date, amount_due, status)
VALUES
(501, 201, 301, '2024-05-02', '2024-05-20', 1625.00, 'Unpaid'),
(502, 202, 302, '2024-05-02', '2024-05-20', 3500.00, 'Paid'),
(503, 203, 301, '2024-05-02', '2024-05-20', 975.00, 'Unpaid');

-- Insert data into Payment
INSERT INTO Payment (payment_id, bill_id, payment_date, amount_paid, payment_method)
VALUES
(601, 502, '2024-05-10', 3500.00, 'UPI');

-- Insert data into Technician
INSERT INTO Technician (technician_id, name, contact_number, area_of_operation, role)
VALUES
(701, 'Kiran Kumar', '9845012345', 'South Bangalore', 'Meter Maintenance'),
(702, 'Ramesh Gowda', '9845087654', 'North Bangalore', 'Complaint Handling');

-- Insert data into Complaint
INSERT INTO Complaint (complaint_id, customer_id, technician_id, description, date_reported, status)
VALUES
(801, 101, 702, 'Meter not working properly', '2024-06-01', 'Pending'),
(802, 103, 701, 'Bill amount too high', '2024-06-05', 'Resolved');

-- Verify Data
SELECT * FROM Customer;
SELECT * FROM Meter;
SELECT * FROM Tariff;
SELECT * FROM Meter_Reading;
SELECT * FROM Bill;
SELECT * FROM Payment;
SELECT * FROM Technician;
SELECT * FROM Complaint;

