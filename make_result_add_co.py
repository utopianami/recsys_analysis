#-*- coding: utf-8 -*-

import pandas as pd
from file_manager import *
import csv

def matching(df_test, dict_fp, dict_conf, threshold):
    test_session = df_test.groupby(['session_id'])

    result = []
    k = 0
    progress = 0
    for name, click_logs in test_session:
        k += 1
        #진행상황 프린트
        if k - progress == 1000:
            progress = k
            print progress

        bought_list = []
        click_items = click_logs.item_id.tolist()

        for item in click_items:

            if item not in dict_fp.keys():
                continue

            val = prediction(set(click_items), dict_fp[item], dict_conf)

            if val >= threshold:
                tmp = [name, item, val]
                result.append(tmp)

        #
        # if len(bought_list) > 0:
        #     write(f, name, bought_list)

    return result




def prediction(click_item, item_pattern, dict_conf):

    max_val = -9999
    for pattern_info in item_pattern:
        pattern = set(pattern_info.keys()[0])

        intersection = len(pattern & click_item)
        similarity = float(intersection)/len(click_item)
        confidence = float(pattern_info.values()[0][1]) / dict_conf[pattern_info.keys()[0]]

        sup = pattern_info.values()[0][0]
        tmp_val = float(similarity) * sup * confidence

        print "val", click_item, similarity, confidence, confidence

        if tmp_val > max_val:
            max_val = tmp_val

    return max_val


# def write(f, name, bought_list):
#     f.write(str(name) + ";" + str(bought_list[0]))
#     if len(bought_list) >= 2:
#         for i in range(1,len(bought_list)):
#             f.write("," + str(bought_list[i]))
#     f.write('\n')


if __name__ == "__main__":

    dict_fp = load_obj("result/item_pattern_dict")
    address_test_data = "../data/test_data.csv"
    df_test = pd.read_csv(address_test_data)

    dict_conf = load_obj("result/dict_confidence")
    threshold = 0.5

    # f = open('solution.dat', 'w')


    "start"
    # call function
    result =  matching(df_test, dict_fp, dict_conf, threshold)


    print "write all file"
    save_obj(result, "result")