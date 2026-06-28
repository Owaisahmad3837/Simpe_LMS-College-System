
# Simple College LMS System 🎓

A simple Learning Management System (LMS) built with Python Flask that manages college users through different roles.

This project demonstrates a basic college management workflow where a Principal can manage users, including adding, updating, and deleting student and teacher records.

## Project Overview

The system has multiple user levels:

### Principal Level
- Login to admin panel
- Add new users
- Update user information
- Delete users
- Manage college users

### Teacher Level
- Teacher account management
- Access based on assigned role

### Student Level
- Student account management
- Access based on assigned role

## Features

✅ Role-based user management  
✅ Principal admin dashboard  
✅ Add users  
✅ Update users  
✅ Delete users  
✅ User authentication system  
✅ Database integration  
✅ File upload support  

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
├── config.py           # Application configuration
├── database.py         # Database connection
├── models.py           # Database models
│
├── templates/          # HTML pages
├── static/uploads/     # Uploaded files
├── utils/              # Utility functions
│
└── README.md

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

Install dependencies:

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

## Future Improvements

* Add student attendance system
* Add marks/grades management
* Add teacher dashboard
* Add email notifications
* Improve authentication security

## Author

**Owais Ahmad**

Software Engineer | Python Developer

```
