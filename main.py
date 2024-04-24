# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def make_sound(self):
        pass


    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Чирик-чирик")

    def eat(self):
        print("Я ем семена")

class Mammal(Animal):
    def make_sound(self):
        print("Мяу")

    def eat(self):
        print("Я ем рыбу")

class Reptile(Animal):
    def make_sound(self):
        print("Шшш")

    def eat(self):
        print("Я ем мух")

bird = Bird("воробей", 2)
mammal = Mammal("кот", 5)
reptile = Reptile("ящерица", 1)

animals = [bird, mammal, reptile]

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


def animal_eat(animals):
    for animal in animals:
        animal.eat()

class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)


class ZooKeeper:
    def feed_animal(self):
        print("Животные покормлены")


class Veterinarian:
    def heal_animal(self):
        print("Животные вылечены")


employee1 = ZooKeeper()
employee2 = Veterinarian()

my_zoo = Zoo()
my_zoo.add_employee(employee1)
my_zoo.add_animal(bird)
my_zoo.add_animal(mammal)
my_zoo.add_animal(reptile)
my_zoo.add_employee(employee2)

print(
    f"Животные в зоопарке: {my_zoo.animals[0].name}, {my_zoo.animals[1].name}, {my_zoo.animals[2].name}")
animal_sound(my_zoo.animals)
animal_eat(my_zoo.animals)
print(
    f"Сотрудники в зоопарке: {my_zoo.employees[0].__class__.__name__}, {my_zoo.employees[1].__class__.__name__}")
employee1.feed_animal()
employee2.heal_animal()

#добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки

