# coding: UTF-8
import csv
import collections

player_list = list()
with open("olympic_tennis.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n",
                        quotechar='"', skipinitialspace=True)
    header = next(reader)

    for tennis in reader:
        sex = tennis[2]
        medal = tennis[14]
        event = tennis[13]
        noc = tennis[7]
        player = (sex, noc, event, medal)
        player_list.append(player)

list_noc_medal = list(map(lambda x: (x[1], x[3],x[0],x[2]), player_list))
list_medalist = list(filter(lambda x: (x[1] == 'Gold' or x[1] == 'Silver' or x[1] == 'Bronze') and x[2] == 'M' and x[3] == "Tennis Men's Singles", list_noc_medal))
noc_count = collections.Counter(list(map(lambda x: x[0], list_medalist)))
noc_count_most = noc_count.most_common()
c_sorted = sorted(noc_count_most,key=lambda x: x[1],reverse=True)
(noc, medals) = c_sorted[0]
print("メダルを多く取ってる国は%sで%dです"%(noc, medals))
