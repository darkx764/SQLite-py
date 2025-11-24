from classes.cli_prompter import menu
import sqlite3

class SQLiteDB:
    """ Simple sqlite connection manager class """

    def __init__(self, dbname):
        self.connection = None
        self.cursor = None
        self.menu = menu() # create menu instance
        self.dbname = f"databases/{dbname}" # db path name
        self.connect() # connect db

    def connect(self):
        """ make sqlite connection """
        try:
            # create connection 
            self.connection = sqlite3.connect(self.dbname)
            # cursor function for execute SQL statement
            self.cursor = self.connection.cursor()
        except Exception as e:
            print('exception error:', e)
        finally:
            pass

    def tables(self):
        """ List all available table in database """
        # checking if cursor instance not available
        if self.cursor is None:
            print("Error: Not connected to any database.")
            return []
        # sql query to get all data
        res = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        # fetch all tables
        tables = res.fetchall()
        return [table[0] for table in tables]

    def show(self):
        """ show menu with table choices """
        try:
            # question to put in choices with list of DB name
            return self.menu.select(f"Choose databases in {self.dbname}", self.tables())
        
        except Exception as e:
            print('exception error:', e)
            self.disconnect()
        
    def disconnect(self):
        """ close sqlite connection """
        self.connection.close()