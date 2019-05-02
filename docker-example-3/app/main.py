import numpy as np
import pymysql.cursors

connection = pymysql.connect(host='db-service',
                            user='user',
                            password='password',
                            db='my_data',
                            cursorclass=pymysql.cursors.DictCursor)

try:
  with connection.cursor() as cursor:
    sql = "SELECT * FROM `goods`"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    sql = "SELECT `price` FROM `goods` WHERE `product`='Bread (Loaf)'"
    cursor.execute(sql)
    result = cursor.fetchone()
    sixLoaves = result['price'] * 6
    print("The price of six loaves of bread is: %s" % sixLoaves)
finally:
  connection.close()
