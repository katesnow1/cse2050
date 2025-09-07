# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0):
        """Initializes the LocalRecord object with params pos, max, min, precision"""
        self.pos = (round(pos[0]), round(pos[1])) # (latitude, longitude) tuple
        self.max = max
        self.min = min
        self.precision = precision    

    def add_report(self, temp):
        """Adds a temperature report to the LocalRecord, updates max and min if appropriate"""
        if self.max is None:
            self.max = temp
        if self.min is None:
            self.min = temp
        if temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp
        

    def __eq__(self, other):
        """returns true if two positions are equal to each other, false otherwise"""
        if round(self.pos[0]) == round(other.pos[0]) and round(self.pos[1]) == round(other.pos[1]):
            return True
        else:
            return False

    def __hash__(self):
        """Returns a hash for the LocalRecord object based on its position"""
        return hash(self.pos)

    def __repr__(self):
        """Returns a string representation of the LocalRecord object"""
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap: #custom set, but with key:value pairs
    def __init__(self):
        """initializes the RecordsMap object"""
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for _ in range(self._n_buckets)]

    def __len__(self):
        """retursn the number of many key:value pairs are stored"""
        return self._len
    
    def __contains__(self, pos):
        """returns true if a given position is in the RecordsMap, false otherwise"""
        lr = LocalRecord(pos)
        idx = hash(lr) % self._n_buckets
        for record in self._L[idx]:
            if record == lr:
                return True
        return False

    def add_report(self, pos, temp):
        """adds a report to the RecordsMap"""
        lr = LocalRecord(pos, max=temp, min=temp)

        if pos in self: 
            return lr.add_report(temp)
        
        idx = hash(lr) % self._n_buckets
        self._L[idx].append(lr)
        self._len += 1
        if len(self) >= 2*self._n_buckets:
            self._rehash(self._n_buckets * 2)

    def __getitem__(self, pos):
        """gets the (min, max) tuple for a given position"""
        lr = LocalRecord(pos)
        if pos not in self: raise KeyError(f"Key {pos} not in RecordsMap")
        idx = hash(lr) % self._n_buckets
        for record in self._L[idx]:
            if lr==record:
                return (record.min, record.max)

            
    def _rehash(self, m_new):
        """rehashes as number of entries increases"""
        new_L = [[] for i in range(m_new)]

        for bucket in self._L:
            for lr in bucket:
                newIdx = hash(lr) % m_new
                new_L[newIdx].append(lr)
        
        self._L = new_L
        self._n_buckets = m_new