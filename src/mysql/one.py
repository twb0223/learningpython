import MySQLdb

# 打开数据库连接
mysqldb = MySQLdb.connect(
    "bdm275410299.my3w.com", "bdm275410299", "tanwenbin", "bdm275410299_db")

cursor = mysqldb.cursor()

# 使用execute方法执行SQL语句
cursor.execute("Select * from t_girl limit 100 ")

res1=cursor.fetchone()
print(res1)

# 使用 fetchone() 方法获取一条数据
res = cursor.fetchall()
for row in res:
    print(row)

# 关闭数据库连接
mysqldb.close()


