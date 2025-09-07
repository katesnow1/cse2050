jake = ["jake", ['CSE2050', 'CSE3100']]
rachel = ["rachel",['CSE2050', 'CSE3666']]
marco = ["marco", 3.3, ['CSE1010']]
print(f"{jake[0]} is teaching {jake[1]}")
jake = {'name':'jake', 'courses':['CSE2050', 'CSE3100']}
print(f"{jake['name']} is teaching {jake['courses']}")

class Person:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

jake = Person('jake', ['CSE2050', 'CSE3100'])
print(f"{jake.name} is teaching {jake.courses}")
rachel = Person('rachel', ['CSE2050', 'CSE3100'])