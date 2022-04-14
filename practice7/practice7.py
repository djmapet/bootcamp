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

        survived = titanic[0]
        pclass = titanic[1]
        name = titanic[2]
        sex = titanic[3]
        passenger = (survived,pclass, name, sex, age)
        passenger_list.append(passenger)

pclass1_list = list(filter(lambda x: x[0] == '1' and x[1] == '1' ,
                    passenger_list))
pclass2_list = list(filter(lambda x: x[0] == '1' and x[1] == '2',
                    passenger_list))
pclass3_list = list(filter(lambda x: x[1] == '3' and x[3] == "female" and x[4] >= 30,
                    passenger_list))
pclass1_cnt = len(pclass1_list)
pclass2_cnt = len(pclass2_list)
pclass3_cnt = len(pclass3_list)


print("1等級の乗客は%d名です" % pclass1_cnt)
print("2等級の乗客は%d名です" % pclass2_cnt)
#print("3等級の乗客は%d名です" % pclass3_cnt)
print("3等級で30歳以上の女性は%d名です" % pclass3_cnt)
