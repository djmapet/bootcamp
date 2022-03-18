import csv
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for oscar in reader:
        if oscar[1] == "1991":
            oscar_1991 = oscar[3]
        if oscar[2] <= "30":
            for u_30 in oscar[2]:
                oscar_u30 = u_30


    print("1991年のオスカー女優は%sです"
          %(oscar_1991))

    print("30歳以下のオスカー女優は%s名です"
          %(oscar_u30))


