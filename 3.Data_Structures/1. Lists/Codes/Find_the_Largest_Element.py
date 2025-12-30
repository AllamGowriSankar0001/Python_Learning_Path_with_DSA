# Find the largest number in a list without using max().
# nums = [3, 7, 2, 9, 4]
nums = [3, 7, 2, 9, 4]
a = nums[0]
for i in nums:
    if (a<i):
        a = i
print(a)