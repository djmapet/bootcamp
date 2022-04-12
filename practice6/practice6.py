# coding: UTF-8
import csv
age_list = list()
male_list = list()
female_list = list()
oldest_male_age = 0
oldest_female_age = 0

with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[3] == "male":
            try:
                age = int(titanic[4])
                male_list.append(age)
            except ValueError:
                continue
        if titanic[3] == "female":
            try:
                age = int(titanic[4])
                female_list.append(age)
            except ValueError:
                continue

#male_list.sort()
#female_list.sort()

(age) = max(male_list)
oldest_male_age = age
(age) = max(female_list)
oldest_female_age = age

print("男性乗客の最高年齢は%d歳です" % oldest_male_age)
print("女性乗客の最高年齢は%d歳です" % oldest_female_age)

n_gender = 0
n_gender_cnt = 0
print("乗客は性別で%sの方が%d人多く乗っていました" % (n_gender, n_gender_cnt))

total_pass_cnt = 0
dead_cnt = 0
print("乗客数は%dで、うち死亡したのは%d人です" % (total_pass_cnt, dead_cnt))