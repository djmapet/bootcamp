#coding: UTF-8
import collections
import csv
u30 = 0
u30_list = list()
count = 0
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for oscar in reader:
        if oscar[1] == "1991":
            oscar_1991 = oscar[3]
        if oscar[2] <= "30":
            u30 += 1
            u30_list.append(oscar[3])







    print("1991年のオスカー女優は%sです"
          %(oscar_1991))
    print("30歳以下のオスカー女優は%s名です"
          %(u30))

    print("30歳以下のオスカー女優は以下の通りです")
    for l in u30_list:
        count +=1
        names = l

        print("{0:d}".format(count),"{0:s}".format(names))


