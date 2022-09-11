data = input()
courses = {}

while not data == "end":
    course_name, student_name = data.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    data = input()
# sorted_courses = sorted(courses.items(), key=lambda kvpt: len(kvpt[1]), reverse=True)
# sorted_courses = sorted(courses.items(), key=lambda kvpt: -len(kvpt[1]))
# sorted_courses = sorted(courses.items())
sorted_courses = courses.items()
# print(sorted_courses)
for course_name, students in sorted_courses:
    print(f"{course_name}: {len(students)}")
    # for name in sorted(students):
    for name in students:
        print(f"-- {name}")
