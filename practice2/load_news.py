#coding: UTF-8
data = dict()
with open("news.txt","r") as open_news:
    us_news = open_news.read()

print(us_news)

import re
result = re.sub(r"[^a-z]","",us_news)

for k in result:
    data[k] = result.count(k)


k_sorted = sorted(data.items(), key=lambda x:x[1], reverse=True)
print(k_sorted)
import re
found = re.compile(r'[a-z]+')



print("一番使われている文字は'%s'で%d個使われています" %
      (k_sorted[0][0],k_sorted[0][1] ))