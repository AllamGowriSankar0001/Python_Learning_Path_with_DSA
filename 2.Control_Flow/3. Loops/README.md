# Loops in Python

A **loop** is used to execute a block of code repeatedly until a condition is met. Instead of writing the same code multiple times, loops allow you to repeat actions efficiently.

**Think of it like this:** If you need to print numbers 1 to 100, you don't write 100 print statements. You use a loop!

---

## Python's Main Looping Concepts

Python has **3 main looping concepts**:

1. **`for` loop** — iterate over a sequence
2. **`while` loop** — repeat while condition is true
3. **Nested loops** — loop inside another loop

**Plus loop control statements:**
- `break` — stop the loop
- `continue` — skip current iteration
- `pass` — placeholder

---

## 1. for Loop

Used to **iterate over a sequence** (list, tuple, string, range, etc.). Perfect when you know how many times you want to repeat something.

### Syntax

```python
for variable in sequence:
    statements
```

### Basic Example

```python
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

**How it works:**
- `range(5)` creates a sequence: 0, 1, 2, 3, 4
- `i` takes each value in the sequence
- The code inside the loop executes for each value

### Looping Through a String

```python
for ch in "Python":
    print(ch)
```

**Output:**
```
P
y
t
h
o
n
```

**More examples:**

```python
# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange

# Loop through a tuple
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num * 2)

# Output:
# 2
# 4
# 6
# 8
# 10
```

### Practical Example: Sum of Numbers

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")  # Sum: 150
```

---

## 2. range() Function (Used with for)

The `range()` function generates a sequence of numbers. It's commonly used with `for` loops.

### Three Forms of range()

#### Form 1: `range(stop)`
Generates numbers from 0 to stop-1

```python
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

#### Form 2: `range(start, stop)`
Generates numbers from start to stop-1

```python
for i in range(2, 7):
    print(i)

# Output: 2, 3, 4, 5, 6
```

#### Form 3: `range(start, stop, step)`
Generates numbers from start to stop-1, incrementing by step

```python
for i in range(1, 10, 2):
    print(i)

# Output: 1, 3, 5, 7, 9
```

**More examples:**

```python
# Count backwards
for i in range(10, 0, -1):
    print(i)

# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Even numbers
for i in range(0, 10, 2):
    print(i)

# Output: 0, 2, 4, 6, 8

# Countdown
for i in range(5, 0, -1):
    print(i)
print("Blast off!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!
```

**Important notes:**
- `range()` doesn't include the stop value (it's exclusive)
- Default start is 0
- Default step is 1
- `range()` doesn't create a list — it's a generator (memory efficient)

---

## 3. while Loop

Used when you **don't know in advance** how many times the loop should run. It continues as long as the condition is `True`.

### Syntax

```python
while condition:
    statements
```

### Example

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Output:**
```
1
2
3
4
5
```

**How it works:**
1. Check if `i <= 5` is `True`
2. If `True`, execute the code inside
3. Increment `i` by 1
4. Check the condition again
5. Repeat until condition becomes `False`

### More Examples

```python
# Countdown timer
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Time's up!")

# User input validation
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Sum until user enters 0
total = 0
num = 1
while num != 0:
    num = float(input("Enter a number (0 to stop): "))
    total += num
print(f"Total: {total}")
```

### ⚠️ Infinite Loop Warning

If the condition **never becomes `False`**, you get an **infinite loop**:

```python
# Infinite loop - DON'T RUN THIS!
i = 1
while i <= 5:
    print(i)
    # Forgot to increment i!
    # i stays 1 forever, loop never ends
```

**How to avoid:**
- Always ensure the condition can become `False`
- Make sure you modify the variable in the condition
- Use `break` to exit if needed

**To stop an infinite loop:** Press `Ctrl + C` in the terminal

---

## 4. Nested Loops

A **loop inside another loop**. The inner loop completes all its iterations for each iteration of the outer loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

**Output:**
```
0 0
0 1
1 0
1 1
2 0
2 1
```

**How it works:**
- Outer loop: `i` goes from 0 to 2 (3 iterations)
- For each `i`, inner loop: `j` goes from 0 to 1 (2 iterations)
- Total iterations: 3 × 2 = 6

### More Examples

#### Pattern Printing

```python
# Print a rectangle pattern
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()  # New line after each row

# Output:
# *****
# *****
# *****
```

#### Multiplication Table

```python
# Print multiplication table (1-5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i * j}", end="  ")
    print()  # New line after each row

# Output:
# 1 × 1 = 1  1 × 2 = 2  1 × 3 = 3  1 × 4 = 4  1 × 5 = 5
# 2 × 1 = 2  2 × 2 = 4  2 × 3 = 6  2 × 4 = 8  2 × 5 = 10
# ...
```

#### Matrix Processing

```python
# Process a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

**Common uses:**
- ✅ Patterns and shapes
- ✅ Matrices and 2D arrays
- ✅ Multiplication tables
- ✅ Nested data structures

---

## 5. else with Loops (Important)

Python allows `else` with loops. It's a unique feature that many beginners don't know about!

### How it Works

The `else` block executes **only if the loop ends normally** (without `break`).

### Example

```python
for i in range(5):
    print(i)
else:
    print("Loop finished normally")
```

**Output:**
```
0
1
2
3
4
Loop finished normally
```

### With break

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished normally")
```

**Output:**
```
0
1
2
```

**Notice:** The `else` block **did not execute** because the loop was broken.

### Practical Use Case

```python
# Search for a number
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list")
```

**Output:** `4 not found in the list`

**Why it's useful:**
- No need for a flag variable
- Cleaner code
- Executes only when loop completes naturally

---

## 6. Infinite Loop Example

An **infinite loop** runs forever (or until manually stopped).

### Example

```python
while True:
    print("Hello")
```

**Output:** Prints "Hello" forever (until you press `Ctrl + C`)

### When Infinite Loops Are Useful

```python
# Game loop
while True:
    user_input = input("Enter command (quit to exit): ")
    if user_input == "quit":
        break
    # Process game logic
    print(f"Processing: {user_input}")

# Server loop
while True:
    # Wait for requests
    # Process requests
    # Continue waiting
    pass
```

### ⚠️ Use Carefully!

**Always have an exit condition:**
- Use `break` to exit
- Check for a condition that can become `False`
- Provide a way for users to exit

**Bad infinite loop:**
```python
# DON'T DO THIS
while True:
    print("Stuck forever!")
    # No way to exit!
```

**Good infinite loop:**
```python
# DO THIS
while True:
    user_input = input("Continue? (no to exit): ")
    if user_input == "no":
        break
    print("Continuing...")
```

---

## for vs while: When to Use Which?

### Use `for` when:
- ✅ You know how many times to iterate
- ✅ Iterating over a sequence (list, string, range)
- ✅ You want simpler, cleaner code
- ✅ Counting or iterating through items

**Example:**
```python
# Iterate through a list
for item in shopping_list:
    print(item)
```

### Use `while` when:
- ✅ You don't know how many iterations
- ✅ Condition-based repetition
- ✅ User input validation
- ✅ Waiting for an event

**Example:**
```python
# Wait for valid input
while True:
    age = input("Enter age: ")
    if age.isdigit():
        break
```

---

## 📝 Complete Examples

### Example 1: Number Guessing Game

```python
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Guess the number between 1 and 100!")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game over! The number was {secret_number}")
```

### Example 2: Shopping Cart Total

```python
items = [
    {"name": "Apple", "price": 1.50, "quantity": 3},
    {"name": "Banana", "price": 0.75, "quantity": 5},
    {"name": "Orange", "price": 2.00, "quantity": 2}
]

