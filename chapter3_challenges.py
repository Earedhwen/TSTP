import random

x = random.randint(0,35)

if x<=10:
    print("x is less than or equal to 10")
elif x<=25:
    print("x is greater than 10 but less than or equal to 25")
else:
    print("x is greater than 25")

num1 = random.randint(50,200)
num2 = random.randint(1,50)

print("remainder is " + str(num1%num2))
print("quotient is " + str(num1//num2))

age = random.randint(0,120)

if age < 1:
    print("baby")
elif age < 3:
    print("toddler")
elif age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")
