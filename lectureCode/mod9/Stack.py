class Stack:
    def __init__(self): self._L = []

    def __len__(self) : return len(self._L)

    def push(self, item): self._L.append(item)

    def pop(self): return self._L.pop()

    def __iter__(self):
        while len(self) > 0:
            yield self.pop()
        #return None


if __name__ == '__main__':
    n = 5
    s = Stack()
    for i in range(n):
        s.push(i)


    for item in s:
        print(item)