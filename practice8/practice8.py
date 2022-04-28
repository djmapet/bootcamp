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
gold_tennis_player = list(filter(lambda x: x[0] == 'Gold' and (x[1] == 'F' or x[1] == 'M') ,tennis_player_list))
gold_list_m = list(filter(lambda x: x[1] =='M' ,gold_tennis_player))
gold_list_f = list(filter(lambda x: x[1] =='F' ,gold_tennis_player))
"""最年少と最高齢を出したい"""
m_gold_young = list(map(lambda x: (x[3],x[2]),gold_list_m))
(m_age_young,m_name_young) = min(m_gold_young)
m_gold_old = list(map(lambda x: (x[3],x[2]),gold_list_m))
(m_age_old,m_name_old) = max(m_gold_old)
f_gold_young = list(map(lambda x: (x[3],x[2]),gold_list_f))
(f_age_young,f_name_young) = min(f_gold_young)
f_gold_old = list(map(lambda x: (x[3],x[2]),gold_list_f))
(f_age_old,f_name_old) = max(f_gold_old)

print("男性の最年少で金メダルは%s歳の%sです" %(m_age_young,m_name_young))
print("男性の最高齢で金メダルは%s歳の%sです" %(m_age_old,m_name_old))
print("女性の最年少で金メダルは%s歳の%sです" %(f_age_young,f_name_young))
print("女性の最高齢で金メダルは%s歳の%sです" %(f_age_old,f_name_old))

"""平均年齢"""
age_list = list(map(lambda x: x[3],gold_tennis_player))
age_sum = sum(age_list)
age_cnt = len(age_list)
age_ave = age_sum / age_cnt
print("金メダル取得者の平均年齢は%1.1f歳です" %age_ave)

"""一番メダルを取ったプレーヤー"""
medalist = list(filter(lambda x: (x[3]== "Gold" or x[3] == 'Silver' or x[3] == 'Bronze') ,player_list))
medalist_name_list = list(map(lambda x:x[4],medalist))
most_medalist = collections.Counter(medalist_name_list)
m_f_got_medal = most_medalist.most_common()
(name1,cnt_medal) = m_f_got_medal[0]

m_medal_list = list(filter(lambda x: (x[3]== "Gold" or x[3] == 'Silver' or x[3] == 'Bronze') and x[0] == 'M', player_list))
m_medalist_name_list = list(map(lambda x: x[4] ,m_medal_list))
m_some_got_medal = collections.Counter(m_medalist_name_list)
m_got_medal_most = m_some_got_medal.most_common()
(m_name,m_cnt_medal) = m_got_medal_most[0]

f_medal_list = list(filter(lambda x: (x[3]== "Gold" or x[3] == 'Silver' or x[3] == 'Bronze') and x[0] == 'F', player_list))
f_medalist_name_list = list(map(lambda x: x[4],f_medal_list))
f_some_got_medal = collections.Counter(f_medalist_name_list)
f_got_medal_most = f_some_got_medal.most_common()
(f_name,f_cnt_medal) = f_got_medal_most[0]

print("メダルを多く取ってる選手は%sの%d個です"%(name1,cnt_medal))
print("男性でメダルを多く取ってる選手は%sの%d個です"%(m_name,m_cnt_medal))
print("女性でメダルを多く取ってる選手は%sの%d個です"%(f_name,f_cnt_medal))
