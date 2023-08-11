# coding: UTF-8

import csv
import sqlite3

n_list = list()
with open("sales.csv", "r"), open("items.csv"), open("users.csv") as open_text:
    reader = csv.reader(open_text, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

def sales_month():
    con = sqlite3.connect("practice12.db")
    cur = con.cursor()
    query = "select buy_date, count(buy_date) from sample group by buy_date"
    cur.execute(query)
    info = cur.fetchone()
    if info:
        return info[0]
    else:
        return None

if __name__ == "__main__":
    result_month = sales_month()
    print(result_month)
