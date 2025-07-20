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


"""
EXTRA ------------------------------------------------------------------------------------
"""

class Employee:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name= name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está cordinando todos los proyectos de la empresa.")

class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando el  proyecto de {self.project}")

class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language= language
    
    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá"
        )
    
    def print_employees(self):
        print ("Ningún empleado")

# Añadir las descripciones

my_manager = Manager(1, "CristianDev")
my_project_manager = ProjectManager(2, "Jorge", "Pagina Web")
my_project_manager2 = ProjectManager(3, "Anyelina", "Software contable")
my_programmer = Programmer(4, "Luis", "Java")
my_programmer2 = Programmer(5, "Ana", "Python")
my_programmer3 = Programmer(6, "Carlos", "JavaScript")
my_programmer4 = Programmer(7, "Maria", "C++")

# Añadir empleados al cargo de superiores

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2) # Ejemplo de error, no se añadirá

# Indicar las funciones que ejecuta cada empleado

my_manager.coordinate_projects()
my_project_manager.coordinate_project()
my_project_manager2.coordinate_project()
my_programmer.code()
my_programmer2.code()
my_programmer3.code()
my_programmer4.code()

# Imprimir los empleados de cada superior


print(f"{my_manager.name} tiene a su cargo a: "), {my_manager.print_employees()}
print(f"{my_project_manager.name} tiene a su cargo a: "), {my_project_manager.print_employees()}
print(f"{my_project_manager2.name} tiene a su cargo a: "), {my_project_manager2.print_employees()}
print(f"{my_programmer.name} tiene a su cargo a: "), {my_programmer.print_employees()}