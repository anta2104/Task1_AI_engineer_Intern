import random
import string

classes = ["K66CB", "K67NN", "K77CB", "K65CB"]
students = []

names = set()

while len(students) < 1000000:
    student_id = str(len(students)+1).zfill(2)
    name = ""
    while name == "" or name in names:
        name_length = random.randint(4, 10)
        name = ''.join(random.choice(string.ascii_uppercase) for _ in range(name_length))
    names.add(name)
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    phone = str(random.randint(1000000, 9999999)).zfill(7)
    class_code = random.choice(classes)
    student = "|".join([student_id, name, month+"/"+day, phone, class_code])
    students.append(student)

students_data = "\n".join(students)

# Write data to file
with open("students_data.txt", "w") as f:
    f.write(students_data)