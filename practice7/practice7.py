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

p1female = list(filter(lambda x: x[1] == '1' and x[3] == "female", passenger_list))
age_sum = sum(list(map(lambda x: x[4], p1female)))
female_cnt = len(list(map(lambda x: x[4], p1female)))
female_ave = age_sum/female_cnt
p1male = list(filter(lambda x: x[1] == '1' and x[3] == "male", passenger_list))
age_sum = sum(list(map(lambda x: x[4], p1male)))
male_cnt = len(list(map(lambda x: x[4], p1male)))
male_ave = age_sum/male_cnt
print("１等の平均年齢は、女性が%1.1f歳で男性は%1.1f歳です" %(female_ave, male_ave))

p1 = list(filter(lambda x: x[1] == '1', passenger_list))
p1_sum = sum(list(map(lambda x: x[5], p1)))
p1_cnt = len(p1)
p1_fare = p1_sum/p1_cnt
p2 = list(filter(lambda x: x[1] == '2', passenger_list))
p2_sum = sum(list(map(lambda x: x[5], p2)))
p2_cnt = len(p2)
p2_fare = p2_sum/p2_cnt
p3 = list(filter(lambda x: x[1] == '3', passenger_list))
p3_sum = sum(list(map(lambda x: x[5], p3)))
p3_cnt = len(p3)
p3_fare = p3_sum/p3_cnt
print("それぞれのfareの平均は、1等が%1.1f£、2等は%1.1f£、3等は%1.1f£です" %(p1_fare, p2_fare, p3_fare))

p1_alive = len(list(filter(lambda x: x[0] == '1', p1)))
p1_alive_ave = p1_alive/p1_cnt*100
print("1等客の生存率は%1.1fです" %p1_alive_ave)
p2_alive = len(list(filter(lambda x: x[0] == '1', p2)))
p2_alive_ave = p2_alive/p2_cnt*100
print("2等客の生存率は%1.1fです" %p2_alive_ave)
p3_alive = len(list(filter(lambda x: x[0] == '1', p3)))
p3_alive_ave = p3_alive/p3_cnt*100
print("3等客の生存率は%1.1fです" %p3_alive_ave)