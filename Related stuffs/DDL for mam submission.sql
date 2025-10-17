-- DDL Statements for Electricity Bill Management System
CREATE DATABASE Electricity_Bill_Management;
USE Electricity_Bill_Management;

-- Customer Table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(15) UNIQUE,
    email VARCHAR(100)
);

-- Meter Table
CREATE TABLE Meter (
    meter_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    installation_date DATE,
    status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

-- Tariff Table
CREATE TABLE Tariff (
    tariff_id INT PRIMARY KEY,
    plan_name VARCHAR(50) NOT NULL,
    unit_rate DECIMAL(10,2) CHECK (unit_rate > 0),
    applicable_from_date DATE
);

-- Meter Reading Table
CREATE TABLE Meter_Reading (
    reading_id INT PRIMARY KEY,
    meter_id INT NOT NULL,
    reading_date DATE NOT NULL,
    reading_value INT CHECK (reading_value >= 0),
    FOREIGN KEY (meter_id) REFERENCES Meter(meter_id)
);

-- Bill Table
CREATE TABLE Bill (
    bill_id INT PRIMARY KEY,
    meter_id INT NOT NULL,
    tariff_id INT NOT NULL,
    billing_date DATE NOT NULL,
    due_date DATE,
    amount_due DECIMAL(10,2) CHECK (amount_due >= 0),
    status VARCHAR(20) DEFAULT 'Unpaid',
    FOREIGN KEY (meter_id) REFERENCES Meter(meter_id),
    FOREIGN KEY (tariff_id) REFERENCES Tariff(tariff_id)
);

-- Payment Table
CREATE TABLE Payment (
    payment_id INT PRIMARY KEY,
    bill_id INT NOT NULL UNIQUE,
    payment_date DATE,
    amount_paid DECIMAL(10,2) CHECK (amount_paid >= 0),
    payment_method VARCHAR(20),
    FOREIGN KEY (bill_id) REFERENCES Bill(bill_id)
);

-- Technician Table
CREATE TABLE Technician (
    technician_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_number VARCHAR(15),
    area_of_operation VARCHAR(50),
    role VARCHAR(50)
);

-- Complaint Table
CREATE TABLE Complaint (
    complaint_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    technician_id INT,
    description VARCHAR(255),
    date_reported DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (technician_id) REFERENCES Technician(technician_id)
);

