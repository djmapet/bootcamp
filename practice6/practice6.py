# coding: UTF-8
import csv
age_list = list()
male_list = list()
female_list = list()
oldest_male_age = 0
oldest_female_age = 0
dead_cnt = 0
live_cnt = 0
error_cnt = 0

with open("titanic.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        try:
            age = float(titanic[4])
        except ValueError:
            error_cnt += 1
            continue

        if titanic[3] == "male":
            male_list.append(age)
        if titanic[3] == "female":
            female_list.append(age)
        if titanic[0] == "0":
            dead_cnt += 1
        if titanic[0] == "1":
            live_cnt += 1

oldest_male_age = max(male_list)
oldest_female_age = max(female_list)

print("男性乗客の最高年齢は%1.1f歳です" % oldest_male_age)
print("女性乗客の最高年齢は%1.1f歳です" % oldest_female_age)

n_gender = 0
n_gender_cnt = 0
male_cnt = len(male_list)
female_cnt = len(female_list)
if male_cnt > female_cnt:
    n_gender = "男性"
    n_gender_cnt = male_cnt - female_cnt
if female_cnt > male_cnt:
    n_gender = "女性"
    n_gender_cnt = female_cnt - male_cnt
print("男性が%d、女性が%d" % (male_cnt, female_cnt))

print("乗客は性別で%sの方が%d人多く乗っていました" % (n_gender, n_gender_cnt))

total_pass_cnt = male_cnt + female_cnt
live_dead = dead_cnt + live_cnt

print("乗客数は%dで、うち死亡したのは%d人です" % (total_pass_cnt, dead_cnt))
print("生存者は%d人です" % live_cnt)
print("合計は%d人です" % live_dead)
print("エラーの数は%d人です" % error_cnt)