class Animal:
    def __init__(self, name, species="animal", sound="hi"):
        """Constructor class for Animal, takes params name, species, and sound"""
        self.name = name
        self.species = species
        self.sound = sound
    def speak(self):
        """returns name and species with its sound"""
        return f"{self.name}, a {self.species}, says {self.sound}!"
    def __repr__(self):
        """returns string representation of object with name, species, and sound"""
        return f"Animal({self.name}, {self.species}, {self.sound})"
    

class Dog(Animal):
    def __init__(self, name, is_good_boy = True):
        """constructor class for dog, takes params name and is_good_boy"""
        super().__init__(name, "dog", "ruff")
        self.is_good_boy = is_good_boy
    def __repr__(self):
        """returns string representation of object with name"""
        return f"Dog({self.name})"

class Cat(Animal):
    def __repr__(self):
        """returns string represenation of object with name, species, and sound"""
        return f"Cat({self.name}, {self.species}, {self.sound})"