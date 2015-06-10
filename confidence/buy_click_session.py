#-*- coding: utf-8 -*-
from loadfile import *
from apriori2 import *
import pickle
from file_manager import *

if __name__ == "__main__":

    address_click_data = "output_data/buy_click_data.csv"
    df_click = pd.read_csv(address_click_data)

    items_fp = load_obj("result/pattern_item_list")

    click_session = df_click.groupby(['session_id'])
    dict_pattern = {}

    print "start"

    progress = 0
    progress_j = 0
    k = 0
    j = 0 #509,696
    for fp in items_fp:
        dict_pattern[tuple(fp)] = 0

        k += 1
        #진행상황 프린트
        if k - progress == 20:
            progress = k
            print progress

        for name, session in click_session:


            j += 1
            if j - progress_j == 10000:
                progress_j = j
                print k, progress_j

            click_log = set(session.item_id.tolist())
            if fp.issubset(click_log):
                dict_pattern[tuple(fp)] += 1

    print "write file"


    file_name = "result/buy_click_session"
    save_obj(file_name, dict_pattern)