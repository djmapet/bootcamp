# coding: UTF-8
import csv
import sqlite3

con = sqlite3.connect("keikyu.db")
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS stations(st, id)"
cur.execute(query)
with open("station_table.csv", "r") as open_text:
    reader = csv.reader(open_text, doublequote=True, lineterminator="\r\n",
                        quotechar='"', skipinitialspace=True)
    header = next(reader)

    rows = list()
    for row in reader:
        rows.append(row)

    cur.executemany(
        "INSERT INTO stations(st, id) \
        VALUES (?,?)", rows)
    con.commit()
