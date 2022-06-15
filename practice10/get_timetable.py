import sqlite3

from requests_html import HTMLSession #スクレイピング
import datetime #現在時刻の取得
import csv #csvファイルの読み込み
import sys #コマンドライン引数、プログラム終了

def get_timetable(r):

    "時刻表（時間）を取得"
    hour = r.html.find(".side01")#平日
    if len(hour) == 0:
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

    "時刻表を格納するための２次元配列の初期化"
    num = len(minute_list)
    dep = [[0 for i in range(2)] for j in range(num)]

    "時刻表の構築作業"
    for i in range(num):
        if i > 0 and minute_list[i-1] > minute_list[i]:
            train += 1
        dep[i] = (train, minute_list[i])
    return dep

def get_station_id(station_name):
    con = sqlite3.connect('keikyu.db')
    cur = con.cursor()
    query = "select st, id from stations where st='%s' " % station_name
    cur.execute(query)
    info = cur.fetchone()
    if info:
        return info[1]
    else:
        return None



def get_url(st, dir, dw):
    slCode = get_station_id(st)
    if not slCode == None:
        return "https://norikae.keikyu.co.jp/transit/norikae/T5?dw=" + dw + "&slCode=" + slCode + "&d=" + dir
    else:
        return None


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("次のコマンドライン引数を与えてください．\n１->駅名（日本語），２->上り:1，下り:2，３->平日:0，土曜:1，休日:2")
        sys.exit(1)

    url = get_url(sys.argv[1], sys.argv[2], sys.argv[3])
    "print(url)"
    "①駅名（日本語），②上り:1，下り:2，③平日:0，土曜:1，休日:2"
    if url == None:
        print("指定された駅は見つかりませんでした")
        sys.exit(1)


    "セッション開始"
    session = HTMLSession()
    r = session.get(url)

    "ブラウザエンジンでHTMLを生成させる"
    r.html.render()

    "時刻表を取得"
    st_name = sys.argv[1]
    st_id = get_station_id(st_name)
    dep = get_timetable(r)
    num = len(dep)
    for i in range(num):
        print("%s,%d,%d,%s,%s" % (st_id, dep[i][0], dep[i][1], sys.argv[2], sys.argv[3]))
