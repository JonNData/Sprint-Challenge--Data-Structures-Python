"""
Holds fixed capacity, potentially with None at the beginning.
When appended, oldest is overwritten, Queue is also FIFO
"""
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = capacity * [None]
        self.counter = 0

    def append(self, item):
        """
        Items need to be replaced FIFO, but the order must remain intact
        Queue, maybe multiple?
        ENUMERATE!! wooo... hmm how would append know that on subsequent calls?
        So we need a counter to keep track of position
        Forget that, let's just use arrays
        """
        self.storage[self.counter] = item
        self.counter +=1
        if self.counter == self.capacity:
            self.counter = 0

    def get(self):
        """
        This returns a list. Do we want to work with the list earlier? Or just at the end?
        """
        return [x for x in self.storage if x is not None]