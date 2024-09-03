import sqlite3

connection = sqlite3.connect("test.db")

name = str(input("What is your name?\n"))
age = int(input("What is your age?\n"))

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, age INTEGER)")
cursor.execute(f"INSERT INTO example VALUES (1, '{name}', {age})")
connection.commit()

cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()