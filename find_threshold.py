#-*- coding: utf-8 -*-

__author__ = 'LeeYoungNam'



from file_manager import *


name = "result"
click_list = load_obj(name)

print "start"
print len(click_list)

threshold = 0.75
result = []



for i in click_list:
    print i

#
# k = 0
# progress = 0
# for i in click_list:
#     if i[2] >= threshold:
#         if i[0] not in result:
#             result.append(i[0])
#
#     k += 1
#
#     # 진행상황 프린트
#     if k - progress == 100:
#         progress = k
#         print progress
#
#
#
#
# print len(result)