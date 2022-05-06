# coding: UTF-8
import csv
import sqlite3

con = sqlite3.connect("tennis.db")
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS tennis(id,name,sex,age,height,weight,team,noc,games,\
        year,season,city,sport,event,medal)"
cur.execute(query)
with open("olympic_tennis.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n",
                        quotechar='"', skipinitialspace=True)
    header = next(reader)

    rows = list()
    for row in reader:
        try:
            age = int(row[3])
        except ValueError:
            age = None
        try:
            year = int(row[9])
        except ValueError:
            year = None
        row[3] = age
        row[9] = year
        rows.append(row)

    cur.executemany(
        "INSERT INTO tennis(id,name,sex,age,height,weight,team,noc,games,year,season,city,sport,event,medal) \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.commit()
