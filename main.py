from classes.databases import databases
from classes.cli_prompter import menu
import classes.sqlite as conn

menu = menu() # init menu instance

def select_db():
    db = databases() # execute list databases menu
    s = db.show() # show list of db
    return s # return selected db

def main(db):
    while True:
        try:
            sql = conn.SQLiteDB(db) # execute connection on SQLite
            tables = sql.show() # show list tables

        except Exception as e:
            print(f"Exception occur in main file : {e}") # print error kalu jadi exception
            q = menu.confirm("An error occur. EXIT?") # confirmation message

            if q[0]:
                break

""" Execute the main function """  
sdb = select_db()
main(sdb)







