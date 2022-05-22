# coding: UTF-8
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

"メダルを一番多く取った国"
