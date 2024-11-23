from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed = 1

    def __init__(self, speed=1):
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + (dz * self.speed)

        if new_z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_eggs = randint(1, 4)
        verb = "is" if num_eggs == 1 else "are"
        message = f"Here {verb} {num_eggs} eggs for you."
        print(message)


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_speed = self.speed // 2
        new_z = self._cords[2] - (dz * new_speed)

        if new_z >= 0:
            self._cords[2] = new_z
        else:
            self._cords[2] = 0


class PoisonousAnimal(AquaticAnimal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()


db.lay_eggs()











