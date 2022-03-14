#coding: UTF-8
data = dict()
with open("practice3_news.txt","r") as open_text:
    practice_news = open_text.read()

print(practice_news)


import re
open = re.findall(r"[a-zA-Z]+",practice_news)

words = {}
for word in practice_news.split():
    words[word] = words.get(word, 0) +1

count_words = [ (v,k) for k,v, in words.items()]
count_words.sort()
count_words.reverse()

for count, word in count_words:
    print (count,word)


