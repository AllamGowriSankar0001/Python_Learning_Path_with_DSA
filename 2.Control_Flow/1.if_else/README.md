# if / else Statement in Python

The **if / else statement** is a decision-making statement. It allows a program to execute different blocks of code based on a condition. This is one of the most fundamental concepts in programming!

---

## 1. if Statement

Used to execute a block of code **only if the condition is True**.

### Syntax

```python
if condition:
    statement(s)
```

### Example

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

**Output:** `Eligible to vote`

**How it works:**
- The condition `age >= 18` is evaluated
- If it's `True`, the code inside the `if` block executes
- If it's `False`, the code is skipped

**More examples:**

```python
# Check if number is positive
number = 10
if number > 0:
    print("Positive number")

# Check if user is logged in
is_logged_in = True
if is_logged_in:
    print("Welcome back!")

# Check if score is passing
score = 85
if score >= 60:
    print("You passed!")
```

---

## 2. if - else Statement

Executes one block if the condition is `True`, otherwise executes the `else` block.

### Syntax

```python
if condition:
    statement(s)
else:
    statement(s)
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

**Output:** `Not eligible to vote`

**How it works:**
- If the condition is `True`, the `if` block executes
- If the condition is `False`, the `else` block executes
- **One of them will always execute** (mutually exclusive)

**More examples:**

```python
# Even or odd number
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Pass or fail
marks = 45
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Positive or negative
value = -5
if value > 0:
    print("Positive")
else:
    print("Negative or zero")
```

---

## 3. if - elif - else Ladder

Used to check **multiple conditions** in sequence.

### Syntax

```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

**Output:** `Grade B`

**How it works:**
1. Check the first `if` condition
2. If `True`, execute that block and **stop**
3. If `False`, check the next `elif` condition
4. Continue until one condition is `True`
5. If all conditions are `False`, execute the `else` block

**Important points:**
- ✅ Only **one block** executes (the first condition that is `True`)
- ✅ `elif` is short for "else if"
- ✅ You can have multiple `elif` statements
- ✅ `else` is optional but recommended

**More examples:**

```python
# Temperature check
temperature = 25

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")
else:
    print("Cold")

# Age group classification
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

---

## 4. Nested if - else (Very Important)

A **nested if-else** means an `if` or `else` block contains another `if-else` statement. This is used for complex conditions.

### Syntax

```python
if condition1:
    if condition2:
        statement(s)
    else:
        statement(s)
else:
    statement(s)
```

### Nested if-else Example

```python
num = 10

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

**Output:** `Positive number`

**How it works:**
- First, check if `num >= 0`
- If `True`, go inside and check if `num == 0`
- If `num == 0`, print "Number is zero"
- If `num != 0`, print "Positive number"
- If `num < 0`, print "Negative number"

**More examples:**

```python
# Check number type and sign
number = 5

if number != 0:
    if number > 0:
        print("Positive number")
    else:
        print("Negative number")
else:
    print("Zero")

# Login system with role check
username = "admin"
password = "12345"
role = "admin"

if username == "admin":
    if password == "12345":
        if role == "admin":
            print("Admin access granted")
        else:
            print("Invalid role")
    else:
        print("Wrong password")
else:
    print("User not found")
```

**Key points:**
- ✅ One decision inside another
- ✅ Used for complex conditions
- ✅ Can be nested multiple levels deep
- ⚠️ Too much nesting can make code hard to read (try to limit to 2-3 levels)

---

## 5. Indentation in if / else (Very Important)

Python uses **indentation** to define blocks of code. This is **mandatory**, not optional!

### ❌ Wrong:

```python
if x > 5:
print("Hello")  # ERROR: IndentationError
```

### ✅ Correct:

```python
if x > 5:
    print("Hello")  # Correct indentation (4 spaces or 1 tab)
```

