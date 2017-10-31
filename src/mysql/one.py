import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(
    "bdm275410299.my3w.com","bdm275410299","tanwenbin","bdm275410299_db")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("show table status")

# 使用 fetchone() 方法获取一条数据
res=cursor.fetchall()
for row in res:
    print(row)


# 关闭数据库连接
db.close()