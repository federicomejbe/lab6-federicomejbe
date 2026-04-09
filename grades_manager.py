
def initialize_dict(student_name, subject_grades):
    result = {}
    result[student_name] = subject_grades
    return result

def add_student(student_grades):
    name = input("Enter student name: ")
    name = name.title()
    subjects = {}
    entry = input("Enter subject and grade (or 'exit' to finish): ")
    while entry.lower() != "exit":
        parts = entry.split(",")
        subject = parts[0].title()
        grade = float(parts[1])
        subjects[subject] = grade
        entry = input("Enter subject and grade (or 'exit' to finish): ")
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    result = {}
    for name in keys:
        encontrado = False
        for student in student_grades:
            if student.lower() == name.lower():
                result[student] = student_grades[student]
                encontrado = True
        if not encontrado:
            print(name.title(), "not found!")
    return result

def avg_by_student(student_grades, keys=None):
    if keys is None:
        for student in student_grades:
            grades = student_grades[student]
            total = 0
            count = 0
            for g in grades:
                total = total + grades[g]
                count = count + 1
            promedio = round(total / count, 1)
            print(student + ":", promedio)
    else:
        result = get_students(student_grades, keys)
        for student in result:
            grades = result[student]
            total = 0
            count = 0
            for g in grades:
                total = total + grades[g]
                count = count + 1
            promedio = round(total / count, 1)
            print(student + ":", promedio)

