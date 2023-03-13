from MysqlConnection.mysqldatabase import MySqlConnection
class CRUD(MySqlConnection):
    def __init__(self):
        pass
    def insertdata(self):
        data=(200,'mumbai',"java")
        sql="insert into hcl_batch5 values(%s,%s,%s);"""
        self.cursor.execute(sql,data)
        self.connect.commit()
        print("Record added Successfully")
    def selectrecord(self):
        sql="select * from hcl_batch5;"
        self.cursor.execute(sql)
        d=self.cursor.fetchall()
        for r in d:
            print(d)

obj=CRUD()

obj.Connect("localhost","root","Lava@2000","myhcl",3306)
obj.insertdata()
obj.selectrecord()