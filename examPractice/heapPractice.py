class Entry():
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __le__(self, other):
        return self.priority <= other.priority

class Heap():
    def __init__(self, entries):
        self._idx = {}
        if entries:
            self._L = entries
            n = len(self) - 1
            for i in range(n, n//2, -1):
                self._idx[self._L[i].item] = i
            
            for i in range(n//2, -1, -1):
                self._idx[self._L[i].item] = i
                self.downheap(i)
        else:
            self._L = []

    def __len__(self):
        return len(self._L)

    def add(self, priority, item):
        self._L.append(Entry(priority, item))
        self._idx[item] = len(self) - 1
        self._L.upheap(len(self) - 1)

    def downheap(self, idx):
        imin = self.min_child(idx)
        while imin and self._L[idx] > self._L[imin]:
            self._swap(imin, idx)
            idx = imin
            imin = self.min_child(idx)


    def upheap(self, idx):
        i_p = self.i_parent(idx)
        while i_p and self._L[idx] < self._L[i_p]:
            self._swap(i_p, idx)
            idx = i_p
            i_p = self.i_parent(idx)

    def i_parent(self, idx):
        if idx == 0:
            return None
        else:
            return (idx-1)//2

    def i_right(self, idx):
        ir = idx * 2 + 2
        return ir if ir < len(self) else None

    def i_left(self, idx):
        il = idx * 2 + 1
        return il if il < len(self) else None

    def remove_min(self):
        item = self._L[0].item
        self._swap(0, len(self) - 1)
        self._L.pop()
        self.downheap(0)
        return item

    def min_child(self, idx):
        il = self.i_left(idx)
        ir = self.i_right(idx)
        if il is None:
            return None
        elif ir is None:
            return il
        else: return il if self._L[il] <= self._L[ir] else ir

    def _swap(self, i, j):
        self._L[i], self._L[j] = self._L[j], self._L[i]
        i_item = self._L[i].item
        j_item = self._L[j].item
        self._idx[i_item],  self._idx[j_item] = self._idx[j_item], self._idx[i_item]


    def change_priority(self, item, new_priority):
        idx = self._idx[item]
        self._L[idx].priority = new_priority
        self.upheap(idx)
        self.downheap(idx)