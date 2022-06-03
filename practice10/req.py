from requests_html import HTMLSession

url = "https://norikae.keikyu.co.jp/transit/norikae/T5?uid=34683&dir=7&path=202010272317801&USR=PC&dw=0&slCode=250-28&d=2&rsf=%89%A9%8B%E0%92%AC"
#京急線 黄金町駅　下り普通のURL

# セッション開始
session = HTMLSession()
r = session.get(url)

# ブラウザエンジンでHTMLを生成させる
r.html.render()#ブラウザでHTMLを生成
print(r.text)#ブラウザで生成したHTMLを出力