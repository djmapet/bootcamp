# coding: UTF-8
import csv
import sqlite3

con = sqlite3.connect("tennis.db")
cur = con.cursor()

query = "select name, medal from tennis where Medal = 'Gold' AND sex = 'M'"

for i in cur.execute(query):
	print("%s %s" % i)