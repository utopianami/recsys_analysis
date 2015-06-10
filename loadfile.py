#-*- coding: utf-8 -*-

import pandas as pd

real = 'real'
test = 'test'

#real data

address_click_data = "../data/click_data.csv"
address_buy_data = "../data/buy_data.csv"
address_test_data = "../data/test_data.csv"

#test data
test_click_data = "data/click_data.csv"
test_buy_data = "data/test/buy_data.csv"
test_test_data = "data/test/test_data_agg.csv"
test_answer_data = "data/test/test_correct_answer.csv"
test_item_list = "data/test/item_list.csv"


def load_csv(type):

    if type == 'real':
        _df_click = pd.read_csv(address_click_data)
        _df_buy = pd.read_csv(address_buy_data)
        _df_test = pd.read_csv(address_test_data)
        return _df_click, _df_buy, _df_test

    else:
        _df_click = pd.read_csv(test_click_data)
        _df_buy = pd.read_csv(test_buy_data)
        _df_test = pd.read_csv(test_test_data)
        _df_answer = pd.read_csv(test_answer_data)
        _df_item_list = pd.read_csv(test_item_list)
        return _df_click, _df_buy, _df_test, _df_answer, _df_item_list




