students = [
{"name": "Annie", "average_mark": 55},
{"name": "Aine", "average_mark": 39},
{"name": "Mira", "average_mark": 66},
{"name": "Dan", "average_mark": 47}
]

for i in range(len(students)):
    print(f"Student Name: {students[i]["name"]}")
    print(f"Student Marks: {students[i]["average_mark"]}")
for student_dict in students:
    if student_dict["name"] == "Dan":
        print(f"Dans average mark: {student_dict["average_mark"]}")

for student in students:
    if student["average_mark"] >= 50:
        print(student["name"])

max_mark = -1
name = None
for i in range(len(students)):
    if students[i]["average_mark"] > max_mark:
        max_mark = students[i]["average_mark"]
        name = students[i]["name"]

print(f"Max mark {max_mark} was {name}")