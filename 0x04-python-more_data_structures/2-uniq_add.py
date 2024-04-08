#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(set(my_list))

my_list = [8, 3, 2]
print("answer: {}".format(uniq_add(my_list)))

