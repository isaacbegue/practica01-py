from Classes.Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, size, color, race, id):
        super().__init__(name, age)
        self.size = size
        self.color = color
        self.race = race
        self.__id = id
    def printInfo(self):
        self.getName()
        self.getAge()
        print(self.size, self.color, self.race, self.__id)