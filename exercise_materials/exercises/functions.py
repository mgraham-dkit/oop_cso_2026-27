def calc_average(marks):
    total =sum(marks)
    return f"{total/len(marks):.2f}"

def add_mark(student_dict, new_mark):
    student_dict["marks"].append(new_mark)

def find_student(student_list,student_name):
    for student in student_list:
        if student["name"] == student_name:
            return student

    return None

if __name__ == "__main__":
    students = [
        {"name": "Evan", "marks": [65, 72, 81]},
        {"name": "Caleb", "marks": [45, 51, 48]},
        {"name": "Angelo", "marks": [82, 77, 91]},
        {"name": "Dorothy", "marks": [55, 63, 59]}
    ]

    for student in students:
        print(f"{student["name"]} is {calc_average(student["marks"])}")

    print(f"Caleb's average mark: {calc_average(students[1]["marks"])}%")

    caleb = find_student(students,"Caleb")
    if caleb is not None:
        print(f"Calebs average mark is {calc_average(caleb["marks"])}%")
    else:
        print("Caleb was not found in the student list")

    print("Students with an average of 50% or higher:")
    for student in students:
        if float(calc_average(student["marks"])) >= 50:
            print(f"{student["name"]}")


    print("Add 66 to Dorothy:")
    dorothy = find_student(students, "Dorothy")
    if dorothy is not None:
        add_mark(dorothy, 66)
        print(f"Dorothy's marks are now: {dorothy["marks"]}")
        print(f"Dorothy's average is now: {calc_average(dorothy["marks"])}")
    else:
        print("Dorothy was not found in this student list")
