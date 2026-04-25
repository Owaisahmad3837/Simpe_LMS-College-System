from flask import Flask, redirect, render_template, request, session
from database import get_conn
import os
import config
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['UPLOAD_FOLDER'] = config.get_upload_folder()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_conn()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cur.fetchone()

        if user:
            session['user_id'] = user[0]
            session['role'] = user[3]

            if user[3] == 'principal':
                return redirect('/principal')
            else:
                return redirect('/student')

    return render_template('login.html')


@app.route('/principal')
def principal_dashboard():
    if session.get('role') != 'principal':
        return "Access Denied"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    return render_template('principal_dashboard.html', students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if session.get("role") != "principal":
        return "Access Denied"

    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]
        username = request.form["username"]
        password = request.form["password"]
        image = request.files["image"]

        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        conn = get_conn()
        cur = conn.cursor()

        # 1️⃣ Create user (student login)
        cur.execute("""
            INSERT INTO users (username, password, role)
            VALUES (%s, %s, 'student') RETURNING id
        """, (username, password))

        user_id = cur.fetchone()[0]

        # 2️⃣ Link student with user
        cur.execute("""
            INSERT INTO students (user_id, name, contact, image)
            VALUES (%s, %s, %s, %s)
        """, (user_id, name, contact, filename))

        conn.commit()

        return redirect("/principal")

    return render_template("add_student.html")



@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    if session.get("role") != "principal":
        return "Access Denied"

    conn = get_conn()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        contact = request.form["contact"]

        cur.execute("""
            UPDATE students
            SET name=%s, contact=%s
            WHERE student_id=%s
        """, (name, contact, id))

        conn.commit()
        return redirect("/principal")

    cur.execute("SELECT * FROM students WHERE student_id=%s", (id,))
    student = cur.fetchone()

    return render_template("edit_student.html", student=student)


@app.route("/delete/<int:id>")
def delete_student(id):
    if session.get("role") != "principal":
        return "Access Denied"

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE student_id=%s", (id,))
    conn.commit()

    return redirect("/principal")

@app.route("/student")
def student_dashboard():
    if session.get("role") != "student":
        return "Access Denied"

    user_id = session["user_id"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE user_id=%s", (user_id,))
    student = cur.fetchone()

    return render_template("student_dashboard.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)
