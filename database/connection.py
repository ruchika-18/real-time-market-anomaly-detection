import mysql.connector


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "market_analytics"
}


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print("Database connection error:", error)
        return None


def close_connection(connection):
    if connection is not None and connection.is_connected():
        connection.close()