#coding: UTF-8
import csv
u20_woman = list()
ave = list()
total_age = 0
count = 0

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
            except ValueError:
                continue

            total_age += age
            count += 1
            ave = total_age/count





for l in u20_woman:
    age = l[0]
    name = l[1]
    print("%s,%s" % (age, name))

print('生存者の平均年齢は%d歳です' %ave)

