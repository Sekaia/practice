def print_student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_student(name="Bobby Hill", school="Sunset High School", grade=10, gpa=2.3)

teacher = {
    'first_name': 'Hank',
    'last_name': 'Hill',
    'school': 'Sunset High',
    'subject': 'History'
}

def print_teacher(first_name, last_name, school, subject):
    print(first_name, last_name)
    print(school)
    print(subject)

print_teacher(**teacher)