import psycopg2 
import uuid

class Database:

    def __init__(self,host:str="db",port:str="5432",user:str="root",passwd:str="password",dbname:str="Products") -> None:
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.dbname=dbname
        self.conn=None
        self.connect()
        self.create_table()
        
    def connect(self):
        if self.conn is not None:
            return "Connected to database"
        else:
            try:
                self.conn=psycopg2.connect("dbname='{}' user='{}' host='{}' password='{}'".format(self.dbname,self.user,self.host,self.passwd))
                
            except Exception as e:
                print("Failed to connect to database ",e)
                return

    def create_table(self):
        cursor=self.conn.cursor()
        try:
            result=cursor.execute("CREATE TABLE IF NOT EXISTS Products(NAME varchar(100) PRIMARY KEY NOT NULL ,DESCRIPTION varchar(1000)NOT NULL,PRODUCT_WEBSITE varchar(600))")
            self.conn.commit()
        
        except Exception as e:
            
            print("Could not create table ",e)
    
        cursor.close()

    def insert_products(self,products:dict):
            cursor=self.conn.cursor()

        
            try: 
                if "Website" in products:
                    result=cursor.execute("INSERT INTO Products (NAME,DESCRIPTION,PRODUCT_WEBSITE) VALUES (%s,%s,%s)",(products["Name"],products["Description"],products["Website"]))
                    self.conn.commit()
                    print(result)
                else:
                    result=cursor.execute("INSERT INTO Products (NAME,DESCRIPTION) VALUES (%s,%s)",(products["Name"],products["Description"]))
                    self.conn.commit()
                    print(result)

            except Exception as e:
                self.conn.rollback()
                print("Could not insert {}".format(products),e)

            self.conn.commit()
            cursor.close()    

    def get_products(self):
        pass
if __name__=="__main__":
    print("Starting")
    database=Database()
    