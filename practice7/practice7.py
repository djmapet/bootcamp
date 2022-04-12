# coding: UTF-8
#Pclassの1,2,3の数を数える
#生存と生死とsurevive,pclass,name,sex,ageをリストに取れるように

import csv
passenger_list = list()

with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        try:
            age = float(titanic[4])
        except ValueError:
            continue

        pclass = titanic[1]
        name = titanic[2]
        sex = titanic[3]
        passenger = (pclass, name, sex, age)
