class Entry:
    def __init__(self, priority, value):
        """Instantiates a new entry object"""
        self.priority = priority
        self.value = value

    def __eq__(self, other):
        """Entries are equal if their priorities are equal"""
        return self.priority == other.priority

    def __lt__(self, other):
        """Entries are compared based on priority"""
        return self.priority < other.priority
    
    def __le__(self, other):
        """Entries are compared based on priority"""
        return self.priority <= other.priority

    def __repr__(self):
        """Returns string representation of Entry"""
        return f"Entry({self.priority}, {self.value})"
    
class Heap:
    def __init__(self):
        """Instantiates a new, empty heap"""
        self._L = []

    def __len__(self):
        """Returns number of entries in heap"""
        return len(self._L)

    def insert(self, item, priority):
        """Adds item w/ given priority to heap"""
        self._L.append(Entry(priority = priority, value = item))
        self._upheap(idx=len(self) - 1)


    def remove_min(self):
        """Removes and returns entry with minimum priority"""
        # extract item to return later
        entry = self._L

        # move last item to top of heap, then pop last item in array
        self._swap(0, len(self)-1)
        self._L.pop()

        # downheap until heap-ordered
        self._downheap(idx=0)

        return entry



    def _upheap(self, idx):
        """Upheaps item at idx until heap is heap-ordered"""
        i_p = self._parent(idx)

        #until heap is heap-ordered
        while i_p is not None and self._L[idx] < self._L[i_p]:
            self._swap(idx, i_p)
            idx = i_p
            i_p = self._parent(idx)

    def _downheap(self, idx):
        """Downheaps item at idx until heap is heap-ordered"""
        idx_min = self._min_child(idx)

        while idx_min is not None and self._L[idx] > self._L[idx_min]:
            self._swap(idx, idx_min)
            idx = idx_min
            idx_min = self._min_child(idx)

    def _parent(self, idx):
        """Returns index of parent"""
        return (idx - 1) // 2 if idx else None

    def _left(self, idx):
        """Returns index of left child or None"""
        i_l = 2*idx + 1
        return i_l if  i_l < len(self) else None

    def _right(self, idx):
        """Returns index of right child or None"""
        i_r = 2*idx + 2
        return i_r if i_r < len(self) else None

    def _min_child(self, idx):
        """Returns index of minimum child or None"""
        idx_left, idx_right = self._left(idx), self._right(idx)
        if idx_left is None: return None
        elif idx_right is None: return idx_left
        else: 
            return idx_left if self._L[idx_left] <= self._L[idx_right] else idx_right 

    def _swap(self, i, j):
        """Swaps items at given indices in heap"""
        self._L[i], self._L[j] = self._L[j], self._L[i]

    def __iter__(self):
        """Iteratively removes every item in heap"""

if __name__ == '__main__':
    priorities = [19, 36, 8, 82, 66, 55, 87, 2, 51, 58, 4, 21, 29, 1, 50]

    h = Heap()
    for priority in priorities:
        h.insert(item=0, priority=priority)
    print(h._L)

    for _ in range(len(priorities)):
        print(h.remove_min())