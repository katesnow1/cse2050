class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap():
    def __init__(self):
        self._n_buckets = 8
        self._len = 0
        self._L = [[] for _ in range(self._n_buckets)]
        self._max_alpha = 1
        self._min_alpha = 0.25
        self._min_buckets = 8

    def __setitem__(self, key, value):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                entry.value = value
                return
        self._L[i_bucket].append(Entry(key, value))
        self._len += 1

        alpha = len(self) / self._n_buckets
        if alpha > self._max_alpha:
            self.rehash(new_buckets=self._n_buckets * 2)

    def __len__(self):
        return self._len

    def __getitem__(self, key):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                return entry.value
        raise KeyError(f"Cannot find key {key}.")

    def remove(self, key):
        i_bucket = hash(key) % self._n_buckets
        for entry in self._L[i_bucket]:
            if entry.key == key:
                value = entry.value
                self._L[i_bucket].remove(entry)
                self._len -=1

                alpha = len(self) / self._n_buckets < self._min_alpha
                if alpha < self._min_alpha and self._n_buckets // 2 >= self._min_buckets:
                    self.rehash(new_buckets=self._n_buckets // 2)
                


                return value
        
        raise KeyError(f"Cannot find key {key}.")
        
                

    def rehash(self, new_buckets):
        self._n_buckets = new_buckets
        new_L = [[] for _ in range(self._n_buckets)]
        for bucket in self._L:
            for entry in bucket:
                i_bucket = hash(entry.key) % self._n_buckets
                new_L[i_bucket].append(entry)
        
        self._L = new_L