mport random
# 1.    Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
# Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
# Представитель каждого класса может умереть, если достигнет определенного возраста
# или для него не будет еды. Напишите виртуальные методы поедания и определения
# состояния живого существа (живой или нет, в зависимости от достижения
# предельного возраста и наличия еды (входной параметр)).
class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)


class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr

    def grown(self):
        self.count *= self.koef_repr

    def info(self):
        print("count plants:", self.count)

    def rabbits_food(self,count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self,count_plants):
        self.count += count_plants

    def cold_summer(day=70, temper=21):
        if day < 60 or temper < 20:
            self.koef_repr *= 0.8


class Rabbits(Alive):
    def __init__(self, koef_repr,koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count rabbits:", self.count)

    def take_away(self,count_rabbits):
        self.count -= count_rabbits

    def foxes_food(self, count_fox):
        self.count -= count_fox * 20

    def add_rabbits(self, count_rabbits):
        self.count += count_rabbits


class Foxes(Alive):
    def __init__(self, koef_repr,koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def info(self):
        print("count foxes:", self.count)

    def take_away(self,count_fox):
        self.count -= count_fox

    def hunting_season():
        if True:
            self.koef_death *= 1.2
        else:
            self.koef_death *= 0.8





plants = Plants(10, 300)
rabbits = Rabbits(5,0.2,70)
fox = Foxes(2, 0.1, 30)

year = 1
print("begin:")
plants.info()
rabbits.info()
fox.info()


while year <= 10:


    if plants.count // 10  <= rabbits.count:
        print("warning!!!!!!!")
        print("plants is very low")
        rabbits.info()
        plants.info()
        choise = int(input("enter 1 - add plants 2 - take away rabbits"))
        if choise == 1:
            count = int(input("enter count plants:"))
            plants.add_plants(count)
        elif choise == 2:
            count = int(input("enter count rabbits:"))
            rabbits.take_away(count)

    if rabbits.count // 5  <= fox.count:
        print("warning!!!!!!!")
        print("rabbits is very low")
        rabbits.info()
        fox.info()
    choise = int(input("enter 1 - add rabbits 2 - take away foxes"))
    if choise == 1:
        count = int(input("enter count rabbits:"))
        rabbits.add_rabbits(count)
    elif choise == 2:
        count = int(input("enter count foxes:"))
        fox.take_away(count)


    if plants.count <= 0 or rabbits.count <= 0 or fox.count <= 0:
        print("Fatality on year:",year)
        print("All our alive is death")
        break
    plants.cold_summer(70, 17)

    plants.grown()
    plants.rabbits_food(rabbits.count)

    rabbits.death()
    rabbits.reproduction()
    rabbits.foxes_food(fox.count)

    fox.hunting_season()
    fox.death()
    fox.reproduction()


    print("year: ", year)

    plants.info()
    rabbits.info()
    fox.info()

    year += 1