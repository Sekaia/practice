class student:
    def __init__(self, first, last, age, gpa, courses, school):
        student.self = self
        student.first = first
        student.last = last
        student.age = age
        student.gpa = gpa
        student.courses = courses
        student.school = school
        student.email = first + '.' + last + "@student." + school + ".edu"

student1 = student("Henry", "Smith", 17, 3.2, ["Math", "History", "Biology", "Art", "Spanish", "Economics"], "Raven High")
