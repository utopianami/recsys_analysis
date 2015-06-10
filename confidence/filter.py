#-*- coding: utf-8 -*-

__author__ = 'LeeYoungNam'



import pandas as pd
import csv

address_click_data = "input/non_buy_click_data.csv"
df_click = pd.read_csv(address_click_data)

address_buy_item_data = "input/buy_item_list.csv"
df_item = pd.read_csv(address_buy_item_data)


buy_item_list = df_item.item_id.tolist();
click_session = df_click.groupby(['session_id'])


print "start"
print "file open"

result = []

progress = 0
k = 0

for name, session in click_session:
    item_list = session.item_id.tolist()

    for i in item_list:
        if i in buy_item_list:
            result.append([name,i])
    k += 1
    #진행상황 프린트
    if k - progress == 10000:
        progress = k
        print progress
    if k == 1:
        break



print "write"
resultFile = open("output.csv",'wb')
wr = csv.writer(resultFile)

for i in result:
    wr.writerows(result)


print "끝"