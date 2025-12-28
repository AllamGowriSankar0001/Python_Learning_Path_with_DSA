# Write a program to check whether a year is a leap year or not.
# Hints
# Year divisible by 4
# But not divisible by 100 unless divisible by 400

year = int(input("Enter a year: "))
if(year/4 ==0 and year/400 ==0 and year/100!=0 ):
    print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is not a Leap Year")
