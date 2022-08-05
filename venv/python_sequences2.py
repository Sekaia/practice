groceries = ["milk", "cereal", "turkey", "pudding", "pickles"]

print(groceries[1:4:2])
print("hello"[::-1])

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(len(nums))
print(max(nums))
print(min(nums))

string = "hello how are you doing on this lovely day"

print(len(string))
print(max(string))
print(min(string))

if 'eggs' not in groceries:
    print("You forgot the eggs!")
    groceries.append("eggs")
    print("I added them for you")
else:
    print("Wow! You remembered the eggs!")


print(string.count('l'))
print(string.index("doing"))
print(groceries.index("turkey"))

object1 = 1, 2, 3, 4, 5
object2 = 6, 7, 8, 9, 10

object1 = object1 + object2
print(object1)

print(string*10)