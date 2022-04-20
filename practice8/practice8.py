# coding: UTF-8
import csv
tennis_player_list = list()
with open("olympic_tennis.csv", "r") as open_text:
    reader = csv.reader(open_text, delimiter="\t", doublequote=True, lineterminator="\r\n", quotechar='"',skipinitialspace=True)
    header = next(reader)

    for tennis in reader:
        id = tennis[0]
        name = tennis[1]
        sex = tennis[2]
        age = tennis[3]
        height = tennis[4]
        weight = tennis[5]
        team = tennis[6]
        noc = tennis[7]
        medal = tennis[14]
        tennis_player = (id, name, sex, age, height, weight, team, noc, medal)
        tennis_player_list.append(tennis_player)

gold_medal = list(filter(lambda x: x[8] == 'Gold',tennis_player_list))
many_gold = sorted(gold_medal, key=lambda x: x[7],reverse=True)
silver_medal = list(filter(lambda x: x[8] == 'Silver', tennis_player_list))
bronze_medal = list(filter(lambda x: x[8] == 'Bronze', tennis_player_list))
got_medal = [gold_medal, silver_medal, bronze_medal]

print(many_gold)