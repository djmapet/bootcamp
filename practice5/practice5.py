# coding: UTF-8
import csv
u20_woman = list()
age_list = list()
count_survived = 0
ave = list()
total_female_age = 0
total_male_age = 0
female_count = 0
male_count = 0
max_age = 0
mini_age = 1000


with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] == "1":
            n = (titanic[4], titanic[2])
            u20_woman.append(n)

        if titanic[0] == "1":
            try:
                age = int(titanic[4])
                name = (titanic[2])
                age_name = (age, name)
                age_list.append(age_name)
            except ValueError:
                continue

            if titanic[3] == "female":
                total_female_age += age
                female_count += 1

            if titanic[3] == "male":
                total_male_age += age
                male_count += 1

            if age >= max_age:
                max_age = age

            if age <= mini_age:
                mini_age = age

female_ave = total_female_age/female_count
male_ave = total_male_age/male_count
for woman in u20_woman:
    age = woman[0]
    name = woman[1]
    print("%s,%s" % (age, name))

min_age_name = min(age_list)
(age1, name1) = min_age_name
max_age_name = max(age_list)
(age2, name2) = max_age_name

#list.sort(age_list)
(age3, name3) = age_list[-1]

print('女性生存者の平均年齢は%d歳です' % int(female_ave))
print('男性生存者の平均年齢は%d歳です' % int(male_ave))
print('生存者の最高年齢は%d歳です' % int(max_age))
print('生存者の最小年齢は%d歳です' % (int(mini_age)))
print('生存者の最小年齢は%sの%d歳です' % (name1, int(age1)))
print('生存者の最高年齢は%sの%d歳です' % (name2, int(age2)))
print("生存者は%d名です" % (len(age_list)))
print("最後の334人目の生存者は%sの%d歳です" % (name3, int(age3)))
