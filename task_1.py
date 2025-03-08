class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        if self.species == 'cat':
            print(f'{self.name} каже Мяу')
        elif self.species == 'dog':
            print(f'{self.name} каже Гав')
        else:
            print(f'{self.name} каже Муууу')


cat = Animal("Жучка", "cat", 24)
dog = Animal("Мурка", "dog", 25)
cow = Animal("Бурьонка", "cow", 4)
cat.make_sound()
dog.make_sound()
cow.make_sound()
