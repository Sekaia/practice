# monkey

# properties:
# tail
# 2 arms
# 2 legs

# behaviors:
# makes monkey sounds
# climbs trees
# eats bananas
# steals things

class Monkey:
    def __init__(self, tail, arms, legs, type="Tamarin"):
        self.tail = tail
        self.arms = arms
        self.legs = legs
        self.type = type
        self.is_hungry = True

    def speak(self):
        print("Ooo oo ah ah!")

    def steal(self, item):
        print(f"Monkey has stolen {item}!")

    def climb(self, height):
        if height >= 20:
            print("Monkey climbed a really high tree!")
        else:
            print("Monkey climbed a small tree")

    def eat(self, item):
        if self.is_hungry:
            if item == "banana":
                print("Monkey love you forever..")
                self.is_hungry = False
            else:
                print("Yum! Monkey full..")
                self.is_hungry = False
        else:
            print("Monkey not hungry.. yet..")


bobo = Monkey(True, 2, 2)
taburi = Monkey(False, 0, 4, "Gorilla")

bobo.speak()
taburi.steal("banana")
bobo.climb(100)
taburi.climb(10)
bobo.eat("banana")
taburi.eat("human")
bobo.eat("taburi")



