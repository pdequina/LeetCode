class MyHashSet(object):

    def __init__(self):
        self.array = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.array:
            self.array.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.array:
            self.array.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.array

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
