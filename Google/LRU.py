from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.popval = 0
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.popval = self.cache.pop(key)
            self.cache[key] = self.popval
            return self.popval
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            self.cache.pop(self.cache.keys()[0])
            self.cache[key] = value