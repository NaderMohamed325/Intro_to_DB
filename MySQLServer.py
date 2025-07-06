import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='009988'
    )
    
    if mydb.is_connected():
        cursor = mydb.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
        # Close cursor
        cursor.close()

except mysql.connector.Error as e:
    print(f"Error: Failed to connect to MySQL server. {e}")

finally:
    # Close database connection
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed.")