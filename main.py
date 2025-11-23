from classes.databases import databases 
from classes.menu import menu
import classes.sqlite as conn

# create DB instance
db = databases()

# get list of DB in folder 'databases'
list_db = db.list('databases')

# question to put in choices with list of DB name
q = {
        "type": "list",
        "message":"Choose your db",
        "choices": list_db
}

# create menu instance
menu = menu()
# execute DB menu
db_menu = menu.question(q)

# naming the selected DB path
sdb = f"databases/{db_menu[0]}"

# make connection into the DB
sql = conn.SQLiteDB()
# connect the selected DB
sql.connect(sdb)

# question with list of tables name
qt= {
    "type": "list",
    "message": f"Available tables in {db_menu[0]}",
    "choices": sql.list_tables()
}

#prompt choices question
t_menu = menu.question(qt)

#selected table
print(t_menu[0])

sql.disconnect








