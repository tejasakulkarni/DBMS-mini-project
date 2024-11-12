import mysql.connector as mysql
import pandas as pd

# Step 1: Connect to MySQL database
db = mysql.connect(
    host="localhost",
    user="root", 
    password="Tejas@84", # Replace with your MySQL root password
    database="student"
)
cursor = db.cursor()
# Step 2: Read the Excel file into a DataFrame
data = pd.read_excel(r"C:\IMP Documents\Tejas Books and study Material\TY\Sem 5\DBMS\Project\Data.xlsx")
# Step 3: Insert DataFrame rows into MySQL table
for _, row in data.iterrows():
    query = "INSERT INTO students (RollNo, Name, Marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (int(row['RollNo']), row['Name'], int(row['Marks'])))
# Commit the transaction and close the connection
db.commit()
db.close()
print("Data loaded successfully!")
