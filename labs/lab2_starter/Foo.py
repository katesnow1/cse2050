class Foo:
    def __init__(self, name, profession):
        """Constructor class for foo, takes in params name and profession"""
        self.name = name
        self.profession = profession

    def speak(self):
        """Returns string saying hello!"""
        return f"{self.name} says hello!"
    
    def __repr__(self):
        """Returns string representation of object, shows name and profession"""
        return f"Foo({self.name}, {self.profession})"
    
