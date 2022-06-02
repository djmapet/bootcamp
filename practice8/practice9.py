# coding: UTF-8
import collections
import sqlite3

con = sqlite3.connect("tennis.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

#query = "select name, medal from tennis where Medal = 'Gold' AND sex = 'M'"
#for i in cur.execute(query):
#	print("%s %s" % i)

query = "select max(age) as max_age from tennis where Medal = 'Gold' AND sex = 'M' "
cur.execute(query)
n = cur.fetchone()
print("メダルの個数は%s個です" % (n['max_age']))

query = "select count(medal) as sum_medal ,name as gold_name from tennis where medal = 'Gold' and sex = 'M' group by gold_name having sum_medal >=1 order by sum_medal desc "
cur.execute(query)
m = cur.fetchone()

most_gold_player_list = "select count(medal) as sum_medal_female ,name as gold_name_female from tennis where medal = 'Gold' and sex = 'F' group by gold_name_female having sum_medal_female >=4 order by sum_medal_female desc "
for female in cur.execute(most_gold_player_list):
    print("女性でメダルを多く取った人は%sの%s個です" % (female['gold_name_female'], female['sum_medal_female']))
    female = cur.fetchone()

most_silver_player_list = "select count(medal) as sum_medal_female2 ,name as silver_name_female from tennis where medal = 'Silver' and sex = 'F' group by silver_name_female having sum_medal_female2 >=2 order by sum_medal_female2 desc "
for female2 in cur.execute(most_silver_player_list):
    print("女性で銀メダルを多く取った人は%sの%s個です" % (female2['silver_name_female'], female2['sum_medal_female2']))
    female2 = cur.fetchone()


print("男性でメダルを多く取った人は%sの%s個です" % (m['gold_name'], m['sum_medal']))

"金メダルを一番多く取った国"
query = "select count(medal) as sum_medal from tennis where medal = 'Gold' group by noc order by sum_medal desc "
cur.execute(query)
s = cur.fetchone()
n = s['sum_medal']

query = "select count(medal) as count_medal_cnt , noc as country from tennis where medal = 'Gold' group by country having count_medal_cnt = %d order by count_medal_cnt desc" % n
l1 = list()
for result in cur.execute(query):
    s2 = (result['country'],result['count_medal_cnt'])
    l1.append(s2)

print("金メダルを一番多く取った国は%sで%sヵ国です" %(n,len(l1)))

print("国は以下の通りです。")
for x in l1:
    print("%s" %x[0])

"金銀銅のどちらかを多く取った国"
query = "select count(medal) as sum_medal2 from tennis where medal='Gold' or medal='Silver' or medal='Bronze' group by noc order by sum_medal2 desc"
cur.execute(query)
s3 = cur.fetchone()
n2 = s3['sum_medal2']

query = "select count(medal) as count_medal_cnt2 , noc as country2 from tennis where medal= 'Gold' or medal='Silver' or medal='Bronze' group by country2 having count_medal_cnt2 = %d order by count_medal_cnt2 " % n2
l2 = list()
for result in cur.execute(query):
    s3 = (result['country2'], result['count_medal_cnt2'])
    l2.append(s3)

print("金銀銅メダルを一番多く取った国は%sで%sヵ国です" %(n2,len(l2)))

print("国は以下の通りです")
for x2 in l2:
    print("%s" %x2[0])


"30歳以下が獲得した金メダルの数"
query = "select count(medal) as u30_medal from tennis where medal='Gold' group by age <= 30 order by u30_medal desc"
cur.execute(query)
s4 = cur.fetchone()
u30_medal = s4['u30_medal']

print('%s' %u30_medal)

"男性の30歳以下が獲得した金メダルの数"
query = "select count(medal) as u30_m_gold from tennis where age <= 30 and medal = 'Gold' group by sex = 'M' order by u30_m_gold desc"
cur.execute(query)
s5 = cur.fetchone()
u30_medal_cnt = s5['u30_m_gold']

query = "select name, sex, age, NOC, year,event, medal from tennis where sex = 'M' and medal = 'Gold' and age <= 30 order by year"
u30_gold_m_list = list()
cur.execute(query)
for m1 in cur.execute(query):
    u30_medal_m = (m1['name'],m1['sex'],m1['age'],m1['NOC'],m1['year'],m1['medal'],m1['event'])
    u30_gold_m_list.append(u30_medal_m)

print('男性の30歳以下が獲得した金メダルの数は%d個で、以下の通りになります'%u30_medal_cnt)
for i, result2 in enumerate(u30_gold_m_list):
    print(i+1, result2)

"男性が最小年齢で獲得した金メダル"