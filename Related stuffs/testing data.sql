-- Insert 20 Customers
INSERT INTO Customer (name, address, contact_number, email, credit_balance) VALUES
('Aarav Sharma', '123 MG Road, Bangalore', '9876543210', 'aarav@example.com', 0.0),
('Bhavya Patel', '456 Koramangala, Bangalore', '9876543211', 'bhavya@example.com', 50.0),
('Chirag Gupta', '789 Indiranagar, Bangalore', '9876543212', 'chirag@example.com', 0.0),
('Diya Singh', '101 Whitefield, Bangalore', '9876543213', 'diya@example.com', 100.0),
('Esha Verma', '202 Jayanagar, Bangalore', '9876543214', 'esha@example.com', 0.0),
('Farhan Khan', '303 HSR Layout, Bangalore', '9876543215', 'farhan@example.com', 20.0),
('Gauri Desai', '404 Malleshwaram, Bangalore', '9876543216', 'gauri@example.com', 0.0),
('Hrithik Jain', '505 BTM Layout, Bangalore', '9876543217', 'hrithik@example.com', 0.0),
('Ishaani Reddy', '606 Marathahalli, Bangalore', '9876543218', 'ishaani@example.com', 0.0),
('Jatin Malhotra', '707 Electronic City, Bangalore', '9876543219', 'jatin@example.com', 30.0),
('Kavya Nair', '808 Yelahanka, Bangalore', '9876543220', 'kavya@example.com', 0.0),
('Lakshmi Rao', '909 Rajajinagar, Bangalore', '9876543221', 'lakshmi@example.com', 0.0),
('Manav Shah', '1010 Bellandur, Bangalore', '9876543222', 'manav@example.com', 0.0),
('Nisha Kapoor', '1111 Banashankari, Bangalore', '9876543223', 'nisha@example.com', 0.0),
('Omkar Yadav', '1212 Hebbal, Bangalore', '9876543224', 'omkar@example.com', 0.0),
('Pooja Menon', '1313 Sarjapur, Bangalore', '9876543225', 'pooja@example.com', 0.0),
('Rahul Iyer', '1414 Vijayanagar, Bangalore', '9876543226', 'rahul@example.com', 0.0),
('Sanya Bose', '1515 JP Nagar, Bangalore', '9876543227', 'sanya@example.com', 0.0),
('Tanvi Kulkarni', '1616 Basavanagudi, Bangalore', '9876543228', 'tanvi@example.com', 0.0),
('Vikram Shetty', '1717 Domlur, Bangalore', '9876543229', 'vikram@example.com', 0.0);

-- Insert 30 Meters
INSERT INTO Meter (customer_id, installation_date, status) VALUES
(1, '2025-01-01', 'ACTIVE'), (1, '2025-01-02', 'ACTIVE'), (2, '2025-01-03', 'ACTIVE'),
(3, '2025-01-04', 'ACTIVE'), (4, '2025-01-05', 'ACTIVE'), (4, '2025-01-06', 'INACTIVE'),
(5, '2025-01-07', 'ACTIVE'), (6, '2025-01-08', 'ACTIVE'), (7, '2025-01-09', 'ACTIVE'),
(8, '2025-01-10', 'ACTIVE'), (9, '2025-01-11', 'ACTIVE'), (10, '2025-01-12', 'ACTIVE'),
(11, '2025-01-13', 'ACTIVE'), (12, '2025-01-14', 'ACTIVE'), (13, '2025-01-15', 'ACTIVE'),
(14, '2025-01-16', 'ACTIVE'), (15, '2025-01-17', 'ACTIVE'), (16, '2025-01-18', 'ACTIVE'),
(17, '2025-01-19', 'ACTIVE'), (18, '2025-01-20', 'ACTIVE'), (19, '2025-01-21', 'ACTIVE'),
(20, '2025-01-22', 'ACTIVE'), (1, '2025-01-23', 'ACTIVE'), (2, '2025-01-24', 'ACTIVE'),
(3, '2025-01-25', 'ACTIVE'), (4, '2025-01-26', 'ACTIVE'), (5, '2025-01-27', 'ACTIVE'),
(6, '2025-01-28', 'ACTIVE'), (7, '2025-01-29', 'ACTIVE'), (8, '2025-01-30', 'ACTIVE');

