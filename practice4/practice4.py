import csv
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)
    print(header)

    for row in reader:
        print(row)

row_oscar = int(input('1991年と入力してください'))
if row_oscar == 1991:
    print("{}年はKathy Batesがオスカー賞を受賞しました".format(row_oscar))



