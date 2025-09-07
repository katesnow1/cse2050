from process import Process

class CircularQueue:
    """A circular queue to allow us to run processes turn-by-turn"""
    def __init__(self, processes=None):
        """Initializes a CircularQueue and adds processes to it"""
        self._d_processes = {}
        self._head = None
        if processes is not None:
            for process in processes:
                self.add_process(process)
    def __len__(self):
        """Returns length of the CircularQueue"""
        return len(self._d_processes)
    
    def __repr__(self):
        """returns the string representation of a circularqueue object"""
        # create a list of the string representations of each node
        strNodes = []
        curr = self._head
        for _ in range(len(self)):
            strNodes.append(repr(curr))
            curr = curr.link
        return f"CircularQueue({', '.join(strNodes)})"
    
    def add_process(self, process):
        """Adds process to end of queue"""
        self._d_processes[process.pid] = process
        if self._head is None:
            process.link = process
            process.prev = process
            self._head = process
            
        else:
            process.link = self._head
            process.prev = self._head.prev
            self._head.prev.link = process
            self._head.prev = process

    def remove_process(self, process):
        """Removes a specific process from the circular queue"""
        if len(self) == 0:
            raise RuntimeError("Can't remove from Circular Queue")
        elif len(self) == 1:
            self._head = None
        else:
            process.link.prev = process.prev
            process.prev.link = process.link
            if process is self._head: self._head = process.link

        del self._d_processes[process.pid]
        return process

    def kill(self, pid):
        if pid not in self._d_processes:
            raise RuntimeError("Process is not in Circular Queue")
        return self.remove_process(self._d_processes[pid])
    
    def run(self, n_cycles):
        """Runs circular queue for n_cycles, giving each process 1 cycle at a time"""
        n_remaining = n_cycles
        return_strings = []   # Using an intermediate list since appending to a string is O(n)

        while n_remaining:
            self._head.cycles -= 1

            if self._head.cycles == 0:
                return_strings.append(f"{self._head.pid} finished after {n_cycles-n_remaining+1} computational cycles.")
                self.remove_process(self._head)

            else:
                self._head = self._head.link
            
            n_remaining -= 1

        return '\n'.join(return_strings)
    

