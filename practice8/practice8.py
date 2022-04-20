# coding: UTF-8
import csv
import collections
player_list = list()
with open("olympic_tennis.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',skipinitialspace=True)
    header = next(reader)

    for tennis in reader:
        medal = tennis[14]
        noc = tennis[7]
        player = (noc, medal)
        player_list.append(player)


l = list(filter(lambda x: x[1] == 'Gold' or x[1] == 'Silver' or x[1] == 'Bronz', player_list))
c = collections.Counter(list(map(lambda x: x[0], l)))
print(c)