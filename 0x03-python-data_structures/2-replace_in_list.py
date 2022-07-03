#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for item in my_list:
        if item == my_list[idx]:
            my_list[idx] = element
    return my_list
