class Entry:
    def __init__(self, item, priority):
        """initializes an Entry object with item and priority params"""
        self.item = item
        self.priority = priority

    def __eq__(self, other):
        """returns True if self's priority is equal to other's priority, false otherwise"""
        return self.priority == other.priority

    def __lt__(self, other):
        """returns True if self's priority is less than other's priority, false otherwise"""
        return self.priority < other.priority

    def __le__(self, other):
        """returns True if self's priority is less than or equal to other's priority, false other wise"""
        return self.priority <= other.priority

    def __repr__(self):
        """returns a string representation of the entry object"""
        return f'Entry(item={self.item}, priority={self.priority})'
