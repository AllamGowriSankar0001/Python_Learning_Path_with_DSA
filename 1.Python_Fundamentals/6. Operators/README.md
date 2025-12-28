# Operators in Python

An **operator** is a symbol used to perform operations on variables and values.

**Example:**

```python
c = a + b
```

Here, `+` is the **operator** and `a`, `b` are **operands**.

---

## Types of Operators in Python

Python has **7 main types** of operators:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison (Relational) Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

---

## 1. Arithmetic Operators

Used for **mathematical operations**.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponent (Power) | `2 ** 3` | `8` |

### Examples:

```python
a = 10
b = 3

print(a + b)   # 13 (Addition)
print(a - b)   # 7 (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.3333333333333335 (Division - returns float)
print(a // b)  # 3 (Floor Division - returns int)
print(a % b)   # 1 (Modulus - remainder of division)
print(a ** b)  # 1000 (Exponent - 10 to the power of 3)
```

### Key Points:

- **Division (`/`)** always returns a float, even if the result is a whole number
- **Floor Division (`//`)** returns the integer part (rounds down)
- **Modulus (`%`)** returns the remainder after division
- **Exponent (`**`)** raises the first number to the power of the second

**More examples:**

```python
# Division vs Floor Division
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3

# Modulus (useful for checking even/odd)
print(10 % 2)   # 0 (even)
print(11 % 2)   # 1 (odd)

# Exponent
print(2 ** 4)   # 16 (2 to the power of 4)
print(5 ** 2)   # 25 (5 squared)
```

---

## 2. Assignment Operators

Used to **assign and update values**.

| Operator | Name | Example | Equivalent To |
|----------|------|---------|---------------|
| `=` | Assign | `x = 5` | `x = 5` |
| `+=` | Add and Assign | `x += 2` | `x = x + 2` |
| `-=` | Subtract and Assign | `x -= 2` | `x = x - 2` |
| `*=` | Multiply and Assign | `x *= 2` | `x = x * 2` |
| `/=` | Divide and Assign | `x /= 2` | `x = x / 2` |
| `//=` | Floor Divide and Assign | `x //= 2` | `x = x // 2` |
| `%=` | Modulus and Assign | `x %= 2` | `x = x % 2` |
| `**=` | Exponent and Assign | `x **= 2` | `x = x ** 2` |

### Examples:

```python
# Basic assignment
x = 5
print(x)  # 5

# Add and assign
x += 2    # Same as: x = x + 2
print(x)  # 7

# Subtract and assign
x -= 3    # Same as: x = x - 3
print(x)  # 4

# Multiply and assign
x *= 2    # Same as: x = x * 2
print(x)  # 8

# Divide and assign
x /= 4    # Same as: x = x / 4
print(x)  # 2.0

# Modulus and assign
x %= 2    # Same as: x = x % 2
print(x)  # 0.0

# Exponent and assign
x = 3
x **= 2   # Same as: x = x ** 2
print(x)  # 9
```

**Why use assignment operators?**
- ✅ Shorter and cleaner code
- ✅ More readable
- ✅ Common in loops and calculations

---

## 3. Comparison (Relational) Operators

Used to **compare values**. Result is always `True` or `False`.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `10 == 5` | `False` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal | `10 >= 10` | `True` |
| `<=` | Less than or equal | `10 <= 5` | `False` |

### Examples:

```python
a = 10
b = 5

print(a == b)  # False (10 is not equal to 5)
print(a != b)  # True (10 is not equal to 5)
print(a > b)   # True (10 is greater than 5)
print(a < b)   # False (10 is not less than 5)
print(a >= b)  # True (10 is greater than or equal to 5)
print(a <= b)  # False (10 is not less than or equal to 5)
```

**Common use cases:**

```python
# Check if equal
age = 18
print(age == 18)  # True

# Check if not equal
name = "Alice"
print(name != "Bob")  # True

# Compare numbers
score = 85
print(score >= 80)  # True (passing grade)
print(score < 60)   # False (not failing)
```

**⚠️ Important:** Use `==` for comparison, not `=` (which is assignment)!

```python
# Wrong
if x = 5:  # ERROR: = is assignment, not comparison

# Correct
if x == 5:  # True: == is comparison
```

---

## 4. Logical Operators

