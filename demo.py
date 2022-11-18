import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="tareqqazzaz",
                                  password="tareqqazzaz",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    # drop any existing todos table
    cursor.execute("DROP TABLE IF EXISTS todos;")

    # (re)create the todos table
    # (note: triple quotes allow multiline text in python)
    cursor.execute("""
    CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
    );
    """)
    # Fetch result
    record = cursor.fetchone() # fetchone() fetchmany(2) 
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

"""
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

"""
