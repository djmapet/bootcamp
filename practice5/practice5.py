#coding: UTF-8
import csv
u20_woman = list()
age_list = list()
ave = list()
total_female_age = 0
total_male_age = 0
female_count = 0
male_count = 0
max_age = 0
minimu_age = 1000


with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] == "1":
            n = (titanic[4],titanic[2])
            u20_woman.append(n)

        if titanic[0] == "1":
            try:
                age = int(titanic[4])
                name = (titanic[2])
                age_name = (age,name)
                age_list.append(age_name)

            except ValueError:
                continue


            if titanic[3] =="female":
                total_female_age += age
                female_count += 1

            if titanic[3] == "male":
                total_male_age += age
                male_count += 1

            if age >= max_age :
                max_age = age


            if age <= minimu_age:
                minimu_age = age



female_ave = total_female_age/female_count
male_ave = total_male_age/male_count
for l in u20_woman:
    age = l[0]
    name = l[1]
    print("%s,%s" % (age, name))

a = min(age_list)
b = max(age_list)
print('女性生存者の平均年齢は%d歳です' %female_ave )
print('男性生存者の平均年齢は%d歳です' %male_ave )
print('生存者の最高年齢は%d歳です'%max_age)
print('生存者の最小年齢は%d歳です'%minimu_age)

print('生存者の最小年齢は%sの%d歳です' %(a[1],a[0]))
print('生存者の最高年齢は%sの%d歳です' %(b[1],b[0]))
