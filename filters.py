grades = ["A", "B", "F", "C", "F", "A"]


def remove_fails(grade):
    return grade != "F"


# print(list(filter(remove_fails, grades)))

filtered_grades = []
for grade in grades:
    if grade != "F":
        filtered_grades.append(grade)
print(filtered_grades)
