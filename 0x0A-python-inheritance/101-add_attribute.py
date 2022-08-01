#!/usr/bin/python3
"""
add_attribute function
"""


def add_attribute(obj, key, value):
    """ Adds a new atrribute to an object if possible """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
