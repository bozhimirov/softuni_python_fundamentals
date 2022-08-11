text = input()
courses = dict()

while ":" in text:

    data = text.split(":")
    name = data[0]
    ids = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][ids] = name

    text = input()

text = text.replace("_", " ")

for ids in courses[text]:
    print(f'{courses[text][ids]} - {ids}')
