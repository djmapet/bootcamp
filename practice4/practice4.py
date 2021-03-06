# coding: UTF-8
import csv
u30_list = list()
with open("oscar.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for oscar in reader:
        if oscar[1] == "1991":
            oscar_1991 = oscar[3]
        if oscar[2] <= "30":
            u30_list.append(oscar[3])
"""
    print("1991年のオスカー女優は%sです"
          %(oscar_1991))
    print("30歳以下のオスカー女優は%s名です"
          %(u30))

    print("30歳以下のオスカー女優は以下の通りです")
    for l in u30_list:
        count +=1
        names = l

        print("{0:d}".format(count),"{0:s}".format(names))
"""
print("1991年のオスカー女優は%sです" % oscar_1991)
print("30歳以下のオスカー女優は%d名です" % len(u30_list))
for i, l in enumerate(u30_list):
    print("%d.%s" % (i+1, l))