-- Insert 10 Tariffs
INSERT INTO Tariff (plan_name, unit_rate, applicable_from_date) VALUES
('Residential Basic', 5.50, '2025-01-01'), ('Residential Premium', 6.75, '2025-01-01'),
('Commercial Standard', 8.00, '2025-01-01'), ('Commercial High', 9.25, '2025-01-01'),
('Industrial', 7.50, '2025-01-01'), ('Residential Eco', 5.00, '2025-02-01'),
('Commercial Eco', 7.00, '2025-02-01'), ('Residential Night', 4.50, '2025-02-01'),
('Commercial Night', 6.50, '2025-02-01'), ('Industrial Heavy', 8.50, '2025-02-01');

-- Insert 100 Meter Readings
INSERT INTO Meter_Reading (meter_id, reading_date, reading_value) VALUES
(1, '2025-02-01', 1000), (1, '2025-03-01', 1200), (1, '2025-04-01', 1450), (1, '2025-05-01', 1700),
(2, '2025-02-01', 800), (2, '2025-03-01', 950), (2, '2025-04-01', 1100), (3, '2025-02-01', 2000),
(3, '2025-03-01', 2300), (3, '2025-04-01', 2600), (4, '2025-02-01', 1500), (4, '2025-03-01', 1800),
(5, '2025-02-01', 900), (5, '2025-03-01', 1100), (6, '2025-02-01', 1200), (6, '2025-03-01', 1400),
(7, '2025-02-01', 1300), (7, '2025-03-01', 1600), (8, '2025-02-01', 1700), (8, '2025-03-01', 2000),
(9, '2025-02-01', 1000), (9, '2025-03-01', 1250), (10, '2025-02-01', 1400), (10, '2025-03-01', 1650),
(11, '2025-02-01', 1100), (11, '2025-03-01', 1300), (12, '2025-02-01', 900), (12, '2025-03-01', 1100),
(13, '2025-02-01', 1600), (13, '2025-03-01', 1900), (14, '2025-02-01', 1200), (14, '2025-03-01', 1400),
(15, '2025-02-01', 1000), (15, '2025-03-01', 1250), (16, '2025-02-01', 1300), (16, '2025-03-01', 1550),
(17, '2025-02-01', 1100), (17, '2025-03-01', 1350), (18, '2025-02-01', 1400), (18, '2025-03-01', 1700),
(19, '2025-02-01', 1200), (19, '2025-03-01', 1450), (20, '2025-02-01', 1000), (20, '2025-03-01', 1300),
(21, '2025-02-01', 900), (21, '2025-03-01', 1100), (22, '2025-02-01', 1500), (22, '2025-03-01', 1800),
(23, '2025-02-01', 1100), (23, '2025-03-01', 1350), (24, '2025-02-01', 1200), (24, '2025-03-01', 1400),
(25, '2025-02-01', 1000), (25, '2025-03-01', 1250), (26, '2025-02-01', 1300), (26, '2025-03-01', 1550),
(27, '2025-02-01', 1100), (27, '2025-03-01', 1350), (28, '2025-02-01', 1400), (28, '2025-03-01', 1700),
(29, '2025-02-01', 1200), (29, '2025-03-01', 1450), (30, '2025-02-01', 1000), (30, '2025-03-01', 1300),
(1, '2025-06-01', 2000), (2, '2025-06-01', 1300), (3, '2025-06-01', 2900), (4, '2025-06-01', 2100),
(5, '2025-06-01', 1400), (6, '2025-06-01', 1700), (7, '2025-06-01', 1900), (8, '2025-06-01', 2300),
(9, '2025-06-01', 1500), (10, '2025-06-01', 1900), (11, '2025-06-01', 1600), (12, '2025-06-01', 1400),
(13, '2025-06-01', 2200), (14, '2025-06-01', 1700), (15, '2025-06-01', 1500), (16, '2025-06-01', 1800),
(17, '2025-06-01', 1600), (18, '2025-06-01', 2000), (19, '2025-06-01', 1700), (20, '2025-06-01', 1600),
(21, '2025-06-01', 1400), (22, '2025-06-01', 2100), (23, '2025-06-01', 1600), (24, '2025-06-01', 1700),
(25, '2025-06-01', 1500), (26, '2025-06-01', 1800), (27, '2025-06-01', 1600), (28, '2025-06-01', 2000),
(29, '2025-06-01', 1700), (30, '2025-06-01', 1600);

