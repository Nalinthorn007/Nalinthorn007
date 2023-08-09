import pymysql

# Connect to the database
def connectdb():
    try:
        # Establish the database connection
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pythondb',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection 
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None  
