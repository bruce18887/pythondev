# import pymysql
import sqlite3

dbObj = sqlite3.connect('zhuliquntestdb')#一般生成到当前路径下
print('数据库已打开')
CreateObj =dbObj.cursor()
#in sqlite3 the format to create a table is :
# CREATE TABLE database_name.table_name(
#    column1 datatype  PRIMARY KEY(one or more columns),
#    column2 datatype,
#    column3 datatype,
#    .....
#    columnN datatype,
# );
# CreateObj.execute('''
#                  CREATE TABLE COMPANY(
#                     ID            INT     PRIMARY KEY      ,
#                    NAME          TEXT                      NOT NULL,
#                    AGE            INT                      NOT NULL,
#                   SEX          BOOLEAN                     NOT NULL
#                   );
#                   ''')
# for var in range(0,1000):
#    CreateObj.execute("INSERT INTO COMPANY (ID,NAME,AGE,SEX) \
#                      VALUES ("+ str(var) +", 'Paul', 32,1)")
CreateObj.execute("INSERT INTO COMPANY")
# CreateObj.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
# CreateObj.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
# CreateObj.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
# print ("数据表创建成功")
# dbObj.commit()
# dbObj.close()
# c = conn.cursor()
# print ("数据库打开成功")

data = CreateObj.execute("SELECT * from COMPANY")

# print(data)#data直接打印显示为<sqlite3.Cursor object at 0x000002379C1C6A40> 一个对象
# CreateObj.execute("DELETE FROM COMPANY WHERE SEX < 1000")
for singlerowdata in data:
   print(singlerowdata)
dbObj.commit()
#
# print ("数据操作成功")
dbObj.close()