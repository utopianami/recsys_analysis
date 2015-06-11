#-*- coding: utf-8 -*-

import pandas as pd
from file_manager import *
import csv
import numpy as np

def matching(df_test, dict_fp, dict_conf, threshold, f):
    test_session = df_test.groupby(['session_id'])

    result = []
    k = 0
    progress = 0
    write_csv = 0
    for name, click_logs in test_session:
        k += 1
        #진행상황 프린트
        if k - progress == 10000:
            progress = k
            print progress, write_csv , write_csv*100/progress

        bought_list = []
        click_items = click_logs.item_id.tolist()

        for item in click_items:

            if item not in dict_fp.keys():
                continue

            val = prediction(click_items, item, dict_fp[item], dict_conf)

            if val >= threshold:
                bought_list.append(item)


        if len(bought_list) > 0:
            write_csv += 1
            write(f, name, bought_list)

    return result




def prediction(click_item, target_item, item_pattern, dict_conf):

    click_item_set = set(click_item)

    max_val = -9999

    # print "--------"

    for pattern_info in item_pattern:
        sup = pattern_info.values()[0][0]
        confidence = float(pattern_info.values()[0][1]) / dict_conf[pattern_info.keys()[0]]


        if sup < 0.7 or confidence < 0.5:
            continue

        pattern = set(pattern_info.keys()[0])
        intersection = len(pattern & click_item_set)
        union = len(pattern | click_item_set)
        similarity = float(intersection)/len(pattern)


        num_of_target_item = 0
        for i in click_item:
            if target_item == i:
                num_of_target_item += 1


        # tmp_val = float(similarity) * sup* confidence

        tmp_val = (similarity*0.6) + (sup*0.2) + (confidence*0.2)
        tmp_val = float(tmp_val)/3 + float(1)/len(click_item) + float(num_of_target_item)/ len(click_item)
        # print tmp_val, sup, confidence, similarity

        if tmp_val > max_val:
            max_val = tmp_val

    return max_val


def write(f, name, bought_list):
    f.write(str(name) + ";" + str(bought_list[0]))
    if len(bought_list) >= 2:
        for i in range(1,len(bought_list)):
            f.write("," + str(bought_list[i]))
    f.write('\n')


if __name__ == "__main__":

    dict_fp = load_obj("result/item_pattern_dict")
    address_test_data = "../data/non_agg/non_agg_test_data.csv"
    df_test = pd.read_csv(address_test_data)

    dict_conf = load_obj("result/dict_confidence")
    threshold = 1.7

    f = open('solution.dat', 'w')


    print "start", threshold
    # call function
    result =  matching(df_test, dict_fp, dict_conf, threshold, f)

    #
    # print "write all file"
    # save_obj(result, "result")