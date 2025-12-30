# Create two lists:
# one with even numbers
# one with odd numbers
# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 2, 3, 4, 5, 6]

even_nums = []
odd_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(even_nums) 
print(odd_nums)   