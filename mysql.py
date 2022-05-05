import pymysql
# 打开数据库连接
db = pymysql.connect(host="49.235.229.66", user="valuelink", password="myegoo3466", db="valuelink")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from ews_user")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()
