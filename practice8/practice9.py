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
