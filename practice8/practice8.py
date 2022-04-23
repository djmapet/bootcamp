# coding: UTF-8
import csv
import collections

player_list = list()
with open("olympic_tennis.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n",quotechar='"', skipinitialspace=True)
    header = next(reader)

    for tennis in reader:
        try:
            age = int(tennis[3])
        except ValueError:
            continue
        sex = tennis[2]
        medal = tennis[14]
        event = tennis[13]
        noc = tennis[7]
        name = tennis[1]
        player = (sex, noc, event, medal, name, age)
        player_list.append(player)

list_noc_medal = list(map(lambda x: (x[1], x[3],x[0],x[2]), player_list))
list_medalist = list(filter(lambda x: (x[1] == 'Gold' or x[1] == 'Silver' or x[1] == 'Bronze') and x[2] == 'M' and x[3] == "Tennis Men's Singles", list_noc_medal))
noc_count = collections.Counter(list(map(lambda x: x[0], list_medalist)))
noc_count_most = noc_count.most_common()
c_sorted = sorted(noc_count_most,key=lambda x: x[1],reverse=True)
(noc, medals) = c_sorted[0]
print("メダルを多く取ってる国は%sで%dです"%(noc, medals))

tennis_player_list = list(map(lambda x: (x[3],x[0],x[4],x[5]), player_list))
gold_tennis_player = list(filter(lambda x: x[0] == 'Gold' and (x[1] == 'F' or x[1] == 'M',x[3]) ,tennis_player_list))
gold_list_m = list(filter(lambda x: x[1] == 'M' ,gold_tennis_player))
gold_list_f = list(filter(lambda x: x[1] == 'F' ,gold_tennis_player))
gold_list_m_young = list(filter(lambda x: x[3] ,gold_list_m))
gold_list_m_young_sort = sorted(gold_list_m_young, key=lambda x:x[3] )
gold_list_m_old = max(list(filter(lambda x: x[3] ,gold_list_m)))
gold_list_f_young = min(list(filter(lambda x: x[3] ,gold_list_f)))
gold_list_f_old = max(list(filter(lambda x: x[3] ,gold_list_f)))

#print(gold_tennis_player)
print(gold_list_m_young_sort)
print(gold_list_m_old)
print(gold_list_f_young)
print(gold_list_f_old)