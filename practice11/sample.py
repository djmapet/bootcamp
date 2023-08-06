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


    for pitch in reader:
        pitch_type = float(pitch[23])
        if true :
            print(pitch_type)

for n in n_list:
    print("%s,%d" % (n[0],n[1]))

def get_speed_ave():
    con =sqlite3.connect('sample.db')
    cur = con.cursor()
    query = "select avg(pich) from sample desc"
    cur.execute(query)
    info = cur.fetchone()
    if info:
        return info[0]
    else:
        return None

def pitching_count():
    con = sqlite3.connect('sample.db')
    cur = con.cursor()
    query = 'select pitch_name, count(pitch_name) from sample group by pitch_name order by count(pitch_name) desc'
    cur.execute(query)
    info = cur.fetchone()
    for n in info:
        if n:
            return n
        else:
            return None


if __name__ == '__main__':
    ohtani_speed_ave_sth = get_speed_ave()
    print("大谷の球速平均スピードは%smphです"%ohtani_speed_ave_sth)

    ohtani_pitching_total = pitching_count()
    for n in ohtani_pitching_total:
        print(n)

    




