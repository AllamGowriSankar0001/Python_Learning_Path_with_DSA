# Reverse a Number
num = int(input("enter a number :"))
print(str(num)[::-1])
result = 0
while(num>0):
    a = num%10
    result = result*10+a
    num = num//10
    # result += a
print(result)