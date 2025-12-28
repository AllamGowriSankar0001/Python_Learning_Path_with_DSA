# break and continue in Python

`break` and `continue` are **loop control statements**. They are used to change the normal flow of loops (`for` and `while`), giving you more control over when to stop or skip iterations.

**Think of it like this:**
- `break` = "Stop everything, I'm done!"
- `continue` = "Skip this one, but keep going!"

---

## 1. break Statement

### What it Does

- **Immediately stops the loop**
- **Control moves outside the loop**
- Remaining iterations are **skipped**
- The loop ends completely

### Syntax

```python
break
```

### Example: break in for Loop

```python
for i in range(10):
    if i == 5:
        break
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
1. Loop starts: `i = 0`, prints `0`
2. `i = 1`, prints `1`
3. `i = 2`, prints `2`
4. `i = 3`, prints `3`
5. `i = 4`, prints `4`
6. `i = 5`, condition `i == 5` is `True`
7. `break` executes → **loop stops immediately**
8. Values 5, 6, 7, 8, 9 are **never processed**

👉 **Loop ends when `i == 5`**

### break in while Loop

```python
i = 1
while i <= 10:
    if i == 6:
        break
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
- Loop runs while `i <= 10`
- When `i == 6`, `break` executes
- Loop stops, remaining iterations (6-10) are skipped

### More Examples

#### Example 1: Finding First Match

```python
numbers = [1, 3, 5, 8, 9, 10, 12]

for num in numbers:
    if num % 2 == 0:  # First even number
        print(f"First even number found: {num}")
        break
```

**Output:** `First even number found: 8`

#### Example 2: User Input with Exit

```python
while True:
    user_input = input("Enter a number (or 'quit' to exit): ")
    
    if user_input == "quit":
        break  # Exit the infinite loop
    
    print(f"You entered: {user_input}")
    # Process the input...

print("Goodbye!")
```

#### Example 3: Search in Nested Loop

```python
found = False
for i in range(3):
    for j in range(3):
        if i * j == 4:
            print(f"Found at i={i}, j={j}")
            break  # Only breaks inner loop
    if found:
        break  # Break outer loop if needed
```

**Note:** `break` only breaks the **innermost loop** it's in. To break multiple loops, you need additional logic.

---

## 2. continue Statement

### What it Does

- **Skips the current iteration**
- **Loop continues with the next iteration**
- The rest of the current iteration is ignored
- Loop doesn't end, just moves to the next value

### Syntax

```python
continue
```

### Example: continue in for Loop

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Output:**
```
0
1
3
4
```

**How it works:**
1. `i = 0`, prints `0`
2. `i = 1`, prints `1`
3. `i = 2`, condition `i == 2` is `True`
4. `continue` executes → **skip rest of this iteration**
5. `print(i)` is **not executed** for `i == 2`
6. Loop continues: `i = 3`, prints `3`
7. `i = 4`, prints `4`

👉 **2 is skipped, loop continues**

### continue in while Loop

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

**Output:**
```
1
2
4
5
```

**Important:** Notice that `i += 1` comes **before** the `continue`. If it came after, `i` would never increment when `i == 3`, causing an infinite loop!

**Correct order:**
```python
i = 0
while i < 5:
    i += 1  # Increment first
    if i == 3:
        continue  # Skip printing, but i is already incremented
    print(i)
```

**Wrong order (infinite loop!):**
```python
i = 0
while i < 5:
    if i == 3:
        continue  # Skip, i stays 3 forever!
    print(i)
    i += 1  # Never reached when i == 3
```

### More Examples

#### Example 1: Skip Negative Numbers

```python
numbers = [1, -2, 3, -4, 5, -6, 7]

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    print(num)
```

**Output:**
```
1
3
5
7
```

#### Example 2: Process Only Valid Data

```python
data = ["apple", "", "banana", None, "orange", ""]

for item in data:
    if not item:  # Skip empty strings and None
        continue
    print(f"Processing: {item}")
```

**Output:**
```
Processing: apple
Processing: banana
Processing: orange
```

#### Example 3: Skip Multiples

```python
# Print numbers 1-20, but skip multiples of 5
for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i, end=" ")
```

**Output:** `1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19`

---

## break vs continue: Key Differences

| Feature | break | continue |
|--------|-------|----------|
| **Action** | Stops the loop completely | Skips current iteration |
| **Loop Status** | Loop ends | Loop continues |
| **Remaining Iterations** | All skipped | Only current skipped |
| **Use Case** | Found what you need, exit | Skip invalid items, keep going |

### Visual Comparison

```python
# break example
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2 (stops at 3)

# continue example
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4 (skips 3, continues)
```

---

## Practical Examples

### Example 1: Number Validation Loop

```python
# Keep asking until valid number is entered
while True:
    user_input = input("Enter a positive number: ")
    
    if user_input.lower() == "quit":
        print("Exiting...")
        break
    
    try:
        number = float(user_input)
        if number <= 0:
            print("Please enter a positive number!")
            continue  # Skip to next iteration
        print(f"Valid number: {number}")
        break  # Exit loop when valid number entered
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip to next iteration
```

### Example 2: Processing List with Conditions

