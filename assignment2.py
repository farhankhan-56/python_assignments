# Part A
# question 1
for i in range (1,11):
    print(i)

# question 2
for i in range (1,21,1):
    print (i)

# question 3
word = 'python'

for char in word:
    print(char)

# question 4
for i in range (5,0,-1):
    print (i)

# quesion 5
i = 1
while i <= 5:
    print(i)
    i+=1

# Part B
# question 1
def greet():
    print ("Hello world")
greet()

# question 2
def num_print(a):
    print(f"the number is: {a}")

num = int(input("enter a number: "))
num_print(num)

# question 3
def add(a,b):
    print(f"the sum of {a} and {b} =",a+b)

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

add(num1,num2)

# question 4
def check(a):
    if a % 2==0:
        print("even")
    else:
        print("odd")

numb = int(input("Enter a number: "))
check(numb)

# question 5
def loop():
    for i in range (1,6):
        print(i)
loop()


# Mini project

def table_generator(a):
    i = 1
    while i <= 10:
        print (f"{a} x {i} =",a*i)
        i+= 1

num = int(input("enter number: "))
table_generator(num)