**Indentation rules:**
- Use **4 spaces** (recommended) or **1 tab** for each level
- Be **consistent** (don't mix spaces and tabs)
- All statements in the same block must have the same indentation

**Examples:**

```python
# Single statement
if x > 5:
    print("Hello")

# Multiple statements
if x > 5:
    print("Hello")
    print("World")
    print("Python")

# Nested indentation
if x > 5:
    if y > 10:
        print("Both conditions true")
    else:
        print("Only first condition true")
else:
    print("First condition false")
```

**Common indentation mistakes:**

```python
# Wrong: No indentation
if x > 5:
print("Hello")  # ERROR

# Wrong: Inconsistent indentation
if x > 5:
    print("Hello")
  print("World")  # ERROR: inconsistent

# Wrong: Missing indentation after else
if x > 5:
    print("Hello")
else:
print("World")  # ERROR
```

---

## 6. Conditions Used in if

Conditions are formed using:

### Comparison Operators

```python
# Equal to
if age == 18:
    print("Exactly 18")

# Not equal to
if age != 18:
    print("Not 18")

# Greater than
if score > 80:
    print("High score")

# Less than
if price < 100:
    print("Affordable")

# Greater than or equal
if age >= 18:
    print("Adult")

# Less than or equal
if temperature <= 0:
    print("Freezing")
```

### Logical Operators

```python
# AND - both conditions must be True
if age >= 18 and age <= 60:
    print("Working age")

# OR - at least one condition must be True
if score >= 90 or bonus_points > 10:
    print("Excellent performance")

# NOT - reverses the condition
if not is_logged_in:
    print("Please log in")

# Combining multiple operators
if (age >= 18 and age <= 65) and (has_license == True):
    print("Can drive")
```

**More examples:**

```python
# Complex condition
age = 25
has_license = True
has_insurance = True

if age >= 18 and has_license and has_insurance:
    print("Can rent a car")

# Range check
score = 85
if score >= 80 and score < 90:
    print("Grade B")

# Multiple options
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Negation
is_weekend = False
if not is_weekend:
    print("Work day")
```

---

## 7. Short if (Ternary Operator)

Python allows a **one-line if-else** statement. This is called a ternary operator or conditional expression.

### Syntax

```python
statement_if_true if condition else statement_if_false
```

### Example

```python
marks = 75
result = "Pass" if marks >= 40 else "Fail"
print(result)  # Pass
```

**How it works:**
- If condition is `True`, return `statement_if_true`
- If condition is `False`, return `statement_if_false`

**More examples:**

```python
# Find maximum
a = 10
b = 5
maximum = a if a > b else b
print(maximum)  # 10

# Check even/odd
number = 8
status = "Even" if number % 2 == 0 else "Odd"
print(status)  # Even

# Grade assignment
score = 85
grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 50 else "F"
print(grade)  # B

# Age check
age = 20
message = "Adult" if age >= 18 else "Minor"
print(message)  # Adult
```

**When to use:**
- ✅ Simple conditions with single statements
- ✅ Assigning values based on conditions
- ❌ Avoid for complex logic (use regular if-else instead)

---

## 8. Common Errors (Exam Tip)

### ❌ Error 1: Missing Colon (`:`)

```python
# Wrong
if x > 5
    print("Hello")  # SyntaxError: expected ':'

# Correct
if x > 5:
    print("Hello")
```

### ❌ Error 2: Wrong Indentation

```python
# Wrong
if x > 5:
print("Hello")  # IndentationError

# Correct
if x > 5:
    print("Hello")
```

### ❌ Error 3: Using `=` Instead of `==`

```python
# Wrong
if x = 5:  # SyntaxError: invalid syntax
    print("Hello")

# Correct
if x == 5:  # Comparison, not assignment
    print("Hello")
```

### ❌ Error 4: Incorrect Logical Operators

```python
# Wrong (using & instead of and)
if x > 5 & y < 10:  # & is bitwise, not logical
    print("Hello")

# Correct
if x > 5 and y < 10:
    print("Hello")
```

### ❌ Error 5: Forgetting Parentheses in Complex Conditions

```python
# Wrong (ambiguous)
if age >= 18 and age <= 65 or has_special_permission:
    print("Access granted")

# Correct (clear precedence)
if (age >= 18 and age <= 65) or has_special_permission:
    print("Access granted")
```

---

## 📝 Complete Example: Grade Calculator

Here's a practical example combining multiple concepts:

```python
# Get student information
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

# Calculate grade
if marks >= 90:
    grade = "A"
    comment = "Excellent!"
elif marks >= 75:
    grade = "B"
    comment = "Very Good!"
elif marks >= 50:
    grade = "C"
    comment = "Good"
else:
    grade = "F"
    comment = "Needs Improvement"

# Display result
print(f"\nStudent: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Comment: {comment}")

# Additional check
if marks >= 50:
    print("Status: Passed ✅")
else:
    print("Status: Failed ❌")
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Use `if` statement to execute code conditionally
- [ ] Use `if-else` to handle two possible outcomes
- [ ] Use `if-elif-else` to check multiple conditions
- [ ] Create nested if-else statements
- [ ] Understand and use proper indentation
- [ ] Form conditions using comparison and logical operators
- [ ] Use ternary operator for simple conditions
- [ ] Avoid common errors (missing colon, wrong indentation, using `=` instead of `==`)
- [ ] Write clean, readable conditional code

---

## 🎯 Practice Exercises

### Exercise 1: Even/Odd Checker

Create a program that checks if a number is even or odd.

**Example solution:**

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Exercise 2: Age Group Classifier

Create a program that classifies age into:
- Child: < 13
- Teenager: 13-19
- Adult: 20-59
- Senior: 60+

### Exercise 3: Number Type Checker

Check if a number is positive, negative, or zero (using nested if-else).

**Example solution:**

```python
num = float(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Positive number")
else:
    print("Negative number")
```

### Exercise 4: Login System

Create a simple login system that checks username and password.

### Exercise 5: Temperature Converter with Advice

Convert temperature and provide advice based on the result.

---

## 💡 Pro Tips

1. **Always use `==` for comparison, not `=`**:
   ```python
   # Wrong
   if x = 5:  # ERROR
   
   # Correct
   if x == 5:  # True
   ```

2. **Use meaningful variable names in conditions**:
   ```python
   # Good
   if age >= 18:
       print("Adult")
   
   # Less clear
   if a >= 18:
       print("Adult")
   ```

3. **Keep conditions simple and readable**:
   ```python
   # Good
   if age >= 18 and has_license:
       print("Can drive")
   
   # Too complex
   if (age >= 18 and age <= 65) and (has_license == True) and (has_insurance == True) and (points < 12):
       print("Can drive")
   ```

4. **Use parentheses for clarity in complex conditions**:
   ```python
   # Clear
   if (age >= 18 and age <= 65) or has_special_permission:
       print("Access granted")
   ```

5. **Limit nesting depth** (2-3 levels max):
   ```python
   # Try to avoid
   if condition1:
       if condition2:
           if condition3:
               if condition4:  # Too deep!
                   print("Hello")
   ```

6. **Use `elif` instead of multiple `if` statements when checking the same variable**:
   ```python
   # Good
   if score >= 90:
       grade = "A"
   elif score >= 75:
       grade = "B"
   
   # Less efficient
   if score >= 90:
       grade = "A"
   if score >= 75 and score < 90:
       grade = "B"
   ```

---

## 🚀 Next Steps

Once you've mastered if/else statements, move on to:
- Loops (for, while)
- break and continue statements
- pass statement
- More complex control flow patterns

---

**Happy Coding! 💻**

