#!/usr/bin/python3
def update_dictionary(a_dictionary,  key, value):
    if key not in a_dictionary.keys():
        a_dictionary.update({key: value})
    else:
        a_dictionary[key] = value
    for keys, values in a_dictionary.items():
        print("{}: {}".format(keys, values))
