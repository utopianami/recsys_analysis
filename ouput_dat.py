#-*- coding: utf-8 -*-
__author__ = 'LeeYoungNam'


import pandas as pd

## variable
address_test_session = "input/result.csv"
df_test = pd.read_csv(address_test_session)
test_sessions = df_test.groupby(['session_id'])

#file
f = open('solution1.dat', 'w')


def write(f, name, bought_list):
    f.write(str(name) + ";" + str(bought_list[0]))
    if len(bought_list) >= 2:
        for i in range(1,len(bought_list)):
            f.write("," + str(bought_list[i]))
    f.write('\n')

k = 0
progress = 0
for name, session in test_sessions:
    items = session.item_id.tolist()

    write(f, name, items)

    k += 1

    # 진행상황 프린트
    if k - progress == 100:
        progress = k
        print progress









max_session_num = 100000

