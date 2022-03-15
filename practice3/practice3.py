#coding: UTF-8
data = dict()
with open("practice3_news.txt","r") as open_text:
    practice_news = open_text.read()

print(practice_news)

marge = practice_news.lower()

import re
result = re.findall(r"[a-zA-Z]+",practice_news)

for k in result:
    data[k] = result.count(k)


k_sorted = sorted(data.items(), key=lambda x:x[1], reverse=True)
print(k_sorted)
import re
found = re.compile(r'[^a-zA-Z]+')

print("一番使われている文字は'%s'で%d個使われています" %
      (k_sorted[0][0],k_sorted[0][1] ))

