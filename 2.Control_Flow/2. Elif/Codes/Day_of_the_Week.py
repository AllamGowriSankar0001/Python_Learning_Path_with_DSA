# Write a program that takes a number (1–7) and displays the day:
# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# 6 → Saturday
# 7 → Sunday
# Any other number → Invalid day


num = int(input("Enter the Number: "))
if(num==1):
    print("its monday")
elif(num==2):
    print("its tuesday")
elif(num==3):
    print("its wednesday")
elif(num==4):
    print("its thursday")
elif(num==5):
    print("its friday")
elif(num==6):
    print("its saturday")
else:
    print("its sunday")