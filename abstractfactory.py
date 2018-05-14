'''
Creatonal -> Abstract Factory
'''
class Dog:
    '''One object to be returned'''
    def speak(self):
        return 'Woof'
    def __str__(self):
        return 'Dog'
    
class DogFactory:
    '''Concrate Factory'''
    def get_pet(self):
        return Dog()
    def get_food(self):
        return 'Dog Food'
    
class PetStore:
    def __init__(self,pet_factory=None):
        self._pet_factory = pet_factory
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print('our pet is {} '.format(pet))
        print('our pet says {} '.format(pet.speak()))
        print('its food is {} '.format(pet_food))
        
#Create the concrate factory
factory = DogFactory()
shop = PetStore(factory)
shop.show_pet()

