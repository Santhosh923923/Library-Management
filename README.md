Library Management System (Python + MySQL)

Project Description
A command-line based Library Management System developed using Python and MySQL. This project demonstrates database connectivity, SQL operations, and structured backend logic.

Users can:
- Add new books
- View available books
- Borrow books
- Return books
- Automatically update book availability
  
Technologies Used
- Python
- MySQL
- SQL (CRUD Operations)
- mysql-connector-python
  
Database Schema
Database Name: librarydb
Table Name: books

CREATE TABLE books (
    bookid INT PRIMARY KEY,
    booktitle VARCHAR(255) NOT NULL,
    authorname VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'available'
);
Features
1. Add Book – Inserts book details into the database with default status 'available'.
2. Show Books – Displays all books stored in the database.
3. Borrow Book – Updates status to 'borrowed' if available.
4. Return Book – Updates status back to 'available'.
   
Key Skills Demonstrated
- Database Connectivity in Python
- SQL Queries (SELECT, INSERT, UPDATE)
- Data Validation & Conditional Logic
- Exception Handling
- Backend Data Management

Installation & Setup
1. Install MySQL and ensure it is running.
2. Create database and table using provided SQL.
3. Install required package: pip install mysql-connector-python
4. Update MySQL credentials in the Python file.
5. Run: python library.py

Why This Project Matters
This project demonstrates practical database handling skills essential for Data Analyst roles. It shows structured data storage, SQL usage, and backend logic implementation.
Future Improvements
- Add user authentication
- Add due date & fine calculation
- Build Power BI dashboard
- Convert into Flask web application
- Add analytical reporting features

Author
Santhosh M K
Aspiring Data Analyst | Python | SQL | Power BI