-- Insert 50 Bills
INSERT INTO Bill (meter_id, tariff_id, billing_date, due_date, amount_due, status) VALUES
(1, 1, '2025-03-01', '2025-03-15', 1100.00, 'UNPAID'), (2, 2, '2025-03-01', '2025-03-15', 1012.50, 'PAID'),
(3, 3, '2025-03-01', '2025-03-15', 2400.00, 'UNPAID'), (4, 4, '2025-03-01', '2025-03-15', 2775.00, 'PAID'),
(5, 5, '2025-03-01', '2025-03-15', 1500.00, 'UNPAID'), (6, 6, '2025-03-01', '2025-03-15', 1000.00, 'PAID'),
(7, 7, '2025-03-01', '2025-03-15', 2100.00, 'UNPAID'), (8, 8, '2025-03-01', '2025-03-15', 1350.00, 'PAID'),
(9, 9, '2025-03-01', '2025-03-15', 1625.00, 'UNPAID'), (10, 10, '2025-03-01', '2025-03-15', 1875.00, 'PAID'),
(11, 1, '2025-03-01', '2025-03-15', 1100.00, 'UNPAID'), (12, 2, '2025-03-01', '2025-03-15', 1350.00, 'PAID'),
(13, 3, '2025-03-01', '2025-03-15', 2400.00, 'UNPAID'), (14, 4, '2025-03-01', '2025-03-15', 1850.00, 'PAID'),
(15, 5, '2025-03-01', '2025-03-15', 1875.00, 'UNPAID'), (16, 6, '2025-03-01', '2025-03-15', 1250.00, 'PAID'),
(17, 7, '2025-03-01', '2025-03-15', 1750.00, 'UNPAID'), (18, 8, '2025-03-01', '2025-03-15', 1350.00, 'PAID'),
(19, 9, '2025-03-01', '2025-03-15', 1625.00, 'UNPAID'), (20, 10, '2025-03-01', '2025-03-15', 2250.00, 'PAID'),
(21, 1, '2025-03-01', '2025-03-15', 1100.00, 'UNPAID'), (22, 2, '2025-03-01', '2025-03-15', 2025.00, 'PAID'),
(23, 3, '2025-03-01', '2025-03-15', 2000.00, 'UNPAID'), (24, 4, '2025-03-01', '2025-03-15', 1850.00, 'PAID'),
(25, 5, '2025-03-01', '2025-03-15', 1875.00, 'UNPAID'), (26, 6, '2025-03-01', '2025-03-15', 1250.00, 'PAID'),
(27, 7, '2025-03-01', '2025-03-15', 1750.00, 'UNPAID'), (28, 8, '2025-03-01', '2025-03-15', 1350.00, 'PAID'),
(29, 9, '2025-03-01', '2025-03-15', 1625.00, 'UNPAID'), (30, 10, '2025-03-01', '2025-03-15', 2250.00, 'PAID'),
(1, 1, '2025-04-01', '2025-04-15', 1375.00, 'UNPAID'), (2, 2, '2025-04-01', '2025-04-15', 1012.50, 'PAID'),
(3, 3, '2025-04-01', '2025-04-15', 2400.00, 'UNPAID'), (4, 4, '2025-04-01', '2025-04-15', 2775.00, 'PAID'),
(5, 5, '2025-04-01', '2025-04-15', 2250.00, 'UNPAID'), (6, 6, '2025-04-01', '2025-04-15', 1500.00, 'PAID'),
(7, 7, '2025-04-01', '2025-04-15', 2100.00, 'UNPAID'), (8, 8, '2025-04-01', '2025-04-15', 1350.00, 'PAID'),
(9, 9, '2025-04-01', '2025-04-15', 1625.00, 'UNPAID'), (10, 10, '2025-04-01', '2025-04-15', 1875.00, 'PAID'),
(11, 1, '2025-04-01', '2025-04-15', 1100.00, 'UNPAID'), (12, 2, '2025-04-01', '2025-04-15', 1350.00, 'PAID'),
(13, 3, '2025-04-01', '2025-04-15', 2400.00, 'UNPAID'), (14, 4, '2025-04-01', '2025-04-15', 1850.00, 'PAID'),
(15, 5, '2025-04-01', '2025-04-15', 1875.00, 'UNPAID'), (16, 6, '2025-04-01', '2025-04-15', 1250.00, 'PAID'),
(17, 7, '2025-04-01', '2025-04-15', 1750.00, 'UNPAID'), (18, 8, '2025-04-01', '2025-04-15', 1350.00, 'PAID'),
(19, 9, '2025-04-01', '2025-04-15', 1625.00, 'UNPAID'), (20, 10, '2025-04-01', '2025-04-15', 2250.00, 'PAID');

