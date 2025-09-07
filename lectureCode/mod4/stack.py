class Stack:
    # Wrapper pattern
    # Wrapping the list in a different
    def __init__(self):
        """Initializes an empty stack"""
        self._L = []

    def push(self, item): 
        """Adds item to top of stack"""
        #self._L.append(item) #O(1)
        self._L.insert(0, item) #O(n)


    def pop(self):
        """Removes and returns top item from stack"""
        #return self._L.pop() #O(1)
        return self._L.pop(0) #O(n)

    
    def peek(self):
        """Returns (but does not remove) top item"""
        if len(self) == 0:
            raise IndexError("Cannot peek from empty Stack")
        #return self._L[-1]
        return self._L[0]

    
    def __len__(self):
        """Returns number of items in stack"""
        return len(self._L)

    
    def is_empty(self): 
        """Returns True iff stack is empty"""
        return len(self) == 0

        