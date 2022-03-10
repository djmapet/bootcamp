#coding: UTF-8
data = dict()
with open("news.txt","r") as open_news:
    print(open_news.read())

    for k in open_news:
        data[k] = open_news.count(k)
        print(data)
    k_sorted = sorted(data.items(), key=lambda x:x[1],reverse=True)
