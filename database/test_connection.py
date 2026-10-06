from connection import get_connection, close_connection


connection = get_connection()

if connection:
    print("MySQL connection successful!")

    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE();")

    result = cursor.fetchone()

    print("Connected database:", result[0])

    cursor.close()
    close_connection(connection)

else:
    print("MySQL connection failed.")