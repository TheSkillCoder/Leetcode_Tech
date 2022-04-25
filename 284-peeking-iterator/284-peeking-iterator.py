class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.temp = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.temp

    def next(self):
        """
        :rtype: int
        """
        value = self.temp
        if self.iterator.hasNext():
            self.temp = self.iterator.next()
        else:
            self.temp = None
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.temp is None:
            return False
        else:
            return True