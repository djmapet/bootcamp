#coding: UTF-8
us_news = 'TheUnited States has announced it is sending additional military assistance to Ukraine'
blank_us_news = us_news.replace(" ","")
marge = blank_us_news.lower()
data = dict()

for k in marge:
    data[k] = marge.count(k)


k_sorted = sorted(data.items(), key=lambda x:x[1],reverse=True)

print('K=',k_sorted)


print("一番使われている文字は'%s'で%d個使われています" %
      (k_sorted[0][0],k_sorted[0][1] ))