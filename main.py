import sqlite3
import os
import databasefunctions
from databasefunctions import *

dbname = "gemsdb.db"
selectsorgu="SELECT * FROM mibfile WHERE id>0"
deletesorgu="DELETE FROM mibfile WHERE id>10 "
updatesorgu="UPDATE mibfile set loaded='NOK' where id=10"

con = DatabaseConnection(dbname)
DatabaseConnection.table_insert(con,'deneme','OK','log','test','deneme','deneme')
DatabaseConnection.table_delete(con,deletesorgu)
DatabaseConnection.table_delete(con,updatesorgu)
DatabaseConnection.table_select(con,selectsorgu)

con.connection_close()

if __name__ == '__main__':
    print("Closing  program..")
