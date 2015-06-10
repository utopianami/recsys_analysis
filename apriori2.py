#-*- coding: utf-8 -*-
__author__ = 'LeeYoungNam'

import itertools



def new_apriori(session_list, support):
    result_fp_list = []

    # min_support 계산
    session_count = len(session_list)
    min_support = session_count * support

    #후보 1개 generate & 후보의 최대길이 구하기
    candidate_element = list(session_list[0])[:]
    candidate_element = set(candidate_element)

    max_candidate_len = len(session_list[0])
    for index in range(1, session_count):
        candidate_element.update(session_list[index])
        if max_candidate_len < len(session_list[index]):
            max_candidate_len = len(session_list[index])

    candidate = set(itertools.combinations(candidate_element, 1))

    # loop invariant
    cur_candidate_len = 1
    while(True):

        dict_tmp = {}
        for item_list in session_list:

            for c in candidate:
                if set(c).issubset(item_list):
                    if c in dict_tmp.keys():
                        dict_tmp[c] += 1
                    else:
                        dict_tmp[c] = 1
        cur_candidate_len += 1

        #다음 길이의 후보들 고르기
        candidate_element = set([])
        for key in dict_tmp:
            if dict_tmp[key] >= min_support:
                item_sup = float(dict_tmp[key])/session_count
                result_fp_list.append({key:[item_sup,dict_tmp[key]]})
                candidate_element.update(set(key))

        if len(candidate_element) == 0 or cur_candidate_len > max_candidate_len:
            break

        # 후보 생성
        candidate = set(itertools.combinations(candidate_element, cur_candidate_len))


    return result_fp_list



def get_item_pattern(session_list, support, list_pattern):

    # min_support 계산
    session_count = len(session_list)
    min_support = session_count * support

    #후보 1개 generate & 후보의 최대길이 구하기
    candidate_element = list(session_list[0])[:]
    candidate_element = set(candidate_element)

    max_candidate_len = len(session_list[0])
    for index in range(1, session_count):
        candidate_element.update(session_list[index])
        if max_candidate_len < len(session_list[index]):
            max_candidate_len = len(session_list[index])

    candidate = set(itertools.combinations(candidate_element, 1))

    # loop invariant
    cur_candidate_len = 1
    while(True):

        dict_tmp = {}
        for item_list in session_list:

            for c in candidate:
                if set(c).issubset(item_list):
                    if c in dict_tmp.keys():
                        dict_tmp[c] += 1
                    else:
                        dict_tmp[c] = 1
        cur_candidate_len += 1

        #다음 길이의 후보들 고르기
        candidate_element = set([])
        for key in dict_tmp:
            if dict_tmp[key] >= min_support:
                if set(key) not in list_pattern:
                    list_pattern.append(set(key))
                candidate_element.update(set(key))

        if len(candidate_element) == 0 or cur_candidate_len > max_candidate_len:
            break

        # 후보 생성
        candidate = set(itertools.combinations(candidate_element, cur_candidate_len))

    return list_pattern


def confidence_apriori(session_list, support, dict_confidence):

    # min_support 계산
    session_count = len(session_list)
    min_support = session_count * support

    #후보 1개 generate & 후보의 최대길이 구하기
    candidate_element = list(session_list[0])[:]
    candidate_element = set(candidate_element)

    max_candidate_len = len(session_list[0])
    for index in range(1, session_count):
        candidate_element.update(session_list[index])
        if max_candidate_len < len(session_list[index]):
            max_candidate_len = len(session_list[index])

    candidate = set(itertools.combinations(candidate_element, 1))

    # loop invariant
    cur_candidate_len = 1
    while(True):

        dict_tmp = {}
        for item_list in session_list:

            for c in candidate:
                if set(c).issubset(item_list):
                    if c in dict_tmp.keys():
                        dict_tmp[c] += 1
                    else:
                        dict_tmp[c] = 1
        cur_candidate_len += 1

        #다음 길이의 후보들 고르기
        candidate_element = set([])
        for key in dict_tmp:
            if dict_tmp[key] >= min_support:
                if key in dict_confidence.keys():
                    dict_confidence[key] += 1
                else:
                    dict_confidence[key] = 1

                candidate_element.update(set(key))

        if len(candidate_element) == 0 or cur_candidate_len > max_candidate_len:
            break

        # 후보 생성
        candidate = set(itertools.combinations(candidate_element, cur_candidate_len))


    return dict_confidence


if __name__ == "__main__":
    a = []
    a1 = [1,2,3,4]
    a2 = [2,3,4]
    a3 = [4,5,6,1,2]
    a4 = [6,1,2]

    a.append(set(a1))
    a.append(set(a2))
    a.append(set(a3))
    a.append(set(a4))

    result_list = []

    print new_apriori(a, 0.6)