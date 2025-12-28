x = input("Enter something: ")
print(x)
print(type(x)) #<class 'str'> all inputs are strings
a = str(input("Enter your name: "))  #only strings are accepted
print(a) 
b = int(input("Enter your age: ")) #only numbers are accepted
print(b)
c = float(input("Enter your salary: ")) #only numbers are accepted and it will be a float
print(c)
d = bool(input("Enter your is_student: ")) #only True or False is accepted and it will be a boolean
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
y = int(input("Enter a: "))
z = int(input("Enter b: "))
sum_result = y + z
print(sum_result) #this will print the sum of a and b
print(type(sum_result)) #this will print the type of sum_result which is int

# we can also use multiple inputs in one line like this:
p,q,r = map(int,input("enter three numbers: ").split())
print(p+q+r)
print(type(p+q+r))

#Separator parameter
print("Hello", "World", sep="*") #this will print Hello*World
print("Hello", "World", sep="\n") #this will print Hello\nWorld in new line
print("Hello", "World", sep="\t") #this will print Hello\tWorld in tab
print("Hello", "World", sep="\n\t") #this will print Hello\n\tWorld in new line and tab

#End parameter
print("Hello", "World", end=" ") #this will print Hello World in same line
print("Hello", "World", end="...") #this will print Hello...World in same line

#Formatted output/f-strings
name = "John"
age = 20
print(f"Name: {name}, Age: {age}") #this will print Name: John, Age: 20
print(f"Name: {name}, Age: {age}") #this will print Name: John, Age: 20

#Escape characters
print("Hello\nWorld") #this will print Hello World in new line
print("Hello\tWorld") #this will print Hello World in tab space
print("Hello\"World") #this will print Hello"World in double quotes
print("Hello\\World") #this will print Hello\World in backslash

#Common errors
#Error 1: Forgetting Type Conversion
age = input("Enter your age: ")
print(age+10) #this will print the age plus 10 which is a string
print(type(age)) #this will print the type of age which is a string
print(int(age)+10) #this will print the age plus 10 which is a integer
print(type(int(age)+10)) #this will print the type of int(age)+10 which is a integer

#Error 2: Using + with String and Number
age = 20
print("Age: " + age) #this will print the age which is a number

#Error 3: Wrong Indentation
name = input("Enter name: ")
    print(name) #this will print the name which is a string

#Error 4: Using print() without parentheses
print("Hello") #this will print Hello which is a string
