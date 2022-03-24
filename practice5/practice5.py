#coding: UTF-8
import csv
u20_woman = list()
with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] =="1":
            n = (titanic[4],titanic[2])
            u20_woman.append(n)


    for l in u20_woman:
        age = l[0]
        name = l[1]
        print("%s,%s" % (age,name))

