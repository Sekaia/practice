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

# class
class Monkey:
    def __init__(self, tail, arms, legs, age, type="Tamarin"):
        self.tail = tail
        self.arms = arms
        self.legs = legs
        self.age = age
        self.type = type
        self.is_hungry = True

    def __str__(self):
        return f"{self.age} year old {self.type}"

    def __eq__(self, other):
        return self.type == other.type and self.age == other.age

    #method
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

class Jungle:
    def __init__(self):
        self.monkeys = []

    def __iter__(self):
        yield from self.monkeys

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

#instantiating instances
bobo = Monkey(True, 2, 2, 3)
taburi = Monkey(False, 0, 4, 18, "Lion-tailed macaque")
maburi = Monkey(True, 2, 2, 18, "Lion-tailed macaque")
kaburi = Monkey(False, 0, 4, 28, "Black Howler")
laburi = Monkey(True, 2, 2, 30, "Mandrill")
monkey_jungle = Jungle()

monkey_jungle.add_monkey(bobo)
monkey_jungle.add_monkey(taburi)
monkey_jungle.add_monkey(maburi)
monkey_jungle.add_monkey(kaburi)
monkey_jungle.add_monkey(laburi)


bobo.speak()
taburi.steal("banana")
bobo.climb(100)
taburi.climb(10)
bobo.eat("banana")
taburi.eat("human")
bobo.eat("taburi")

print(bobo)
print(taburi)

for monkey in monkey_jungle:
    print(monkey)

if taburi == maburi:
    print("equal")
else:
    print("not equal")


