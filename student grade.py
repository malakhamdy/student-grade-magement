students = {}
while True:
    name = input("Enter your name: ")
    if name == "done":
        break
    grade = float(input("Enter your grade: "))
    students[name] = grade

for name, grade in students.items():
    print(name, ':', grade)


def avg():
    total = sum(students.values())  
    average = total / len(students)  
    print("Average grade:", average)

avg()

def max_grade():
    max_grade = max(students.values()) 
    print("Maximum grade:", max_grade)
    
max_grade()


def min_grade():
    min_grade = min(students.values()) 
    print("minmum grade:", min_grade)
    
min_grade()

def grads():
    grads = list(students.values())
    print("grades:", grads)
    
grads()

print(len(students))