#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if max_score == value:
            return key
    return None
