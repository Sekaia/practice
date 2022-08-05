# find any intersecting elements in the list

a = [1, 3, 5, 7, 9]
b = [2, 4, 5, 8, 9]

def find_intersecting(list_1, list_2):
    result = []
    for number in list_1:
        if number in list_2:
            result.append(number)
    return result

def find_intersect(list_1, list_2):
    return list(set(list_1).intersection(set(list_2)))

print(find_intersecting(a, b))

print(find_intersect(a, b))