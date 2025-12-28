# elif in Python

`elif` stands for **"else if"**. It is used when you want to check multiple conditions, one after another, in a structured way.

---

## Why elif is Used

`elif` is essential for handling multiple conditions efficiently:

1. **To avoid writing many separate `if` statements**
2. **To check multiple conditions in order**
3. **Only one block runs** — the first condition that is `True`

**Think of it like this:** You're checking conditions one by one, and as soon as you find one that's true, you stop checking the rest.

---

## Syntax

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

**Key points:**
- `elif` must come **after** an `if` statement
- You can have **multiple** `elif` statements
- `else` is **optional** but recommended
- Only **one block** executes (the first condition that is `True`)

---

## How elif Works

Python checks conditions in order:

1. **First**, it checks the `if` condition
2. **If it's `False`**, it checks the first `elif`
3. **If that's `False`**, it checks the next `elif`
4. **Continues** until one condition is `True`
5. **If none are `True`**, the `else` block runs (if present)

**Important:** Once a condition is `True`, Python **stops checking** the remaining conditions!

---

## Example: Grade Calculator

```python
marks = 78

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
1. Check: `marks >= 90` → `78 >= 90` → `False` ❌
2. Check: `marks >= 75` → `78 >= 75` → `True` ✅
3. Execute: `print("Grade B")`
4. **Stop** — don't check the remaining conditions

---

## More Examples

### Example 1: Temperature Classification

```python
temperature = 25

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")
else:
    print("Cold")
```

**Output:** `Warm`

**Explanation:**
- `25 > 30` → `False`, check next
- `25 > 20` → `True`, print "Warm" and stop

### Example 2: Age Group Classification

```python
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

**Output:** `Adult`

### Example 3: Discount Calculator

```python
purchase_amount = 150

if purchase_amount >= 200:
    discount = 20
    print("20% discount applied!")
elif purchase_amount >= 100:
    discount = 10
    print("10% discount applied!")
elif purchase_amount >= 50:
    discount = 5
    print("5% discount applied!")
else:
    discount = 0
    print("No discount")

final_amount = purchase_amount - (purchase_amount * discount / 100)
print(f"Final amount: ${final_amount}")
```

**Output:**
```
10% discount applied!
Final amount: $135.0
```

---

## Important Points

### 1. You Can Use Multiple elif Statements

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

### 2. elif Must Come After if

```python
# Correct
if x > 10:
    print("Greater than 10")
elif x > 5:
    print("Greater than 5")

# Wrong - elif without if
elif x > 10:  # ERROR: SyntaxError
    print("Greater than 10")
```

### 3. else is Optional

```python
# With else
if score >= 50:
    print("Pass")
else:
    print("Fail")

# Without else (valid)
if score >= 50:
    print("Pass")
# If score < 50, nothing happens
```

### 4. Only One Block Executes

```python
x = 15

if x > 10:
    print("Greater than 10")  # This executes
elif x > 5:
    print("Greater than 5")  # This does NOT execute
```

**Even though both conditions are `True`, only the first one executes!**

---

## elif vs Multiple if

This is a **critical difference** that many beginners miss!

### ❌ Multiple if (Not Recommended)

```python
x = 15

if x > 0:
    print("Positive")  # Executes

if x > 5:
    print("Greater than 5")  # Also executes!

if x > 10:
    print("Greater than 10")  # Also executes!
```

**Output:**
```
Positive
Greater than 5
Greater than 10
```

**Problem:** All conditions are checked independently, so **multiple blocks can execute**.

### ✅ if-elif (Correct)

```python
x = 15

if x > 10:
    print("Greater than 10")  # Only this executes
elif x > 5:
    print("Greater than 5")  # Skipped
elif x > 0:
    print("Positive")  # Skipped
```

**Output:** `Greater than 10`

**Advantage:** Only **one block executes**, which is usually what you want!

### When to Use Each

**Use `if-elif` when:**
- ✅ You want **only one** condition to execute
- ✅ Conditions are **related** (checking the same variable)
- ✅ Conditions are **mutually exclusive**

**Use multiple `if` when:**
- ✅ You want **multiple** conditions to potentially execute
- ✅ Conditions are **independent** of each other

**Example of when multiple `if` is appropriate:**

```python
# Check multiple independent conditions
has_license = True
has_insurance = True
has_registration = True

if has_license:
    print("✓ Has license")

if has_insurance:
    print("✓ Has insurance")

if has_registration:
    print("✓ Has registration")
```

---

## Common Errors

### ❌ Error 1: Using elif Without if

