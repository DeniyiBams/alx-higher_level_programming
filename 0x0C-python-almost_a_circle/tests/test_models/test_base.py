#!/usr/bin/python3

"""
Unittest for models/base.py
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    '''Tests for base class'''

    def setUp(self):
        '''Runs before individual test cases'''

        Base._Base__nb_objects = 0

    def test_class_docstrings(self):
        '''Tests for the Base class docstring'''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_correct_id(self):
        ''' Test for correct output of id'''
        
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertTrue(b1.id, 1)
        self.assertTrue(b2.id, 2)
        self.assertTrue(b3.id, 3)

    def test_custom_id(self):
        '''Test after correct id'''

        b = Base(23)

        self.assertTrue(b4.id, 23)

    def test_correct_id_custom(self):
        '''Test for correct id after custom id'''

        b = Base()

        self.assertTrue(b.id, 1)

    def test_string_input(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_none_input(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_zero_input(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_input(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_list_input(self):
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_class_type(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})

    def test_private_id(self):
        b = Base(1)
        with self.assertRaises(Exception) as e:
            print(b.nb__objects)
        self.assertEqual(
            "'Base' object has no attribute 'nb__objects'",
            str(e.exception)
