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
    df_click = pd.read_csv(address_click_data)


    items = df_buy.groupby(['item_id'])
    click_session = df_click.groupby(['session_id'])
    dict_fp ={}


    print "start"

    pattern_list = []
    ####find fp
    progress = 0
    k = 0
    for name, sessions in items:
        session_click_log_list = []
        session_list = sessions.session_id.tolist()
        dict_item = {}

        k += 1

        # 진행상황 프린트
        if k - progress == 50:
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

        pattern_list = get_item_pattern(session_click_log_list, support, pattern_list)


    print "save data"




    save_obj(pattern_list, "patter_item_list_sup5")
    output = open('item_pattern_list5.txt', 'ab+')
    pickle.dump(pattern_list, output)
    output.close()
