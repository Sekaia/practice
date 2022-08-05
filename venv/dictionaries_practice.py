data = {
    'first_name':'Ben',
    'last_name':'Gillotte',
    'age':25
}

print(data['first_name'])

print(data.keys())
print(data.values())

data['age'] = 26

print(data["age"])

data['email'] = 'gillotte.bm@gmail.com'

print(data.keys())
print(data.values())

del(data['email'])

print(data.keys())
print(data.values())