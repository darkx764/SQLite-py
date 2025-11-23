import sqlite3

class SQLiteDB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, dbname):
        try:
            #create connection 
            self.connection = sqlite3.connect(dbname)
            #cursor function for execute SQL statement
            self.cursor = self.connection.cursor()
        except Exception as e:
            print('exception error:', e)
        finally:
            pass

    def list_tables(self):
        if self.cursor is None:
            print("Error: Not connected to any database.")
            return []
        #sql query to get all data
        res = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        #fetch all tables
        tables = res.fetchall()
        return [table[0] for table in tables]
        
    def disconnect(self):
        self.connection.close()