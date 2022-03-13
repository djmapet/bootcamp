#coding: UTF-8
data = dict()
with open("practice3_news.txt","r") as open_text:
    practice_news = open_text.read()

print(practice_news)


import re
open = re.findall(r"[a-zA-Z]+",practice_news)
print(open)

