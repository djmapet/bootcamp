#coding: UTF-8
import csv
u20_woman = list()
ave_count = list()
#total = 0
with open("titanic.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for titanic in reader:
        if titanic[4] <= "20" and titanic[3] == "female" and titanic[0] =="1":
            n = (titanic[4],titanic[2])
            u20_woman.append(n)

        if titanic[0] == "1":
            #total += 1
            #life = (sum(titanic[4])/ave_count)
            #total = ((titanic[4])+total)/int(titanic[4])
            ave_count.append(titanic[4])


    for l in u20_woman:
        age = l[0]
        name = l[1]
        print("%s,%s" % (age,name))

    for total,count in ave_count:
        #ave_count = ave[1]
        #ave_total = ave[0]
        age = ((int(total) + 1) / (int(count)))
        print("%s" % age)