Used to **combine conditions** and make decisions.

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `and` | Logical AND | True if **both** are True | `a > 5 and b < 10` |
| `or` | Logical OR | True if **any one** is True | `a > 5 or b < 10` |
| `not` | Logical NOT | Reverses the result | `not (a > 5)` |

### Examples:

```python
a = 10
b = 5

# AND operator
print(a > 5 and b < 10)  # True (both conditions are True)
print(a > 5 and b > 10)  # False (second condition is False)

# OR operator
print(a > 5 or b > 10)   # True (first condition is True)
print(a < 5 or b > 10)   # False (both conditions are False)

# NOT operator
print(not (a > 5))       # False (reverses True to False)
print(not (a < 5))       # True (reverses False to True)
```

### Truth Tables:

**AND (`and`):**
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**OR (`or`):**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**NOT (`not`):**
| A | not A |
|---|-------|
| True | False |
| False | True |

### Practical Examples:

```python
# Check age and permission
age = 18
has_permission = True

if age >= 18 and has_permission:
    print("Access granted")

# Check if number is in range
number = 15
if number < 10 or number > 20:
    print("Number is outside range")

# Check if not empty
name = ""
if not name:
    print("Name is required")
```

---

## 5. Bitwise Operators

Work on **binary (bit-level) values**. Used for low-level programming.

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `&` | AND | Bitwise AND | `5 & 3` → `1` |
| `\|` | OR | Bitwise OR | `5 \| 3` → `7` |
| `^` | XOR | Bitwise XOR | `5 ^ 3` → `6` |
| `~` | NOT | Bitwise NOT | `~5` → `-6` |
| `<<` | Left Shift | Shift bits left | `5 << 1` → `10` |
| `>>` | Right Shift | Shift bits right | `5 >> 1` → `2` |

### Examples:

```python
a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)   # 1 (AND: 101 & 011 = 001)
print(a | b)   # 7 (OR: 101 | 011 = 111)
print(a ^ b)   # 6 (XOR: 101 ^ 011 = 110)
print(~a)      # -6 (NOT: inverts all bits)
print(a << 1)  # 10 (Left shift: 101 << 1 = 1010)
print(a >> 1)  # 2 (Right shift: 101 >> 1 = 10)
```

**Note:** Bitwise operators are advanced and rarely used in beginner Python programming. Focus on arithmetic, comparison, and logical operators first!

---

## 6. Membership Operators

Check if a value is **present in a sequence** (list, tuple, string, etc.).

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `in` | In | True if value is found | `2 in [1, 2, 3]` → `True` |
| `not in` | Not In | True if value is not found | `4 not in [1, 2, 3]` → `True` |

### Examples:

```python
# Check in list
numbers = [1, 2, 3, 4, 5]
print(2 in numbers)      # True
print(6 in numbers)      # False
print(3 not in numbers)  # False

# Check in string
text = "Python"
print("P" in text)        # True
print("p" in text)        # True (case-sensitive)
print("Java" in text)     # False
print("th" in text)       # True (substring check)

# Check in tuple
fruits = ("apple", "banana", "orange")
print("apple" in fruits)  # True
print("grape" in fruits)  # False

# Practical use
if "admin" in user_roles:
    print("Admin access granted")
```

**Common use cases:**

```python
# Check if item exists
shopping_list = ["milk", "bread", "eggs"]
item = "milk"
if item in shopping_list:
    print(f"{item} is in the list")

# Check if character exists in string
email = "user@example.com"
if "@" in email:
    print("Valid email format")
```

---

## 7. Identity Operators

Compare **memory location**, not value. Check if two variables refer to the same object.

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `is` | Is | True if both refer to same object | `a is b` |
| `is not` | Is Not | True if both refer to different objects | `a is not b` |

### Examples:

```python
# Same value, same object (for small integers)
a = 10
b = 10
print(a is b)        # True (Python optimizes small integers)
print(a == b)        # True (values are equal)

# Different objects with same value
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)        # False (different objects)
print(x == y)        # True (values are equal)

# Same object
z = x
print(x is z)        # True (same object)
print(x == z)        # True (values are equal)

# None check (common use case)
value = None
if value is None:
    print("Value is None")
```

**⚠️ Important:**

- Use `==` to **compare values**
- Use `is` to **check identity** (same object in memory)
- Use `is None` or `is not None` for None checks (best practice)

**Common mistake:**

```python
# Wrong
if value == None:  # Works but not recommended

# Correct
if value is None:  # Pythonic way
```

