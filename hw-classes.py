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

    def __add__(self, other):
        return self.weight + other

    def take_product(self, sum_product):
        self.product -= sum_product


class goose(Animals):
    voice = 'Га-га'
    product = 2

class cow(Animals):
    voice = 'Муууу'
    product = 18

class sheep(Animals):
    voice = 'Бееее'
    product = 1.2

class chiken(Animals):
    voice = 'Ко-ко-ко'
    product = 6

class goat(Animals):
    voice = 'Мееее'
    product = 4

class duck(Animals):
    voice = 'Кря'
    product = 3

goose_one = goose('Серый', 2, 'Светло-серый')
goose_two = goose('Белый', 5, 'Беленький')
cow_solo = cow('Манька', 96, 'Коричневый')
sheep_one = sheep('Барашек', 44, 'Серый')
sheep_two = sheep('Кудрявый', 54, 'Черный')
chiken_one = chiken('Ко-Ко', 2.5, 'Рыжий')
chiken_two = chiken('Кукареку', 2.8, 'Черно-белый')
goat_one = goat('Рога', 33, 'Белоснежный')
goat_two = goat('Копыта', 38, 'Бежевый')
duck_solo = duck('Кряква', 2, 'Черно-Коричневая')

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