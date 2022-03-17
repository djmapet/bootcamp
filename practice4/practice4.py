import csv
with open("oscar.csv","r") as open_text:
    reader = csv.reader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                        skipinitialspace=True)
    reader = csv.DictReader(open_text,delimiter="\t",doublequote=True, lineterminator="\r\n",quotechar='"',
                            skipinitialspace=True)

    for line in reader:
        reader = [row for row in line]
        print(line)


