#checking if a candidate is eligible for appearing UPSC exams?
name = input("enter your name :")
age = int(input("enter your age :"))

if age >= 21:
    print("you are eligible for the exam")
elif age < 32:
    print("your eligibility has gone!")
else:
    print("you are not eligible for the exam")