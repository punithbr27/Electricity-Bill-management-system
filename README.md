# ⚡ Electricity Bill Management System

A modern web application built with Flask and MySQL for managing electricity billing operations, customer accounts, and payment processing.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0%2B-green)
![MySQL](https://img.shields.io/badge/mysql-8.0%2B-orange)

## 🌟 Features

### Customer Management
- Add and manage customer profiles
- Track customer contact information
- Maintain customer credit balance
- View customer listing and details

### Meter Management
- Register new meters for customers
- Track meter installation dates
- Monitor meter status (Active/Inactive)
- Record and manage meter readings

### Billing System
- Automated bill generation based on meter readings
- Support for different tariff plans
- Flexible due date management
- Track bill payment status
- Handle partial and excess payments
- Credit balance system for overpayments

### Payment Processing
- Record bill payments
- Multiple payment method support
- Handle partial payments
- Automatic credit balance management
- Payment history tracking

### Complaint Management
- Register customer complaints
- Assign technicians to complaints
- Track complaint status
- Maintain complaint history

### Dashboard & Reports
- Overview of total customers
- Active meters tracking
- Overdue bills monitoring
- Revenue analytics
- Daily payment tracking

## 🛠️ Technology Stack

- **Backend:** Python Flask
- **Database:** MySQL
- **Frontend:** HTML, Tailwind CSS
- **Charts:** Chart.js
- **Environment:** Python 3.x

## 📋 Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/punithbr27/Electricity-Bill-management-system.git
   cd Electricity-Bill-management-system
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - Create a MySQL database
   - Import the SQL files from the 'Related stuffs' folder in this order:
     1. Database creation.sql
     2. DDL for mam submission.sql
     3. DML for mam submission.sql

5. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   DB_HOST=localhost
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=Electricity_Bill_Management
   FLASK_SECRET_KEY=your_secret_key
   ```

6. **Run the Application**
   ```bash
   cd ebms_dashboard
   python app.py
   ```

## 💻 Usage

1. **Adding a New Customer**
   - Navigate to 'Add Customer'
   - Fill in customer details
   - Submit the form

2. **Setting Up a Meter**
   - Go to 'Add Meter'
   - Select the customer
   - Enter installation date and status
   - Submit the form

3. **Recording Meter Readings**
   - Access 'Add Reading'
   - Select the meter
   - Enter reading value and date
   - Submit the form

4. **Generating Bills**
   - Go to 'Generate Bill'
   - Select meter and tariff plan
   - Enter billing period
   - System automatically calculates the amount

5. **Processing Payments**
   - Navigate to 'Payment'
   - Select the bill
   - Enter payment details
   - System handles partial payments and credit balance

## 🔑 Key Features Explained

### Credit Balance System
- Handles overpayments automatically
- Maintains customer credit balance
- Applies credits to future bills
- Tracks all credit transactions

### Billing Logic
- Calculates consumption from meter readings
- Applies appropriate tariff rates
- Handles credit balance adjustments
- Manages payment status updates

### Payment Processing
- Supports full and partial payments
- Manages overpayments through credit system
- Updates bill status automatically
- Maintains payment history

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit changes
   ```bash
   git commit -m 'Add YourFeature'
   ```
4. Push to branch
   ```bash
   git push origin feature/YourFeature
   ```
5. Open pull request

## � Bug Reports

Report bugs by creating issues in the GitHub repository. Include:
- Bug description
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Punith BR
- GitHub: [@punithbr27](https://github.com/punithbr27)
- Project Link: [Electricity-Bill-management-system](https://github.com/punithbr27/Electricity-Bill-management-system)

## 🙏 Acknowledgments

- Database Lab project team
- Flask framework community
- MySQL community
- All contributors

---
Made with ❤️ by Punith BR
