def add(*args):
    return sum(args)


def subtract(*args):
    result = args[0]
    for number in args[1:]:
        result -= number
    return result

def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result


def divide(*args):
    result = args[0]
    for number in args[1:]:
        result /= number
    return result

#37
print(add(10, 2, 5, 20))
#3
print(subtract(10, 2, 4, 1))
#120
print(multiply(10, 2, 3, 2))
#1
print(divide(10, 2, 5))

first, last = input("What is your full name? \n").split()
print(f"Nice to meet you, {first}.")


def turn_to_string(*args):
    result = ""
    for letter in args:
        result += letter
    return result


def hey():
    return 'hey'

h, e, y = hey()

print(h)
print(e)
print(y)

print(turn_to_string(h, e, y))
