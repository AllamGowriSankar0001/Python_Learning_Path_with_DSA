# Write a program using elif to classify age:
# Age < 13 → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60+ → Senior

age = int(input("Enter the age: "))
if(age<13):
    print("child")
elif(age>13 and age<19):
    print("teenager")
elif(age>20 and age<59):
    print("Adult")
else:
    print("senior")