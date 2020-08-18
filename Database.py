import sqlite3

try:
    Connection=sqlite3.connect("StudentDatabse.db")
except:
    print("Connection Error...")
Curcer=Connection.cursor()
try:
    Curcer.execute("CREATE TABLE StudentDetail (FirstName,LastName,EnrollmentNumber PRIMARY KEY,Email,City)")
    raise Exception
except:
    pass
