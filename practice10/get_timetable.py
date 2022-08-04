import sqlite3

from requests_html import HTMLSession #スクレイピング
import datetime #現在時刻の取得
import csv #csvファイルの読み込み
import sys #コマンドライン引数、プログラム終了

def parse_timetable(r):

    "時刻表（時間）を取得"
    hour = r.html.find(".side01")#平日
    if len(hour) == 0:
        hour = r.html.find(".side02")#平日以外
    hour_list = []
    for h in hour:
        hour_list.append(int(h.text))
    train = hour_list[0]#始発時間を取得

    "時刻表（分）を取得"
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

def get_timetable(station_name):
    "セッション開始"
    session = HTMLSession()
    "sqlを追加"
    con = sqlite3.connect("stations.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    st_id = get_station_id(station_name)
    time_table = list()
    for dir in range(1,3):
        for dw in range(0,3):
            url = get_url(station_name, dir, dw)
            r = session.get(url)


            "ブラウザエンジンでHTMLを生成させる"
            r.html.render()

            dep = parse_timetable(r)
            num = len(dep)
            for i in range(num):
                l = (st_id, dep[i][0], dep[i][1], dir, dw)
                time_table.append(l)
                query = "select st_id where station_name"
                cur.execute(query)
                n = cur.fetchone()

    return time_table

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
        return "https://norikae.keikyu.co.jp/transit/norikae/T5?slCode=%s&dw=%d&d=%d" % (slCode, dw, dir)
    else:
        return None

def make_csv(list, file_name):
    with open(file_name, 'w') as add_file:
        writer = csv.writer(add_file)
        writer.writerows(list)

if __name__ == '__main__':

    if len(sys.argv) == 2:
        st_name = sys.argv[1]
    else:
        print("駅名を指定してください")
        sys.exit(1)


    "時刻表を取得"
    t_tbl = get_timetable(st_name)
    print(t_tbl)
    make_csv(t_tbl, 'timetable.csv')
