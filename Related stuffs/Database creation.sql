-- Drop database if it exists
DROP DATABASE IF EXISTS Electricity_Bill_Management;

-- Create database
CREATE DATABASE Electricity_Bill_Management;
USE Electricity_Bill_Management;

-- Create Customer table with credit_balance
CREATE TABLE Customer (
    customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    address VARCHAR(255),
    contact_number VARCHAR(255),
    email VARCHAR(255),
    credit_balance DECIMAL DEFAULT 0.0
);

-- Create Meter table
CREATE TABLE Meter (
    meter_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    installation_date DATE,
    status VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Create Tariff table
CREATE TABLE Tariff (
    tariff_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(255),
    unit_rate DECIMAL,
    applicable_from_date DATE
);

-- Create Bill table
CREATE TABLE Bill (
    bill_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    meter_id INTEGER NOT NULL,
    tariff_id INTEGER NOT NULL,
    billing_date DATE,
    due_date DATE,
    amount_due DECIMAL,
    status VARCHAR(255),
    FOREIGN KEY (meter_id) REFERENCES Meter(meter_id),
    FOREIGN KEY (tariff_id) REFERENCES Tariff(tariff_id)
);

-- Create Payment table
CREATE TABLE Payment (
    payment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    bill_id INTEGER NOT NULL,
    payment_date DATE,
    amount_paid DECIMAL,
    payment_method VARCHAR(255),
    FOREIGN KEY (bill_id) REFERENCES Bill(bill_id)
);

-- Create Meter_Reading table
CREATE TABLE Meter_Reading (
    reading_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    meter_id INTEGER NOT NULL,
    reading_date DATE,
    reading_value INTEGER,
    FOREIGN KEY (meter_id) REFERENCES Meter(meter_id)
);

-- Create Technician table
CREATE TABLE Technician (
    technician_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    contact_number VARCHAR(255),
    area_of_operation VARCHAR(255),
    role VARCHAR(255)
);

-- Create Complaint table
CREATE TABLE Complaint (
    complaint_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INTEGER NOT NULL,
    technician_id INTEGER,
    description VARCHAR(255),
    date_reported DATE,
    status VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (technician_id) REFERENCES Technician(technician_id)
);