-- Insert 40 Payments
INSERT INTO Payment (bill_id, payment_date, amount_paid, payment_method) VALUES
(2, '2025-03-02', 1012.50, 'Credit Card'), (4, '2025-03-03', 2775.00, 'UPI'),
(6, '2025-03-04', 1000.00, 'Cash'), (8, '2025-03-05', 1350.00, 'Credit Card'),
(10, '2025-03-06', 2000.00, 'UPI'), (12, '2025-03-07', 1350.00, 'Cash'),
(14, '2025-03-08', 1850.00, 'Credit Card'), (16, '2025-03-09', 1250.00, 'UPI'),
(18, '2025-03-10', 1350.00, 'Cash'), (20, '2025-03-11', 2500.00, 'Credit Card'),
(22, '2025-03-12', 2025.00, 'UPI'), (24, '2025-03-13', 1850.00, 'Cash'),
(26, '2025-03-14', 1250.00, 'Credit Card'), (28, '2025-03-15', 1350.00, 'UPI'),
(30, '2025-03-16', 2250.00, 'Cash'), (32, '2025-04-02', 1012.50, 'Credit Card'),
(34, '2025-04-03', 2775.00, 'UPI'), (36, '2025-04-04', 1500.00, 'Cash'),
(38, '2025-04-05', 1350.00, 'Credit Card'), (40, '2025-04-06', 1875.00, 'UPI'),
(42, '2025-04-07', 1350.00, 'Cash'), (44, '2025-04-08', 1850.00, 'Credit Card'),
(46, '2025-04-09', 1250.00, 'UPI'), (48, '2025-04-10', 1350.00, 'Cash'),
(50, '2025-04-11', 2250.00, 'Credit Card'), (2, '2025-03-03', 500.00, 'UPI'),
(4, '2025-03-04', 1000.00, 'Cash'), (6, '2025-03-05', 500.00, 'Credit Card'),
(8, '2025-03-06', 500.00, 'UPI'), (10, '2025-03-07', 1000.00, 'Cash'),
(12, '2025-03-08', 500.00, 'Credit Card'), (14, '2025-03-09', 500.00, 'UPI'),
(16, '2025-03-10', 500.00, 'Cash'), (18, '2025-03-11', 500.00, 'Credit Card'),
(20, '2025-03-12', 1000.00, 'UPI'), (22, '2025-03-13', 500.00, 'Cash'),
(24, '2025-03-14', 500.00, 'Credit Card'), (26, '2025-03-15', 500.00, 'UPI'),
(28, '2025-03-16', 500.00, 'Cash'), (30, '2025-03-17', 1000.00, 'Credit Card');