---

## Operator Precedence

The **order of execution** when multiple operators are used together.

### Precedence Order (Highest to Lowest):

1. **`()`** - Parentheses (highest priority)
2. **`**`** - Exponent
3. **`*`, `/`, `//`, `%`** - Multiplication, Division, Floor Division, Modulus
4. **`+`, `-`** - Addition, Subtraction
5. **`==`, `!=`, `>`, `<`, `>=`, `<=`** - Comparison
6. **`not`** - Logical NOT
7. **`and`** - Logical AND
8. **`or`** - Logical OR (lowest priority)

### Examples:

```python
# Multiplication before addition
result = 10 + 2 * 3
print(result)  # 16 (not 36!)
# Calculation: 2 * 3 = 6, then 10 + 6 = 16

# Parentheses override precedence
result = (10 + 2) * 3
print(result)  # 36
# Calculation: (10 + 2) = 12, then 12 * 3 = 36

# Exponentiation before multiplication
result = 2 ** 3 * 4
print(result)  # 32
# Calculation: 2 ** 3 = 8, then 8 * 4 = 32

# Logical operators
result = True and False or True
print(result)  # True
# Calculation: (True and False) = False, then (False or True) = True

# Use parentheses for clarity
result = (10 > 5) and (20 < 30)
print(result)  # True
```

**💡 Tip:** Use parentheses to make your code clearer, even if not strictly necessary!

```python
# Clear
result = (a + b) * (c - d)

# Less clear (but works the same)
result = a + b * c - d
```

---

## 📝 Complete Example: Using Multiple Operators

```python
# Calculate total with discount
price = 100
quantity = 3
discount = 0.1  # 10%

# Calculate total
subtotal = price * quantity
discount_amount = subtotal * discount
total = subtotal - discount_amount

# Check if eligible for free shipping
free_shipping_threshold = 250
eligible = total >= free_shipping_threshold

print(f"Subtotal: ${subtotal}")
print(f"Discount: ${discount_amount}")
print(f"Total: ${total}")
print(f"Free shipping: {eligible}")

# Check conditions
if total > 200 and quantity >= 2:
    print("Bonus gift included!")
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Use arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- [ ] Understand the difference between `/` and `//`
- [ ] Use assignment operators (`+=`, `-=`, `*=`, etc.)
- [ ] Compare values using comparison operators (`==`, `!=`, `>`, `<`, etc.)
- [ ] Combine conditions using logical operators (`and`, `or`, `not`)
- [ ] Check membership using `in` and `not in`
- [ ] Understand the difference between `==` and `is`
- [ ] Know operator precedence and use parentheses correctly
- [ ] Avoid common mistakes (using `=` instead of `==`)

---

## 🎯 Practice Exercises

### Exercise 1: Calculator Operations

Create a program that:
1. Takes two numbers as input
2. Performs all arithmetic operations
3. Displays the results

**Example solution:**

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponent: {a ** b}")
```

### Exercise 2: Comparison Checker

Ask for two numbers and compare them using all comparison operators.

### Exercise 3: Grade Calculator

Create a program that:
- Takes a score as input
- Uses logical operators to determine grade:
  - A: >= 90
  - B: >= 80 and < 90
  - C: >= 70 and < 80
  - F: < 70

**Example solution:**

```python
score = float(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

### Exercise 4: Membership Check

Create a list of fruits and check if a user-input fruit is in the list.

---

## 💡 Pro Tips

1. **Always use `==` for comparison, not `=`**:
   ```python
   # Wrong
   if x = 5:  # ERROR
   
   # Correct
   if x == 5:  # True
   ```

2. **Use parentheses for clarity**:
   ```python
   # Clear
   result = (a + b) * (c - d)
   ```

3. **Use `is None` instead of `== None`**:
   ```python
   # Pythonic
   if value is None:
       pass
   ```

4. **Understand division types**:
   ```python
   print(10 / 3)   # 3.333... (float)
   print(10 // 3)  # 3 (int, floor division)
   ```

5. **Use assignment operators for cleaner code**:
   ```python
   # Cleaner
   x += 5
   
   # Instead of
   x = x + 5
   ```

---

## 🚀 Next Steps

Once you've mastered operators, move on to:
- Control Flow (if/else, loops)
- Functions
- Data Structures (lists, dictionaries)
- More complex programs

---

**Happy Coding! 💻**

