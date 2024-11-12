from flask import Flask, request, render_template, redirect
import mysql.connector as mysql

app = Flask(__name__)

# MySQL Connection
db = mysql.connect(host="localhost", user="root", password="Tejas@84", database="student_db")
cursor = db.cursor()

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Insert Data
@app.route('/insert', methods=['POST'])
def insert():
    roll_no = request.form['roll_no']
    name = request.form['name']
    marks = request.form['marks']
    
    query = "INSERT INTO students (RollNo, Name, Marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (roll_no, name, marks))
    db.commit()
    return redirect('/')

# Update Data
@app.route('/update', methods=['POST'])
def update():
    roll_no = request.form['roll_no']
    attribute = request.form['attribute']
    value = request.form['value']
    
    query = f"UPDATE students SET {attribute} = %s WHERE RollNo = %s"
    cursor.execute(query, (value, roll_no))
    db.commit()
    return redirect('/')

# Delete Data
@app.route('/delete', methods=['POST'])
def delete():
    roll_no = request.form['roll_no']
    query = "DELETE FROM students WHERE RollNo = %s"
    cursor.execute(query, (roll_no,))
    db.commit()
    return redirect('/')

# Show Data
@app.route('/show', methods=['GET'])
def show():
    option = request.args.get('option')
    roll_no = request.args.get('roll_no', None)
    
    if option == "all":
        cursor.execute("SELECT * FROM students")
    else:
        cursor.execute("SELECT * FROM students WHERE RollNo = %s", (roll_no,))
    
    data = cursor.fetchall()
    return render_template('show.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
