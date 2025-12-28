# logical operators
a = 10
b = 5
print(a>0 and b>0) #true if both a and b are greater than 0
print(a>=10 or b>10) #true if either a or b is greater than 0
print(not(a>0)) #true if a is not greater than 0

# truth table for logical operators
print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false
print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false
print(not True) #false
print(not False) #true

# we can have multiple conditions using logical operators   
a = 10
b = 5
c = 15
print(a>0 and b>0 and c>0) #true if all a, b and c are greater than 0
print(a>0 or b>0 or c>0) #true if any one of a, b or c is greater than 0
print(not(a>0 and b>0 and c>0)) #true if all a, b and c are not greater than 0
print(not(a>0 or b>0 or c>0)) #true if any one of a, b or c is not greater than 0