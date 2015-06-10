__author__ = 'LeeYoungNam'


from file_manager import *


name = "result"
click_list = load_obj(name)

threshold = 0.8

f = open('./solution.dat', 'w')

result = []
for i in click_list:
    if i[2] >= threshold:
        if i[0] not in result:
            result.append(i[0])
            f.write('\n')
            f.write(str(i[0]) + ";" + str(i[1]))
        else:
            f.write("," + str(i[1]))