```python
numbers = [10, 20, 0, 30, 40, 0, 50]
total = 0
count = 0

for num in numbers:
    if num == 0:
        continue  # Skip zeros
    if num > 100:
        print(f"Number {num} is too large, stopping!")
        break  # Stop if number too large
    total += num
    count += 1

print(f"Sum: {total}, Count: {count}, Average: {total/count}")
```

### Example 3: Search with break

```python
# Search for a name in a list
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
search_name = "Charlie"
found = False

for name in names:
    if name == search_name:
        print(f"Found {search_name}!")
        found = True
        break  # Stop searching once found

if not found:
    print(f"{search_name} not found")
```

### Example 4: Filter and Process

```python
# Process only even numbers, stop if number > 50
numbers = [2, 5, 8, 12, 15, 18, 25, 30, 35, 40]

for num in numbers:
    if num > 50:
        print("Number too large, stopping!")
        break
    
    if num % 2 != 0:
        continue  # Skip odd numbers
    
    print(f"Processing even number: {num}")
    # Do something with the number...
```

**Output:**
```
Processing even number: 2
Processing even number: 8
Processing even number: 12
Processing even number: 18
Processing even number: 30
Processing even number: 40
```

---

## Common Patterns

### Pattern 1: break in Infinite Loop

```python
# Common pattern for user input
while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    # Process command...
```

### Pattern 2: continue for Filtering

```python
# Process only valid items
for item in items:
    if not is_valid(item):
        continue
    process(item)
```

### Pattern 3: break After Finding

```python
# Stop after finding first match
for item in collection:
    if matches_criteria(item):
        result = item
        break
```

### Pattern 4: continue to Skip Errors

```python
# Skip items that cause errors
for data in dataset:
    try:
        process(data)
    except Exception:
        continue  # Skip problematic items
```

---

## Important Notes and Warnings

### ⚠️ break Only Breaks Innermost Loop

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"i={i}, j={j}")
```

**Output:**
```
i=0, j=0
i=1, j=0
i=2, j=0
```

To break outer loop, use a flag:

```python
break_outer = False
for i in range(3):
    for j in range(3):
        if j == 1:
            break_outer = True
            break
    if break_outer:
        break
```

### ⚠️ continue in while Loop: Watch Variable Updates

```python
# Correct
i = 0
while i < 5:
    i += 1  # Update before continue
    if i == 3:
        continue
    print(i)

# Wrong - infinite loop!
i = 0
while i < 5:
    if i == 3:
        continue  # i never increments!
    print(i)
    i += 1
```

### ⚠️ break/continue with else

Remember: `else` with loops only executes if loop ends **normally** (no `break`):

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed normally")  # Won't execute because of break
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Understand what `break` does and when to use it
- [ ] Understand what `continue` does and when to use it
- [ ] Use `break` to exit loops early
- [ ] Use `continue` to skip iterations
- [ ] Know the difference between `break` and `continue`
- [ ] Use `break` in both `for` and `while` loops
- [ ] Use `continue` in both `for` and `while` loops
- [ ] Avoid common mistakes (infinite loops with `continue` in `while`)
- [ ] Understand that `break` only breaks the innermost loop
- [ ] Write clean, efficient loop code with control statements

---

## 🎯 Practice Exercises

### Exercise 1: Find First Even Number

Write a program that finds and prints the first even number in a list, then stops.

**Example solution:**

```python
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

### Exercise 2: Skip Multiples of 3

Print numbers 1-20, but skip all multiples of 3.

### Exercise 3: Password Checker

Keep asking for password until user enters "secret123" or types "quit".

**Example solution:**

```python
while True:
    password = input("Enter password (or 'quit' to exit): ")
    if password == "quit":
        break
    if password == "secret123":
        print("Access granted!")
        break
    print("Wrong password, try again!")
```

### Exercise 4: Process Valid Numbers

Process a list of numbers, skip negative numbers, and stop if you encounter a number greater than 100.

### Exercise 5: Search and Stop

Search for a name in a list. If found, print it and stop. If not found after checking all items, print "Not found".

---

## 💡 Pro Tips

1. **Use `break` when you've found what you need:**
   ```python
   # Good - stops when found
   for item in items:
       if item == target:
           print("Found!")
           break
   ```

2. **Use `continue` to filter items:**
   ```python
   # Good - processes only valid items
   for item in items:
       if not is_valid(item):
           continue
       process(item)
   ```

3. **Always update loop variables before `continue` in `while` loops:**
   ```python
   # Correct
   i = 0
   while i < 10:
       i += 1
       if i % 2 == 0:
           continue
       print(i)
   ```

4. **Use flags to break outer loops:**
   ```python
   # When you need to break multiple loops
   done = False
   for i in range(10):
       for j in range(10):
           if condition:
               done = True
               break
       if done:
           break
   ```

5. **Combine `break` and `continue` for complex logic:**
   ```python
   for item in items:
       if item < 0:
           continue  # Skip negative
       if item > 100:
           break  # Stop if too large
       process(item)
   ```

6. **Use `break` in infinite loops for clean exit:**
   ```python
   # Clean pattern
   while True:
       user_input = input("Enter command: ")
       if user_input == "quit":
           break
       process(user_input)
   ```

---

## 🚀 Next Steps

Once you've mastered `break` and `continue`, move on to:
- `pass` statement
- List comprehensions
- Functions
- Exception handling (try/except)
- More advanced loop patterns

---

**Happy Coding! 💻**

