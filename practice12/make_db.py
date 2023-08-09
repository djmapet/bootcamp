# coding: UTF-8
import csv
import sqlite3

with open("ECサンプルデータ - sales.csv", "r") as open_text :
    render = csv.reader(open_text, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"',
                    skipinitialspace=True)
    header = next(render)

element = ",".join(header)
element_cnt = len(header)

scheme = "sample("+element.replace('"','')+")"

l_element = list()
for n in header:
    l_element.append("?")
s_element = ",".join(l_element)

con = sqlite3.connect("sample.db")
cur = con.cursor()
query = "CREATE TABLE IF NOT EXISTS "+scheme
cur.execute(query)
with open("ECサンプルデータ - sales.csv", "r") as open_text:
    reader = csv.reader(open_text, doublequote=True, lineterminator="\r\n",
                        quotechar='"', skipinitialspace=True)
    header = next(reader)

    rows = list()
    for row in reader:
        rows.append(row)

    n_query = "INSERT INTO "+scheme+" VALUES ("+s_element+")"
    print(n_query)
    cur.executemany(n_query, rows)
    con.commit()



