import csv
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    header = next(reader)
    print(header)

    for row in reader:
        print(row[1] =="1991" ,row[1], row[3])



