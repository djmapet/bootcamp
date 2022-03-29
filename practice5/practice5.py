#coding: UTF-8
import csv
u20_woman = list()
ave = list()
total_female_age = 0
total_male_age = 0
female_count = 0
male_count = 0

with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] == "1":
            n = (titanic[4],titanic[2])
            u20_woman.append(n)

        if titanic[0] == "1" and titanic[3] =="female" and "male":
            try:
                female_age = int(titanic[4])
                male_age = int(titanic[4])
            except ValueError:
                continue

        if titanic[0] == "1" and titanic[3] =="female":
            total_female_age += female_age
            female_count += 1

        if titanic[0] == "1" and titanic[3] == "male":
            total_male_age += male_age
            male_count += 1

female_ave = total_female_age/female_count
male_ave = total_male_age/male_count
for l in u20_woman:
    age = l[0]
    name = l[1]
    print("%s,%s" % (age, name))


print('女性生存者の平均年齢は%d歳です' %female_ave )
print('男性生存者の平均年齢は%d歳です' %male_ave )

