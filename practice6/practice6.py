# coding: UTF-8
import csv
age_list = list()

with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[0] == "1":
            try:
                age = int(titanic[4])
                name = (titanic[2])
                age_name = (age, name)
                age_list.append(age_name)
            except ValueError:
                continue

oldest_male_age = 0
oldest_female_age = 0
print("男性乗客の最高年齢は%d歳です" % oldest_male_age)
print("女性乗客の最高年齢は%d歳です" % oldest_female_age)

n_gender = 0
n_gender_cnt = 0
print("乗客は性別で%sの方が%d人多く乗っていました" % (n_gender, n_gender_cnt))

total_pass_cnt = 0
dead_cnt = 0
print("乗客数は%dで、うち死亡したのは%d人です" % (total_pass_cnt, dead_cnt))
