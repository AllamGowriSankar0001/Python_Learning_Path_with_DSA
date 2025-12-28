# Sum of Digits of a Number

num = int(input("Give a number: "))
result = 0
while(num>0):
    a=num%10
    num= num//10
    result += a
print(result)
