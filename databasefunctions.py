import  sqlite3
import os



class Connect():

        def __init__(self,dbname):
            self.dbname=dbname
            self.con=None
            self.connect_database(self.dbname)

        def connect(self,dbname):
            self.con = sqlite3.connect(self.dbname)
            self.cursor = self.con.cursor()

        def connect_database(self,dbname):
            if os.path.isfile(self.dbname):
                print('Database connection success')
                self.connect(self.dbname)
                return True
            else:
                print('Database connection error')
                self.connect(self.dbname)
                self.cursor.execute(
                    "CREATE TABLE IF NOT EXISTS mibfile "
                    "(id  INTEGER PRIMARY KEY AUTOINCREMENT,imports  varchar(2000),loaded varchar(2000),"
                    "log varchar(2000), name varchar(2000), path varchar(2000),"
                    "uploadtime DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')) , "
                    "filename varchar(2000)) ")
                return False

        def connection_close(self):
            if self.con is not None:
              self.con.close()


class DatabaseConnection(Connect):
        def __init__(self,dbname):
            super().__init__(dbname)


        def table_insert(self,imports,loaded,log,name,path,filename):
            self.imports = imports
            self.loaded=loaded
            self.log=log
            self.name=name
            self.path=path
            self.filename=filename
            sorgu="INSERT INTO mibfile  (imports,loaded,log,name,path,filename)" \
                  " values " \
                  "('{0}','{1}','{2}','{3}','{4}','{5}')".format(
              self.imports,self.loaded,self.log,self.name,self.path,self.filename
            )
            self.cursor.execute(sorgu)
            self.con.commit()


        def table_delete(self, sorgu):
            self.cursor.execute(sorgu)
            self.con.commit()

        def table_update(self, sorgu):
            self.cursor.execute(sorgu)
            self.con.commit()

        def table_select(self, sorgu):
            self.cursor.execute(sorgu)
            data = self.cursor.fetchall()
            for row in data:
                print(row)
















