# coding: UTF-8
import csv
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