total = 0
print("Shopping Cart:")
print("-" * 30)

for item in items:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['name']}: ${item['price']:.2f} × {item['quantity']} = ${item_total:.2f}")

print("-" * 30)
print(f"Total: ${total:.2f}")
```

### Example 3: Pattern Printing

```python
# Print a triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Use `for` loop to iterate over sequences
- [ ] Use `range()` function with different parameters
- [ ] Use `while` loop for condition-based repetition
- [ ] Create nested loops for complex patterns
- [ ] Use `break` to exit loops
- [ ] Use `continue` to skip iterations
- [ ] Understand `else` with loops
- [ ] Avoid infinite loops
- [ ] Choose between `for` and `while` appropriately
- [ ] Write clean, efficient loop code

---

## 🎯 Practice Exercises

### Exercise 1: Print Numbers 1-100

Use a `for` loop to print numbers from 1 to 100.

**Example solution:**

```python
for i in range(1, 101):
    print(i)
```

### Exercise 2: Sum of Even Numbers

Calculate the sum of all even numbers from 1 to 100.

### Exercise 3: Factorial Calculator

Calculate the factorial of a number using a loop.

**Example solution:**

```python
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
```

### Exercise 4: Password Validator

Keep asking for password until user enters "secret123".

### Exercise 5: Multiplication Table

Print the multiplication table for a given number (1-10).

### Exercise 6: Pattern Printing

Print a pyramid pattern using nested loops.

---

## 💡 Pro Tips

1. **Use `for` when possible** — it's cleaner and less error-prone:
   ```python
   # Good
   for i in range(10):
       print(i)
   
   # Less ideal
   i = 0
   while i < 10:
       print(i)
       i += 1
   ```

2. **Always update the condition variable in `while` loops**:
   ```python
   # Good
   i = 0
   while i < 10:
       print(i)
       i += 1
   ```

3. **Use `break` and `continue` wisely**:
   ```python
   # Good - clear exit condition
   for num in numbers:
       if num < 0:
           continue  # Skip negative
       process(num)
   ```

4. **Avoid deep nesting** (more than 2-3 levels):
   ```python
   # Try to limit nesting
   for i in range(10):
       for j in range(10):
           # OK - 2 levels
           pass
   ```

5. **Use meaningful variable names in loops**:
   ```python
   # Good
   for student in students:
       print(student)
   
   # Less clear
   for x in y:
       print(x)
   ```

6. **Remember: `range()` is exclusive of the stop value**:
   ```python
   range(5)  # 0, 1, 2, 3, 4 (not 5!)
   ```

---

## 🚀 Next Steps

Once you've mastered loops, move on to:
- break and continue (detailed)
- pass statement
- List comprehensions
- Functions
- Data structures (lists, dictionaries)

---

**Happy Coding! 💻**

