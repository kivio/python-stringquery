__author__ = 'kivio'

import re

from result import StringResult

class StringQuery(object):

    def __init__(self, query = None, data = None):
        self._data = data
        self._query = query
        if data and query:
            self._make_query(data, query)

    def query(self, data = None, query = None):
        if not self._query and not query:
            raise TypeError("query method expected query")

        if not self._data and not data:
            raise TypeError("query method expected data")

        return self._make_query(self._data or data, self._query or query)

    def _make_query(self, data, query):
        query_kw = self._evaluate_query(query)
        query_reg = self._evaluate_regexp(query)
        result = self._get_data(query_reg, data)
        result = dict(zip(query_kw, result))
        return StringResult(**result)

    def _evaluate_query(self, query):
        query_ev = []
        kwargs = query.split("{")
        for kw in kwargs:
            query_ev.append(kw.split("}")[0])
        return tuple(filter(lambda x: x != '', query_ev))

    def _evaluate_regexp(self, data):
        return re.sub(r"{\w+}", "(.*)", data)

    def _get_data(self, query, data):
        return re.findall(query, data)[0]

