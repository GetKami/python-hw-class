class Animals:
    nickname = 'Кличка'
    weight = 0
    color = 'Цвет'
    fullness = False
    voice = 'Голос'
    product = 0

    def __init__(self, nickname, weight, color):
        self.nickname = nickname
        self.weight = weight
        self.color = color

    def food(self, food_volume):
        self.fullness = True

    def take_product(self, sum_product):
        self.product -= sum_product


class Goose(Animals):
    voice = 'Га-га'
    product = 2

class Cow(Animals):
    voice = 'Муууу'
    product = 18

class Sheep(Animals):
    voice = 'Бееее'
    product = 1.2

class Chiken(Animals):
    voice = 'Ко-ко-ко'
    product = 6

class Goat(Animals):
    voice = 'Мееее'
    product = 4

class Duck(Animals):
    voice = 'Кря'
    product = 3

goose_one = Goose('Серый', 2, 'Светло-серый')
goose_two = Goose('Белый', 5, 'Беленький')
cow_solo = Cow('Манька', 96, 'Коричневый')
sheep_one = Sheep('Барашек', 44, 'Серый')
sheep_two = Sheep('Кудрявый', 54, 'Черный')
chiken_one = Chiken('Ко-Ко', 2.5, 'Рыжий')
chiken_two = Chiken('Кукареку', 2.8, 'Черно-белый')
goat_one = Goat('Рога', 33, 'Белоснежный')
goat_two = Goat('Копыта', 38, 'Бежевый')
duck_solo = Duck('Кряква', 2, 'Черно-Коричневая')

goose_one.food(6)
goose_two.food(5)
cow_solo.food(34)
sheep_one.food(8)
sheep_two.food(9)
chiken_one.food(3)
chiken_two.food(2)
goat_one.food(4)
goat_two.food(6)
duck_solo.food(2)

goose_one.take_product(3)
goose_two.take_product(2)
cow_solo.take_product(32)
sheep_one.take_product(1)
sheep_two.take_product(2)
chiken_one.take_product(3)
chiken_two.take_product(4)
goat_one.take_product(19)
goat_two.take_product(12)
duck_solo.take_product(5)

animals_list = [goose_one, goose_two, cow_solo, sheep_one, sheep_two, chiken_one, chiken_two, goat_one, goat_two, duck_solo]

all_weight = 0
max_weight = 0
heavy_animal = str()
for animal in animals_list:
  all_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    heavy_animal = animal.nickname

print('Общий вес животных на ферме Дяди Джо - {} кг'.format(all_weight))
print('Самая тяжелая {} - весит {} кг.'.format(heavy_animal, max_weight))