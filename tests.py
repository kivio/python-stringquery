__author__ = 'kivio'

import unittest
from unittest import TestCase
from stringquery import StringQuery

class StringQueryTest(TestCase):

    def setUp(self):
        self.sq = None
        self.simple_name = "Marcin"
        self.simple_surname = "Karkocha"
        self.data = "{} {}".format(self.simple_name, self.simple_surname)
        self.simple_query = "{name} {surname}"

    def assertSimpleQuery(self, result):
        self.assertTrue(hasattr(result, 'name'))
        self.assertEqual(result.name, self.simple_name)
        self.assertTrue(hasattr(result, 'surname'))
        self.assertEqual(result.surname, self.simple_surname)

    def test_query_and_data_in_constructor(self):
        sq = StringQuery(self.simple_query, self.data)
        result = sq.query()
        self.assertSimpleQuery(result)

    def test_query_in_constructor(self):
        self.sq = StringQuery(self.simple_query)
        result = self.sq.query(self.data)
        self.assertSimpleQuery(result)

    def test_data_in_constructor(self):
        sq = StringQuery(data = self.data)
        result = sq.query(query = self.simple_query)
        self.assertSimpleQuery(result)

if __name__ == "__main__":
    unittest.main()