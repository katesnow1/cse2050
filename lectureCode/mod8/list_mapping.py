class Entry:
    def __init__(self, key, value):
        """Creates a new entry object"""
        self.key = key
        self.value = value

    def __repr__(self):
        """Returns string representation of obj"""
        return f"Entry({self.key}, {self.value})"

    
class Mapping:
    def __init__(self):
        """Creates a new empty mapping"""
        self._L = []

    def __setitem__(self, key, value):
        """Adds key:value pair to mapping, or updates value if key already in mapping"""
        for entry in self._L:
            if entry.key == key:
                entry.value = value
                return
            
        self._L.append(Entry(key, value))

    def __getitem__(self, key):
        """Return the value associated with key, or raise a KeyError if key not in mapping"""
        for entry in self._L:
            if entry.key == key:
                return entry.value
            
        raise KeyError(f"Key {key} not in mapping")
    
class Mapping2:
    def __init__(self):
        """Creates a new empty mapping"""
        self._L = []

    def __setitem__(self, key, value):
        """Adds key:value pair to mapping, or updates value if key already in mapping"""
        self._L.append(Entry(key, value))

    def __getitem__(self, key):
        """Return the value associated with key, or raise a KeyError if key not in mapping"""
        n = len(self._L)
        for i in range(n):
            if self._L[n-1-i].key == key:
                return self._L[n-1-i].value
            
        raise KeyError(f"Key {key} not in mapping")

if __name__ == '__main__':
    m1 = Mapping()
    m1['jake'] = ['cse2050', 'cse3100']          # __setitem__
    assert m1['jake'] == ['cse2050', 'cse3100']  # __getitem__

    print("all good")