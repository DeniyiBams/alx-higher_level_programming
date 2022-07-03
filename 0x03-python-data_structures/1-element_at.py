#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    for element in my_list:
        if element == my_list[idx]:
            return element
            break
