import pymysql 
import pymysql.cursors

conn = pymysql.connect(
   database="xcampos_todos",
   user='xcampos',
   password='221349988',
   host='10.100.33.60', 
   cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute("SELECT `Name`, `HeadOfState` FROM `country`")


results = cursor.fetchall()

from pprint import pprint as print 

print(results[0]["HeadOfState"])

for x in results :
    print(x['HeadOfState'])

