students=int(input("Enter number of students: "))

StuGrades_list=[]
student_data={}


def student(name):
    name=input(f"Enter name of student {x} : ")
    grade=float(input(f"Enter grade of student {name}: "))
    student_data[name]=grade
    return name,grade

for x in range(1,students+1):
  student_name,student_grade=student(x)
  StuGrades_list.append(student_grade)


avg=sum(StuGrades_list)/students
print("Average grade: ",avg)

above_avg=[name for name, grade in student_data.items() if grade > avg]
print("Students above average: ",above_avg)

top_student_name=max(student_data, key=student_data.get)
top_student_grade = student_data[top_student_name]
print("Top student: ", top_student_name, " with ", top_student_grade)
