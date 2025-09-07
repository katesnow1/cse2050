class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Mapping:
    def __init__(self):
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for _ in range(self._n_buckets)]
        self.max_loadfactor = 1.5

    def __contains__(self, key):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                return True
        
        return False
    
    def __len__(self):
        return self._len
    
    def __setitem__(self, key, value):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                entry.value = value
                return
        self._L[i_bucket].append(Entry(key, value))
        self._len += 1

        if len(self) / self._n_buckets > self.max_loadfactor:
            self.rehash(self._n_buckets * 2)

    def __getitem__(self, key):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                return entry.value
            
        raise KeyError(f"Key {key} not found.")
    
    def rehash(self, new_buckets):
        self._n_buckets = new_buckets
        new_L = [[] for _ in range(self._n_buckets)]
        for bucket in self._L:
            for entry in bucket:
                i = hash(entry.key) % self._n_buckets
                new_L[i].append(entry)

        self._L = new_L
