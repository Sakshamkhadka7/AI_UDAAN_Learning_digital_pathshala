def greet(name):
    print("Hello ",name)

greet("Saksham Khadka")


def add(num1,num2):
    return num1 + num2

sum=add(1,2)
print(sum)

def student():
    return "Saksham" , 20 , "Birgunj"

name,age,location=student()
print(name)


def square_num(num):
    return num*num

result=square_num(5)

result2=lambda num:num*num
print(result2(10))