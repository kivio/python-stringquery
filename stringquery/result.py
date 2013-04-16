__author__ = 'kivio'

class StringResult(object):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            self.__setattr__(key, value)

        self._data = args

    def __iter__(self):
        for dat in self._data:
            yield dat
