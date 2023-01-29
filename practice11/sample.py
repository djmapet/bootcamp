# coding: UTF-8
import csv
import sqlite3
n_list = list()
with open("ohtani_pitch_2022.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for data in reader:
        speed = float(data[2])
        if speed >= 80:
            n_list.append([data[1],speed])

for n in n_list:
    print("%s,%d" % (n[0],n[1]))

def get_speed_ave(speed_ave):
    con =sqlite3.connect('sample.db')
    cur = con.cursor()
    query = "select avg(release_speed) from sample desc"
    cur.execute(query)
    average = cur.fetchone()
    print("大谷の平均急速は%1.1f mlです") %(average)



if __name__ == '__main__':
    get_speed_ave()
    #for n2 in get_speed_ave():
     #   print("大谷選手の平均の球速は%1.1f mlです" % float(n2))







