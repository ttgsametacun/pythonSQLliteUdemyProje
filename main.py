# This is a sample Python script.
import sqlite3
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

con = sqlite3.connect("gems2.db")
cursor = con.cursor()


def database_table_creat():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS mibfile (id  INTEGER PRIMARY KEY AUTOINCREMENT,imports  varchar(2000),loaded varchar(2000),log varchar(2000), name varchar(2000), path varchar(2000), uploadtime DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')) , filename varchar(2000)) ")


def table_insert():
    cursor.execute(
        "INSERT INTO mibfile  (imports,loaded,log,name,path,filename) values ('deneme','OK','log','test','deneme','deneme')")
    con.commit()


def table_select():
    cursor.execute("SELECT * FROM mibfile where id>0")
    data = cursor.fetchall()
    for row in data:
        print(row)

def table_update():
    cursor.execute("Update mibfile set filename=?,log=? where id=1",('mibfile1','Error'))
    con.commit()

def table_delete(rownum):
    cursor.execute("delete from mibfile where id<? ",(rownum,))
    con.commit()


database_table_creat()
table_insert()
table_select()
table_update()
table_delete(50)
con.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Database connection Succes..")
