#  Remove duplicate values without using set().
# nums = [1, 2, 2, 3, 4, 4, 5]

nums = [1, 2, 2, 3, 4, 4, 5]
a = []
for i in nums:
    if(i not in a):
       a.append(i)
    else:
        pass
print(a)