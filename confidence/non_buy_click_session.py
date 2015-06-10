#-*- coding: utf-8 -*-
from loadfile import *
from apriori2 import *
import pickle
from file_manager import *

if __name__ == "__main__":


    address_click_data = "input/non_buy_click_data.csv"
    df_click = pd.read_csv(address_click_data)


    output = open('item_pattern_list.txt', 'rb')
    items_fp = pickle.load(output)

    click_session = df_click.groupby(['session_id'])
    dict_pattern = {}


    progress = 0
    k = 0
    for fp in items_fp:
        dict_pattern[tuple(fp)] = 0

        k += 1
        #진행상황 프린트
        if k - progress == 100:
            progress = k
            print progress

        for name, session in click_session:
            click_log = set(session.item_id.tolist())
            if fp.issubset(click_log):
                dict_pattern[tuple(fp)] += 1

    print "write file"
    file_name = "result/non_buy_click_session"
    save_obj(file_name, dict_pattern)