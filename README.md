📚 Library Management System (Python + MySQL)

A command-line based Library Management System developed using Python and MySQL.
This project demonstrates database connectivity, SQL operations, and structured backend logic.

📌 Project Description

The Library Management System allows users to manage book records efficiently using a MySQL database.

Users can:

➕ Add new books

📖 View available books

📥 Borrow books

📤 Return books

🔄 Automatically update book availability

This project showcases practical implementation of CRUD operations and database integration using Python.

🛠️ Technologies Used

Python

MySQL

SQL (CRUD Operations)

mysql-connector-python

🗂️ Database Schema

Database Name: librarydb
Table Name: books

CREATE TABLE books (
    bookid INT PRIMARY KEY,
    booktitle VARCHAR(255) NOT NULL,
    authorname VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'available'
);

⚙️ Features
1️⃣ Add Book

Inserts book details into the database

Sets default status as "available"

2️⃣ Show Books

Displays all books stored in the database

Shows current availability status

3️⃣ Borrow Book

Checks if the book exists

Updates status to "borrowed" if available

4️⃣ Return Book

Verifies if book was borrowed

Updates status back to "available"

💡 Key Concepts Demonstrated

Database Connectivity in Python

SQL Queries (SELECT, INSERT, UPDATE)

Data Validation & Conditional Logic

Exception Handling

Backend Data Management

🔧 Installation & Setup
Step 1: Install MySQL

Make sure MySQL is installed and running.

Step 2: Create Database
CREATE DATABASE librarydb;
USE librarydb;

Step 3: Create Table
CREATE TABLE books (
    bookid INT PRIMARY KEY,
    booktitle VARCHAR(255),
    authorname VARCHAR(255),
    status VARCHAR(50)
);

Step 4: Install Required Package
pip install mysql-connector-python

Step 5: Update MySQL Credentials

Edit the Python file and update:

user="root"
password="your_password"

Step 6: Run the Program
python library.py

📊 Why This Project is Important

This project demonstrates core backend and database handling skills required for:

Data Analyst

Business Analyst

Database Administrator (Beginner Level)

It shows understanding of structured data storage, SQL operations, and real-world data management.

🚀 Future Improvements

Add user login system

Implement due date & fine calculation

Build Power BI dashboard for reporting

Convert to web application using Flask

Add data analytics insights

👤 Author

Santhosh M K
Aspiring Data Analyst | Python | SQL | Power BI

Passionate about working with data and building data-driven solutions.
