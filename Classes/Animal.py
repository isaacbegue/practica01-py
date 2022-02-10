class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getName(self):
        print(self.__name, end=" ")
    def getAge(self):
        print(self.__age, end=" ")
    def eat(self):
        print('eating...')