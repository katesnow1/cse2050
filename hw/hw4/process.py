class Process:
    def __init__(self, pid, cycles=100):
        """Initializes a process object"""
        self.pid = pid
        self.cycles = cycles
        self.link = None
        self.prev = None
    def __eq__(self, other):
        """Checks if the pids of processes in params are equal"""
        return self.pid == other.pid
    def __repr__(self):
        """Prints the string representation of the process object"""
        return f"Process({self.pid}, {self.cycles})"