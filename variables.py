# Section A
# question 1
name = "farhan khan"
print (name)

# question 2
age = 20
height = 6.5
print(age,height)

# question 3
number = 50
print (type(number))

# question 4
is_student = True
print(is_student)

# question 5
num = input("enter a number: ")
print (num)

# Section B
# quesion 1
num1 = int(input("enter first number: "))
num2 = int(input("enter secind number: "))
print ("sum = ",num1 + num2)

# question 2
num3 = int(input("enter first number: "))
num4 = int(input("enter secind number: "))

if num3 > num4:
    print ("greater is: ",num3)
else:
    print ("greater is: ",num4)

# question 3
num5 = int(input("enter number: "))
if num5 % 2 == 0:
    print("even")
else:
    print("odd")

# question 4
marks = int(input("enter marks: "))
if marks >= 50:
    print("pass")
else:
    print("FAil")

# qustion 5
num6 = int(input("enter number: "))
if num6 < 10:
    print("smaller than 10")
elif num6 == 10:
    print ("equal to 10")
elif num6 > 10:
    print("greater than 10")

# Mini project

num_check = int(input("enter number: "))
if num_check == 0:
    print("number is zero")
elif num_check > 0:
    print("number is postive")
elif num_check < 0:
    print("number is negative")