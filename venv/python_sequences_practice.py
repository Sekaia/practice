groceries = ["eggs", "milk", "cereal", "turkey", "pudding", "pickles"]
# iterating with basic for loops


for item in groceries:
    print(item)

# iterating with enumerate

# this is still a bit confusing for me, need to practice a bit more
for index, item in enumerate(groceries, 1):
    print(f"{index}. {item}")