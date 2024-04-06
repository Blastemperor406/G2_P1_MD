import psycopg2 
import uuid

class Database:

    def __init__(self,host:str="localhost",port:str="5432",user:str="root",passwd:str="password",dbname:str="Products") -> None:
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
            result=cursor.execute("CREATE TABLE IF NOT EXISTS Products(ID uuid,NAME varchar(40) NOT NULL UNIQUE ,DESCRIPTION varchar(600)NOT NULL,PRODUCT_WEBSITE varchar(400) NOT NULL)")
            self.conn.commit()
        
        except Exception as e:
            print("Could not create table ",e)
    
        cursor.close()

    def insert_products(self,products:list):
        cursor=self.conn.cursor()

        for i in products:
            try: 
                result=cursor.execute("INSERT INTO Products (ID,NAME,DESCRIPTION,PRODUCT_WEBSITE) VALUES (%s,%s,%s,%s)",(str(uuid.uuid4()),i["Name"],i["Description"],i["Website"]))
                print(result)
            except Exception as e:
                print("Could not insert {}".format(i),e)

        self.conn.commit()
        cursor.close()    


if __name__=="__main__":
    print("Starting")
    database=Database()
    