#coding: UTF-8
import csv
u20_woman = list()
ave_count = list()
count = 0
with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] =="1":
            n = (titanic[4],titanic[2])
            u20_woman.append(n)

        if titanic[0] == "1" and titanic[3] == "female" and titanic[3] == "male":
            count +=1
            life = (int(titanic[4])/sum(titanic[4]))
            ave_count.append(life)


    for l in u20_woman:
        age = l[0]
        name = l[1]
        print("%s,%s" % (age,name))

    for ave in ave_count:
        ave_age = ave[0]
        print("%s" % (ave_age))





