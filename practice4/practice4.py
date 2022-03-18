import csv
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)

    for row in reader:
        if row[1] == "1991":
            print("1991年のオスカー女優は%sです"
                  %(row[3]))
        elif row[2] <= "30":
            print("30歳以下のオスカー女優は%sです"
                  %(row[3]))







