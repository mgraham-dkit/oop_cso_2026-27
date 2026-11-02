def add_mark(student_dict,new_mark):
    student_dict["marks"].append(new_mark)


if __name__ == "__main__":
    students = [
        {"name": "Evan", "marks": [65, 72, 81]},
        {"name": "Caleb", "marks": [45, 51, 48]},
        {"name": "Angelo", "marks": [82, 77, 91]},
        {"name": "Dorothy", "marks": [55, 63, 59]}
    ]


    print("Adding 66 to Caleb mark")
    for student in students:
        if student["name"] == "Caleb":
            add_mark(student,66)

    print(students)