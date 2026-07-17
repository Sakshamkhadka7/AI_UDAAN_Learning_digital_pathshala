print("Welcome to DPLMS Student Registration System")

courses=("Python with AI/ML","JavaScript","Flutter","MERN Stack")



name=input("Enter your name : ")
email=input("Enter your email :")
age=input("Enter your age : ")
selected_course=input("Select the course : ")

student_info={
    "name":name,
    "email":email,
    "age":age,
    "course":selected_course
}



found=False

for course in courses:
    if selected_course == course :
        found=True
        break

if found:
    print("registration successfully")
else :
    print("Not available course")

print(student_info)

