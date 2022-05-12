# coding: UTF-8
import sqlite3

con = sqlite3.connect("tennis.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

#query = "select name, medal from tennis where Medal = 'Gold' AND sex = 'M'"
#for i in cur.execute(query):
#	print("%s %s" % i)

query = "select max(age) as max_age from tennis where Medal = 'Gold' AND sex = 'M' "
cur.execute(query)
n = cur.fetchone()
print("%d" % (n['max_age']))

query = "select count(medal) as sum_medal ,name as gold_name  from tennis where medal = 'Gold' group by gold_name order by sum_medal desc"
cur.execute(query)
m = cur.fetchone()
print("%s %d" % (m['gold_name'], m['sum_medal']))