-- Insert 10 Technicians
INSERT INTO Technician (name, contact_number, area_of_operation, role) VALUES
('Ravi Kumar', '9876543301', 'MG Road', 'Electrician'),
('Sneha Patil', '9876543302', 'Koramangala', 'Supervisor'),
('Vijay Singh', '9876543303', 'Indiranagar', 'Technician'),
('Anita Sharma', '9876543304', 'Whitefield', 'Electrician'),
('Rohan Gupta', '9876543305', 'Jayanagar', 'Supervisor'),
('Priya Nair', '9876543306', 'HSR Layout', 'Technician'),
('Arjun Reddy', '9876543307', 'Malleshwaram', 'Electrician'),
('Meena Desai', '9876543308', 'BTM Layout', 'Supervisor'),
('Kiran Yadav', '9876543309', 'Marathahalli', 'Technician'),
('Suresh Menon', '9876543310', 'Electronic City', 'Electrician');

-- Insert 30 Complaints
INSERT INTO Complaint (customer_id, technician_id, description, date_reported, status) VALUES
(1, NULL, 'Power outage in area', '2025-03-01', 'OPEN'),
(2, 1, 'Incorrect bill amount', '2025-03-02', 'IN_PROGRESS'),
(3, 2, 'Meter not working', '2025-03-03', 'RESOLVED'),
(4, NULL, 'Frequent power cuts', '2025-03-04', 'OPEN'),
(5, 3, 'Sparking wires', '2025-03-05', 'IN_PROGRESS'),
(6, 4, 'Billing dispute', '2025-03-06', 'OPEN'),
(7, NULL, 'Low voltage issue', '2025-03-07', 'OPEN'),
(8, 5, 'Meter reading error', '2025-03-08', 'RESOLVED'),
(9, 6, 'Power surge damage', '2025-03-09', 'IN_PROGRESS'),
(10, NULL, 'Streetlight not working', '2025-03-10', 'OPEN'),
(11, 7, 'Transformer issue', '2025-03-11', 'IN_PROGRESS'),
(12, 8, 'Billing error', '2025-03-12', 'RESOLVED'),
(13, NULL, 'Power outage', '2025-03-13', 'OPEN'),
(14, 9, 'Meter replacement needed', '2025-03-14', 'IN_PROGRESS'),
(15, 10, 'Voltage fluctuation', '2025-03-15', 'OPEN'),
(16, NULL, 'Power cut complaint', '2025-03-16', 'OPEN'),
(17, 1, 'Incorrect billing', '2025-03-17', 'RESOLVED'),
(18, 2, 'Meter malfunction', '2025-03-18', 'IN_PROGRESS'),
(19, NULL, 'Power supply issue', '2025-03-19', 'OPEN'),
(20, 3, 'Wiring problem', '2025-03-20', 'OPEN'),
(1, 4, 'Billing dispute', '2025-03-21', 'IN_PROGRESS'),
(2, NULL, 'Power outage', '2025-03-22', 'OPEN'),
(3, 5, 'Meter reading issue', '2025-03-23', 'RESOLVED'),
(4, 6, 'Voltage drop', '2025-03-24', 'IN_PROGRESS'),
(5, NULL, 'Streetlight issue', '2025-03-25', 'OPEN'),
(6, 7, 'Transformer fault', '2025-03-26', 'OPEN'),
(7, 8, 'Billing error', '2025-03-27', 'RESOLVED'),
(8, NULL, 'Power surge', '2025-03-28', 'OPEN'),
(9, 9, 'Meter not working', '2025-03-29', 'IN_PROGRESS'),
(10, 10, 'Low voltage', '2025-03-30', 'OPEN');



SELECT COUNT(*) FROM Customer; -- Should return 20
SELECT COUNT(*) FROM Meter; -- Should return 30
SELECT COUNT(*) FROM Tariff; -- Should return 10
SELECT COUNT(*) FROM Meter_Reading; -- Should return 100
SELECT COUNT(*) FROM Bill; -- Should return 50
SELECT COUNT(*) FROM Payment; -- Should return 40
SELECT COUNT(*) FROM Technician; -- Should return 10
SELECT COUNT(*) FROM Complaint; -- Should return 30


SELECT customer_id FROM Customer; -- Should be 1–20
SELECT meter_id FROM Meter; -- Should be 1–30
SELECT tariff_id FROM Tariff; -- Should be 1–10
SELECT bill_id FROM Bill; -- Should be 1–50
SELECT technician_id FROM Technician; -- Should be 1–10
SELECT complaint_id FROM Complaint; -- Should be 1–30