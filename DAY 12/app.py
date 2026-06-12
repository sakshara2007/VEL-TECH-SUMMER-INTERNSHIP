from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create Database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rollno TEXT,
        department TEXT,
        year TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT,
        address TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        rollno = request.form['rollno']
        department = request.form['department']
        year = request.form['year']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        address = request.form['address']

        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO students
        (name, rollno, department, year, email, phone, gender, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (name, rollno, department, year, email, phone, gender, address))

        conn.commit()
        conn.close()

        return redirect('/students')

    return render_template('register.html')


@app.route('/students')
def students():

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    print("DATABASE DATA =", data)

    conn.close()

    return render_template('students.html', students=data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)