#coding: UTF-8
import csv
u20_woman = list()
with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20":
            u20_woman.append(titanic[4])
            survived_names = titanic[2]

    for i, l in enumerate(u20_woman):
        print("%s,%s" % (survived_names,l))

