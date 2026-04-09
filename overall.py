

def student_averages(students):
    result = {}
    for student in students:
        grades = students[student]
        total = 0
        count = 0
        for g in grades:
            total = total + grades[g]
            count = count + 1
        promedio = round(total / count)
        result[student] = promedio
    return result

def assignment_averages(students):
    result = {}

    for student in students:
        grades = students[student]
        for tarea in grades:
            if tarea not in result:
                result[tarea] = 0
            result[tarea] = result[tarea] + grades[tarea]
    for tarea in result:
        result[tarea] = round(result[tarea] / len(students))
    return result
    
