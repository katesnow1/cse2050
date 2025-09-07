class Entry:
    def __init__(self, key, value):
        """Creates a new entry object"""
        self.key = key
        self.value = value

    def __repr__(self):
        """Returns string representation of obj"""
        return f"Entry({self.key}, {self.value})"
    
class HashMap:
    def __init__(self):
        """Initializes a new empty hashmap"""
        self.n_buckets = 8 # use a power of 2 (1, 2, 4, 8, 16, ...) as the number of buckets
        self._L = [[] for _ in range(self.n_buckets)]
        self._len = 0
        self.max_loadfactor = 1.5

    def __len__(self):
        """Returns number of key:value pairs in hashmap"""
        return self._len
    
    def __setitem__(self, key, value):
        """Adds k:v pair or updates value"""
        # Find the bucket where key  *should* be
        i_bucket = hash(key) % self.n_buckets

        # Iterate over every entry in that bucket
        # If I find the key, update value and return
        for entry in self._L[i_bucket]:
            if entry.key == key:
                entry.value = value
                return
            
        # Append entry to bucket
        self._L[i_bucket].append(Entry(key, value))
        self._len += 1

        if len(self) / self.n_buckets > self.max_loadfactor:
            self.rehash(2*self.n_buckets)

    def rehash(self, new_buckets):
        """Rehashes into int: new_buckets buckets"""
        self.n_buckets = new_buckets
        new_L = [[] for _ in range(self.n_buckets)]
        for bucket in self._L:
            for entry in bucket:
                i = hash(entry.key) & self.n_buckets
                new_L[i].append(entry)

        self._L = new_L

        

    def __getitem__(self, key):
        """Returns value associated with key"""
        i_bucket = hash(key) % self.n_buckets

        for entry in self._L[i_bucket]:
            if entry.key == key:
                return entry.value
        
        raise KeyError(f"Key {key} not found.")
    
    def __contains__(self, key):
        i_bucket = hash(key % self.n_buckets)
        for entry in self._L[i_bucket]:
            if entry.key == key:
                return True
        
        return False
    
