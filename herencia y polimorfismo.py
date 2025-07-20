"""
Ejercicio de herencia y polimorfismo en Python.
"""

#Superclase

class Animal:
    def __init__ (self, name: str):
        self.name = name 
    
    def sound(self):
        pass    # Método que será sobreescrito por las subclases 

#Subclases

class Cat(Animal):
    def sound(self):
        print ("Meow!")

class Dog(Animal):
    def sound(self):
        print ("Woof!")
    def specie(self):
        return "lobo ciberiano"
    
    
def print_sound(animal: Animal):
    animal.sound()

my_pet = Animal("Generic Animal")
my_pet.sound()    
my_cat = Cat("Pelusa")
#print(my_cat.name, "hace:", my_cat.sound()) --> funciona con return
print_sound(my_cat) # eliminar esta linea si usa return en lugar de print en la función
my_dog = Dog("Firulais") 
#print(my_dog.name, "hace:", my_dog.sound(), "y es un", my_dog.specie()) --> funciona con return
print_sound(my_dog) # eliminar esta linea si usa return en lugar de print en la función
