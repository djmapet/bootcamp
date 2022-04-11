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
        if titanic[0] == "1" or titanic[0] == "0":
            try:
                age = int(titanic[4])
                name = (titanic[2])
                age_name = (age, name)
                age_list.append(age_name)
            except ValueError:
                continue
            if titanic[3] == "male":
                try:
                    male_age = int(titanic[4])
                    male_name = (titanic[2])
                    male_age_name = (male_age, male_name)
                    male_list.append(male_age_name)
                except ValueError:
                    continue
            if titanic[3] == "female" :
                try:
                    female_age = int(titanic[4])
                    female_name = (titanic[2])
                    female_age_name = (female_age,female_name)
                    female_list.append(female_age_name)
                except ValueError:
                    continue

#male_list.sort()
#female_list.sort()

oldest_male_age = max(male_list)
(male_age) = oldest_male_age
oldest_female_age = max(female_list)
(age2) = oldest_female_age

print("男性乗客の最高年齢は%d歳です" % oldest_male_age[0])
print("女性乗客の最高年齢は%d歳です" % oldest_female_age[0])

n_gender = 0
n_gender_cnt = 0
print("乗客は性別で%sの方が%d人多く乗っていました" % (n_gender, n_gender_cnt))

total_pass_cnt = 0
dead_cnt = 0
print("乗客数は%dで、うち死亡したのは%d人です" % (total_pass_cnt, dead_cnt))

