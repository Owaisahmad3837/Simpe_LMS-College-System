
# Simple College LMS System 🎓

A simple College Learning Management System (LMS) built with Python that helps manage college users and academic activities through different roles.

The system provides separate access levels for:

- Principal
- Teacher
- Student

## Project Overview

This project is designed to manage basic college operations with role-based access control.

The system allows the Principal to manage users, while teachers and students have their own functionalities.

## User Roles & Features

### 👨‍💼 Principal

- Secure login
- Add new users
- Update user information
- Delete users
- Manage college users

### 👨‍🏫 Teacher

- Teacher account access
- Manage teacher-related activities
- View assigned information

### 👨‍🎓 Student

- Student account access
- View student-related information

## Features

✅ Role-based login system  
✅ User management  
✅ Add / Update / Delete users  
✅ Database integration  
✅ File upload support  
✅ Simple college management workflow  

## Tech Stack

- Python
- Flask
- SQLite Database
- HTML
- CSS
- JavaScript

## Project Structure

```

Simple-College-System/

│
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── database.py         # Database connection
├── models.py           # Database models
│
├── templates/          # HTML pages
├── static/uploads/     # Uploaded files
├── utils/              # Helper functions
│
└── README.md

```

## System Workflow

```

User Login
|
↓
Check Role
|
┌─────────────┐
|             |
Principal   Teacher/Student
|
Manage Users

```

## Login Demo

Principal Account:

```

Username: admin
Password: 1234

````

## How to Run

Clone repository:

```bash
git clone https://github.com/Owaisahmad3837/Simpe-College-System.git
````

Go to project folder:

```bash
cd Simpe-College-System
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```



## Author

**Owais Ahmad**

Software Engineer | Python Developer

```
