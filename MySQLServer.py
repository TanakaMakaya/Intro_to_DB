# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
      
        connection = mysql.connector.connect(
            host="localhost",       
            user="your_username",   
            password="your_password" 
        )
        cursor = connection.cursor()

       
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
    
    finally:
      
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
