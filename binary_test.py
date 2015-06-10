#-*- coding: utf-8 -*-

__author__ = 'LeeYoungNam'


import pickle


# a = { 1:set([2,2]), 3:set([4,4,4])}
# print a
#
#
def save_obj(obj, name ):
    with open(name + '.pkl', 'ab+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
#
#
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


a = load_obj("result/dict_confidence")

print len(a.keys())
#
# dict_confidence = {}
#
#
# k = 0
# progress = 0
# for i in a:
#     for j in a[i]:
#         if j.keys()[0] not in dict_confidence:
#             dict_confidence[j.keys()[0]] = j.values()[0][1]
#         else:
#             dict_confidence[j.keys()[0]] += j.values()[0][1]
#
#     #진행상황 프린트
#     if k - progress == 100:
#         progress = k
#         print progress
#
#
# save_obj(dict_confidence, "dict_confidence")