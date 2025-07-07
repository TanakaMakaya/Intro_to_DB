# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",       # Change this if your server is remote
            user="your_username",   # Replace with your MySQL username
            password="your_password" # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # Attempt to create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
    
    finally:
        # Always close the connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
