# Write a program to display the grade based on marks:
# ≥ 90 → Grade A
# ≥ 75 → Grade B
# ≥ 50 → Grade C
# < 50 → Fail

marks = int(input("Enter Your Marks: "))
if(marks>100):
    print(f"you gave score is more than 100 its not correct enter the marks below 100")
else:
    if(marks>=90 and marks<=100):
        print(f"You score {marks}, so your grade is A ")
    else:
        if(90>marks and marks>=75):
            print(f"you score {marks}, so your grade is B")
        else:
            if(marks<75 and marks>=50):
                print(f"you score {marks}, so your grade is C")
            else:
                print(f"you score {marks}, so your grade is Fail")
