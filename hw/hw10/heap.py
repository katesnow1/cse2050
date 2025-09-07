from entry import Entry

class Heap:
    def __init__(self):
        """initlializes a heap object"""
        self._L = []
        self._idx = {}

    def __len__(self):
        """returns length of the heap"""
        return len(self._L)

    def __iter__(self):
        """yields minimum entry until heap is empty"""
        while self:
            yield self.remove_min()

    def idx_parent(self, idx):
        """returns index of parent node"""
        if idx == 0:
            return None
        else:
            return (idx - 1)//2

    def idx_left(self, idx):
        """returns index of left child node"""
        i_left = 2*idx + 1
        return i_left if  i_left < len(self) else None
    
    def idx_right(self, idx):
        """returns index of right child node"""
        i_right = 2*idx + 2
        return i_right if i_right < len(self) else None

    def idx_min_child(self, idx):
        """returns index of the child with minimum priority"""  
        i_left, i_right = self.idx_left(idx), self.idx_right(idx)
        if i_left is None: return None
        elif i_right is None: return i_left
        else: 
            return i_left if self._L[i_left] <= self._L[i_right] else i_right 
        
    def insert(self, item, priority):
        """adds a Entry object into the heap"""
        self._idx[item] = len(self)
        self._L.append(Entry(item, priority))
        self._upheap(idx=len(self)-1)
        #update index in the dictionary where ??? swap method ???

    def remove_min(self):
        """removes Entry object with least priority"""
        if len(self) == 0: raise IndexError("Cannot remove from empty heap")
        # extract item to return later
        entry = self._L[0] #might be just entry = self._L 

        # move last item to top of heap, then pop last item in array
        self._swap(0, len(self)-1)
        self._L.pop()

        # downheap until heap-ordered
        self._downheap(idx=0)

        self._idx.pop(entry.item)

        return entry

    def change_priority(self, item, priority):
        """updates the priority of the Entry to given priority in params"""
        #needs to access dictionary
        idx = self._idx[item]
        old_priority = self._L[idx].priority
        self._L[idx].priority = priority
        if priority < old_priority:
            self._upheap(idx)
        elif priority > old_priority:
            self._downheap(idx)
        new_idx = self._idx[item]
        return new_idx


    def _swap(self, i, j):
        """swaps two entries at specified indexes i and j"""
        self._L[i], self._L[j] = self._L[j], self._L[i]
        self._idx[self._L[j].item], self._idx[self._L[i].item] = j, i
        #update dicionary index here??? idk lol this part does not work

    def _upheap(self, idx):
        """moves Entry up in the heap until it is in its correct spot"""
        i_p = self.idx_parent(idx)

        #until heap is heap-ordered
        while i_p is not None and self._L[idx] < self._L[i_p]:
            self._swap(idx, i_p)
            idx = i_p
            i_p = self.idx_parent(idx)

    def _downheap(self, idx):
        """moves Entry down in the heap until it is in its correct spot"""
        idx_min = self.idx_min_child(idx)

        while idx_min is not None and self._L[idx] > self._L[idx_min]:
            self._swap(idx, idx_min)
            idx = idx_min
            idx_min = self.idx_min_child(idx)
    
    @staticmethod
    def heapify(entries):
        """creates and returns a heap out of a passed in list of Entry objects"""
        # hp = Heap()
        # for entry in entries:
        #     hp.insert(entry.item, entry.priority)
        # return hp
        #this is O(nlogn)

        #creates heap object and then downheapifies
        hp = Heap()
        hp._L = entries
        for i in range(len(entries)):
            hp._idx[entries[i].item] = i

        last_parent_idx = len(hp) // 2 - 1
        for i in range(last_parent_idx, -1, -1):
            hp._downheap(i)
        return hp



if __name__ == '__main__':
    a = Entry("a", 0)
    b = Entry("b", 4)
    c = Entry("c", 2)
    d = Entry("d", 1)
    entries = [a, b, c, d]
    hp = Heap.heapify(entries)
    print(hp._L)
    print(hp._idx)