```python
# Wrong
elif x > 10:
    print("Big")  # SyntaxError: invalid syntax
```

**✅ Correct:**

```python
if x > 10:
    print("Big")
elif x > 5:
    print("Medium")
```

### ❌ Error 2: Wrong Indentation

```python
# Wrong
if x > 10:
    print("Big")
    elif x > 5:  # IndentationError
        print("Medium")
```

**✅ Correct:**

```python
if x > 10:
    print("Big")
elif x > 5:  # Same indentation as if
    print("Medium")
```

### ❌ Error 3: Missing Colon (`:`)

```python
# Wrong
if x > 10
    print("Big")
elif x > 5  # Missing colon
    print("Medium")
```

**✅ Correct:**

```python
if x > 10:
    print("Big")
elif x > 5:  # Colon required
    print("Medium")
```

### ❌ Error 4: Using `=` Instead of `==`

```python
# Wrong
if x = 10:  # SyntaxError
    print("Equal to 10")
elif x = 5:  # SyntaxError
    print("Equal to 5")
```

**✅ Correct:**

```python
if x == 10:  # Use == for comparison
    print("Equal to 10")
elif x == 5:
    print("Equal to 5")
```

---

## 📝 Complete Example: Student Grade System

Here's a practical example combining multiple concepts:

```python
# Get student information
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

# Determine grade using elif
if marks >= 90:
    grade = "A"
    comment = "Excellent work!"
elif marks >= 80:
    grade = "B"
    comment = "Very good!"
elif marks >= 70:
    grade = "C"
    comment = "Good job!"
elif marks >= 60:
    grade = "D"
    comment = "Passed, but needs improvement"
else:
    grade = "F"
    comment = "Failed. Please study harder."

# Display results
print(f"\n{'='*30}")
print(f"Student: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Comment: {comment}")
print(f"{'='*30}")
```

**Sample Output:**
```
Enter student name: Alice
Enter marks (0-100): 85

==============================
Student: Alice
Marks: 85.0
Grade: B
Comment: Very good!
==============================
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Understand what `elif` means and why it's used
- [ ] Use `elif` to check multiple conditions
- [ ] Know that only one block executes in an if-elif-else chain
- [ ] Understand the difference between `elif` and multiple `if` statements
- [ ] Know when to use `elif` vs multiple `if` statements
- [ ] Avoid common errors (missing colon, wrong indentation, etc.)
- [ ] Write clean, readable conditional code with multiple conditions

---

## 🎯 Practice Exercises

### Exercise 1: Grade Calculator

Create a program that takes marks and assigns grades:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

**Example solution:**

```python
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
```

### Exercise 2: Age Group Classifier

Classify age into:
- Baby: 0-2
- Child: 3-12
- Teenager: 13-19
- Adult: 20-59
- Senior: 60+

### Exercise 3: BMI Calculator

Calculate BMI and classify:
- Underweight: < 18.5
- Normal: 18.5-24.9
- Overweight: 25-29.9
- Obese: >= 30

### Exercise 4: Time of Day Greeting

Based on hour (0-23), greet:
- Morning: 5-11
- Afternoon: 12-17
- Evening: 18-21
- Night: 22-4

---

## 💡 Pro Tips

1. **Always check conditions in the right order:**
   ```python
   # Wrong order
   if marks >= 50:
       grade = "C"
   elif marks >= 90:  # This will never execute!
       grade = "A"
   
   # Correct order (highest to lowest)
   if marks >= 90:
       grade = "A"
   elif marks >= 50:
       grade = "C"
   ```

2. **Use `elif` when conditions are related:**
   ```python
   # Good - checking the same variable
   if age < 13:
       category = "Child"
   elif age < 20:
       category = "Teenager"
   
   # Less ideal - unrelated conditions
   if age < 13:
       category = "Child"
   elif has_license:  # Different variable
       category = "Licensed"
   ```

3. **Keep conditions simple and readable:**
   ```python
   # Good
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   
   # Too complex
   if score >= 90 and attendance > 80:
       grade = "A"
   elif score >= 80 and attendance > 70:
       grade = "B"
   ```

4. **Remember: Only the first `True` condition executes:**
   ```python
   x = 15
   if x > 10:      # True - executes this
       print("A")
   elif x > 5:     # Also True, but skipped!
       print("B")
   ```

5. **Use `else` as a catch-all:**
   ```python
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   else:  # Catches all other cases
       grade = "C or below"
   ```

---

## 🚀 Next Steps

Once you've mastered `elif`, move on to:
- Loops (for, while)
- break and continue statements
- pass statement
- Combining control flow with loops

---

**Happy Coding! 💻**

