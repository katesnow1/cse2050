class Entry:
    def __init__(self, item, priority):
        """initializes an Entry object with params item, priority"""
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        """returns true if self's priority is less than other's priority"""
        return self.priority < other.priority

    def __eq__(self, other):
        """returns true if self's item and priority are equal to other's item and priority"""
        return self.item == other.item and self.priority == other.priority

class PQ_UL:
    """priority queue ADT with an unordered list data structure"""
    def __init__(self):
        """Initializes an priority queue ADT with an unordered list data structure"""
        self._L = []

    def __len__(self):
        """returns length of the p"""
        return len(self._L)

    def insert(self, item, priority):
        """adds item with priority to PQ"""
        self._L.append(Entry(item, priority))

    def find_min(self):
        """returns item with minimum priority"""
        min_entry = Entry("hello", float('inf'))
        for e in self._L:
            if e < min_entry:
                min_entry = e

        return min_entry

    def remove_min(self):
        """removes item with minimum priority"""
        min_entry = self.find_min()
        self._L.remove(min_entry)
        return min_entry

class PQ_OL:
    """priority queue ADT with an ordered list data structure"""
    def __init__(self):
        """Initializes an priority queue ADT with an unordered list data structure"""
        self._L = []

    def __len__(self):
        """returns length of the PQ"""
        return len(self._L)

    def insert(self, item, priority):
        """adds item with given priority to PQ"""
        self._L.append(Entry(item, priority))
        self._L.sort(reverse=True)

    def find_min(self):
        """returns item with minimum priority"""
        return self._L[-1]

    def remove_min(self):
        """remove item with minimum priority"""
        return self._L.pop()