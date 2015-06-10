#-*- coding: utf-8 -*-
from loadfile import *
from apriori2 import *
import pickle
from file_manager import *

if __name__ == "__main__":


    support  = 0.6

    ## variable
    df_click, df_buy, df_test = load_csv(real)

    address_click_data = "input/buy_click_data.csv"
    address_buy_data = "../data/buy_data.csv"

    df_click = pd.read_csv(address_click_data)
    df_buy = pd.read_csv(address_buy_data)

    items = df_buy.groupby(['item_id'])
    click_session = df_click.groupby(['session_id'])
    dict_fp ={}


    print "start"

    ####find fp
    progress = 0
    k = 0
    for name, sessions in items:
        session_click_log_list = []
        session_list = sessions.session_id.tolist()

        k += 1

        # 진행상황 프린트
        if k - progress == 100:
            progress = k
            print progress

        if len(session_list) == 1:
            click_log = click_session.get_group(session_list[0]).item_id.tolist()
            if len(click_log) > 7:
                continue

        for session in session_list:
            idx_click_item = 0
            click_log = click_session.get_group(session).item_id.tolist()

            #문제상황
            session_click_log_list.append(set(click_log))
        dict_fp = confidence_apriori(session_click_log_list, support, dict_fp)
        print dict_fp

        if k == 2:
            break

    #
    # print "save data"
    #
    #
    #
    #
    # save_obj(dict_fp, "result/item_pattern_dict")
    # output = open('item_pattern_dict.txt', 'ab+')
    # pickle.dump(dict_fp, output)
    # output.close()
