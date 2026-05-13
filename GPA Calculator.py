# fuction 1: แปลงคะแนน -> เกรด
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
# fuction 2: คำนวณ GPA
def calculate_gpa(grades):
    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    total = 0

    for grade in grades:
     total += grade_points[grade] 

    gpa = total / len(grades) 
    return gpa

grades = []

subject = int(input("Number of subject: "))

for i in range(subject):
    subject_name = input("subject name: ")
    score = int(input("Type your score here: "))
    grade = get_grade(score)
    grades.append(grade)

gpa = calculate_gpa(grades)

print(gpa)
