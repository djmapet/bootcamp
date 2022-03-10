#coding: UTF-8
data = dict()
with open("news.txt","r") as open_news:
    us_news = open_news.read()

print(us_news)
blank = us_news.replace(" ","")
marge = blank.lower()

for k in marge:
    data[k] = marge.count(k)

k_sorted = sorted(data.items(), key=lambda x:x[1], reverse=True)
print(k_sorted)

print("一番使われている文字は'%s'で%d個使われています" %
      (k_sorted[0][0],k_sorted[0][1] ))