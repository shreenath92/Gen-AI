import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()


# Create the table (if it doesn't already exist)
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT1 (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT1 VALUES ('Shreenath', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT1 VALUES ('John', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT1 VALUES ('Mukesh', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT1 VALUES ('Jacob', 'DEVOPS', 'A', 50)")
cursor.execute("INSERT INTO STUDENT1 VALUES ('Dipesh', 'DEVOPS', 'A', 35)")

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT1")
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()

# Close the connection
connection.close()
