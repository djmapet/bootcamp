# coding: UTF-8
#Pclassの1,2,3の数を数える
#生存と生死とsurevive,pclass,name,sex,ageをリストに取れるように

import csv
passenger_list = list()
male_cnt = 0
total_male_age = 0
female_cnt = 0
total_female_age = 0
with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        try:
            age = float(titanic[4])
            fare = float(titanic[7])
        except ValueError:
            continue

        survived = titanic[0]
        pclass = titanic[1]
        name = titanic[2]
        sex = titanic[3]
        passenger = (survived,pclass, name, sex, age, fare)
        passenger_list.append(passenger)

p1female = list(filter(lambda x: x[1] == '1' and x[3] == "female" , passenger_list))
