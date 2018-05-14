'''
Type of design patterns:
1. Creational
 - Create objects in a systematic way
 - Felxible
 - Dominant OOP Mechanism: Polymorphism
2. Structural
 - Establish usuful relationships between componenets
 - Dominant OOP Mechanism: Inheritence
3. Behavioral
 - Best practices of objects interaction
 - Focus: Define protocols
 - Dominant OOP Mechanism: Methods and their signitures
'''

class Dog:
    def __init__(self,name):
        self._name = name
    def speak(self):
        return 'Woof'

class Cat:
    def __init__(self,name):
        self._name = name
    def speak(self):
        return 'moew'
    
def get_pet(pet='dog'):
    '''Factory Method'''
    pets = dict(dog=Dog('Hope'),cat=Cat('Cirmi'))
    return pets[pet]

    
print(get_pet('dog'))