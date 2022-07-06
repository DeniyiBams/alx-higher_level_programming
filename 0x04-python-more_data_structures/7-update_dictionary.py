#!/usr/bin/python3
def update_dictionary(a_dictionary,  key, value):
    a_dictionary[key] = value
    for keys, values in a_dictionary.items():
        print("{}: {}".format(keys, values))
