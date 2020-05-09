class Animals:
    animal_list = {}
    def __init__(self, name, weight):
        self.food_status = 'Голодный'
        self.voice = 'Звуки неопределенного животного'
        self.name = name
        self.weight = weight
        Animals.animal_list[name] = weight

    def feed(self):
        if self.food_status == 'Голодный':
            print('Животное успешно накормлено')
            self.food_status = 'Сытый'
        else:
            print('Животное не голодно')

    def voice_recognition(self):
        if self.voice == 'Га-га-га':
            print('Это гусь')
        elif self.voice == 'Му-у':
            print('Это корова')
        elif self.voice == 'Бе-е':
            print('Это овца')
        elif self.voice == 'Ме-е':
            print('Это коза')
        elif self.voice == 'Ко-ко-ко':
            print('Это курица')
        elif self.voice == 'Кря-кря':
            print('Это утка')

    def weight_sum(self):
        print(sum(Animals.animal_list.values()))

    def weigh_most(self):
        print(list(Animals.animal_list.keys())[list(Animals.animal_list.values()).index(max(Animals.animal_list.values()))])


class Milk_Animals(Animals):
    def __init__(self, name, weight):
        super(Milk_Animals, self).__init__(name, weight)
        self.milk = 'Молоко есть'

    def milking(self):
        if self.milk == 'Молоко есть':
            print('Животное успешно подоено')
            self.milk = 'Молока нет'
        else:
            print(self.milk)


class Egg_Animals(Animals):
    def __init__(self, name, weight):
        super(Egg_Animals, self).__init__(name, weight)
        self.eggs = 'Яйца есть'

    def collecting_eggs(self):
        if self.eggs == 'Яйца есть':
            print('Яйца успешно собраны')
            self.eggs = 'Яиц нет'
        else:
            print(self.eggs)


class Goose(Egg_Animals, Animals):
    def __init__(self, name, weight):
        super(Goose, self).__init__(name, weight)
        self.voice = 'Га-га-га'


class Cow(Milk_Animals, Animals):
    def __init__(self, name, weight):
        super(Cow, self).__init__(name, weight)
        self.voice = 'Му-у'

class Sheep(Animals):
    def __init__(self, name, weight):
        super(Sheep, self).__init__(name, weight)
        self.voice = 'Бе-е'
        self.wool = 'Животное обросло'

    def wool_picking(self):
        if self.wool == 'Животное обросло':
            print('Стрижка прошла успешно')
            self.wool = 'Шерсти нет'
        else:
            print(self.wool)

class Goat(Milk_Animals, Animals):
    def __init__(self, name, weight):
        super(Goat, self).__init__(name, weight)
        self.voice = 'Ме-е'

class Hen(Egg_Animals, Animals):
    def __init__(self, name, weight):
        super(Hen, self).__init__(name, weight)
        self.voice = 'Ко-ко-ко'

class Duck(Egg_Animals, Animals):
    def __init__(self, name, weight):
        super(Duck, self).__init__(name, weight)
        self.voice = 'Кря-кря'


goose1 = Goose('Серый', 20)
goose1.feed()
goose1.collecting_eggs()


goose2 = Goose('Белый', 25)
goose2.feed()
goose2.collecting_eggs()


cow = Cow('Манька', 230)
cow.feed()
cow.milking()


sheep1 = Sheep('Барашек', 110)
sheep1.feed()
sheep1.wool_picking()


sheep2 = Sheep('Кудрявый', 95)
sheep2.feed()
sheep2.wool_picking()



hen1 = Hen('Ко-Ко', 8)
hen1.feed()
hen1.collecting_eggs()


hen2 = Hen('Кукареку', 11)
hen2.feed()
hen2.collecting_eggs()


goat1 = Goat('Рога', 83)
goat1.feed()
goat1.milking()


goat2 = Goat('Копытка', 87)
goat2.feed()
goat2.milking()

duck = Duck('Кряква', 19)
duck.feed()
duck.collecting_eggs()

duck.weight_sum()
duck.weigh_most()