import sqlite3

from requests_html import HTMLSession #スクレイピング
import datetime #現在時刻の取得
import csv #csvファイルの読み込み
import sys #コマンドライン引数、プログラム終了

def get_info(st, r):

    #改行単位でsplit
    #参考URL：https://karupoimou.hatenablog.com/entry/2019/07/08/112734
    page = r.text.split("\n")
    unko = '*'
    for i in range(len(page)):
        p = page[i]
        if "運行情報" in p:
            unko = page[i+1]#「運行情報」文字列の次の行に内容が書いてある．
    return st +"駅は"+ unko

def get_timetable(r):

    #時刻表（時間）を取得
    hour = r.html.find(".side01")#平日
    if len(hour)==0:
        hour = r.html.find(".side02")#平日以外
    hour_list = []
    for h in hour:
        hour_list.append(int(h.text))
    train = hour_list[0]#始発時間を取得

    #時刻表（分）を取得
    minute = r.html.find(".min1001")#普通列車のclass
    minute_list = []
    for m in minute:
        minute_list.append(int(m.text))
    del minute_list[0]#最初と最後の要素は時刻ではないので削除
    del minute_list[-1]#同上

    #時刻表を格納するための２次元配列の初期化
    num = len(minute_list)
    dep = [[0 for i in range(2)] for j in range(num)]

    #時刻表の構築作業
    for i in range(num):
        if  i>0 and minute_list[i-1] > minute_list[i]:
            train+=1
        dep[i] = (train, minute_list[i])
    return dep

def echo_dep(dep, time):

    #指定時刻から先の3つの発車時刻を格納するため配列の定義
    dep_time = []
    #現在時刻から最も近い発車時刻を取得
    next=0
    now_i=0
    num = len(dep)
    for i in range(num):#始発電車から１つずつ探していく．
        if dep[i][0]==time.hour:#現在時刻（時間）と比較
            now_i = i
            if dep[i][1]>time.minute:#現在時刻（分）と比較
                next = i
                break
    if next==0:#分がHitしなかった場合の処理（時間を繰り上げ）
        next=now_i+1

    #表示用リストの作成
    for i in range(4):
        if next+i>=num:
            next = -1
            dep_time.append("〜終電〜")
        dep_time.append(str(dep[next+i][0]).zfill(2)+":"+str(dep[next+i][1]).zfill(2))

    return dep_time

k_st = list()
def get_station_id(station_name):
    con = sqlite3.connect('keikyu.db')
    cur = con.cursor()
    st = station_name
    query = "select st, id from stations where st " %st
    cur.execute(query)
    info = cur.fetchone()
    return print("%s" % info[0])

def get_url(st , dir, dw):
    slCode = get_station_id(st)
    return "https://norikae.keikyu.co.jp/transit/norikae/T5?dw="+dw+"&slCode="+slCode+"&d="+dir

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("次のコマンドライン引数を与えてください．\n１->駅名（日本語），２->上り:1，下り:2，３->平日:0，土曜:1，休日:2")
        sys.exit(1)

    url = get_url(sys.argv[1], sys.argv[2], sys.argv[3])
    #print(url)
    #①駅名（日本語），②上り:1，下り:2，③平日:0，土曜:1，休日:2

    # セッション開始
    session = HTMLSession()
    r = session.get(url)

    # ブラウザエンジンでHTMLを生成させる
    r.html.render()

    #運行情報を取得
    info = get_info(sys.argv[1],r)

    #時刻表を取得
    dep = get_timetable(r)

    #現在時刻を取得
    #参考URL：https://note.nkmk.me/python-datetime-now-today/
    time = datetime.datetime.now()

    #次の発車時刻を取得
    dep_time = echo_dep(dep, time)

    #結果出力
    print("今日もおつかれさまでした．")
    print(info)
    print("次の発車は,")
    [print(i) for i in dep_time]

    sys.exit(0)