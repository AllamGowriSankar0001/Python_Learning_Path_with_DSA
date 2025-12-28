# Type Casting in Python

**Type casting** means converting one data type into another. Python allows both automatic and manual type conversion, which is essential for working with different data types in your programs.

---

## 1. Why Type Casting is Needed

Type casting is necessary in several situations:

### Common Scenarios:

1. **`input()` always returns a string**
   - Even when the user enters a number, it's stored as a string
   - You need to convert it to perform calculations

2. **To perform calculations**
   - You can't add a string and a number directly
   - Type conversion makes operations possible

3. **Combining different data types**
   - Sometimes you need to convert types to work together

### Example (Without Casting):

```python
x = input("Enter a number: ")  # x is a string
print(x + 5)   # ERROR: can't concatenate str and int
```

### With Casting:

```python
x = int(input("Enter a number: "))  # Convert to int
print(x + 5)  # Works perfectly!
```

---

## 2. Types of Type Casting

### 1️⃣ Implicit Type Casting (Automatic)

Python **automatically converts** a smaller data type to a larger one when needed.

**Example:**

```python
x = 10      # int
y = 2.5     # float
z = x + y   # x is automatically converted to float
print(z)    # 12.5
print(type(z))  # <class 'float'>
```

**Characteristics:**
- ✅ No data loss
- ✅ Happens automatically
- ✅ Python handles it for you

**More examples:**

```python
# int + float = float
result = 5 + 3.14
print(result)  # 8.14
print(type(result))  # <class 'float'>

# int * float = float
product = 10 * 2.5
print(product)  # 25.0
```

### 2️⃣ Explicit Type Casting (Manual)

The **programmer converts** the data type explicitly using built-in functions.

**Example:**

```python
x = "10"
y = int(x)  # Explicitly convert string to int
print(y + 5)  # 15
```

**When to use:**
- Converting user input
- Ensuring correct data type
- Combining different types intentionally

---

## 3. Common Type Casting Functions

### int() - Convert to Integer

Converts a value to an integer.

```python
# From float to int (truncates decimal part)
x = int(3.8)
print(x)  # 3 (not 4 - it truncates!)

# From string to int
y = int("10")
print(y)  # 10

# From boolean to int
z = int(True)
print(z)  # 1
w = int(False)
print(w)  # 0
```

**❌ Invalid conversions:**

```python
int("10.5")    # ERROR: ValueError
int("abc")      # ERROR: ValueError
int(None)       # ERROR: TypeError
```

**Note:** `int()` truncates (cuts off) the decimal part, it doesn't round!

### float() - Convert to Float

Converts a value to a floating-point number.

```python
# From int to float
x = float(10)
print(x)  # 10.0

# From string to float
y = float("3.14")
print(y)  # 3.14

# From string to float (integer string)
z = float("5")
print(z)  # 5.0
```

**Examples:**

```python
price = float("99.99")
print(price)  # 99.99

temperature = float("-2.5")
print(temperature)  # -2.5
```

### str() - Convert to String

Converts a value to a string.

```python
# From int to string
x = str(100)
print(x)      # "100"
print(type(x))  # <class 'str'>

# From float to string
y = str(3.14)
print(y)  # "3.14"

# From boolean to string
z = str(True)
print(z)  # "True"
```

**Common use case:**

```python
age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old
```

### bool() - Convert to Boolean

Converts a value to a boolean (`True` or `False`).

**Truthy values** (convert to `True`):
- Non-zero numbers
- Non-empty strings
- Non-empty collections

**Falsy values** (convert to `False`):
- Zero (`0`, `0.0`)
- Empty string (`""`)
- `None`
- Empty collections (`[]`, `{}`)

**Examples:**

```python
# Numbers
print(bool(0))      # False
print(bool(1))      # True
print(bool(-5))     # True
print(bool(0.0))    # False
print(bool(3.14))   # True

# Strings
print(bool(""))     # False
print(bool("Hi"))   # True
print(bool(" "))    # True (space is not empty!)

# Collections
print(bool([]))     # False (empty list)
print(bool([1, 2])) # True (non-empty list)
print(bool({}))     # False (empty dict)

# None
print(bool(None))   # False
```

---

## 4. Type Casting with input()

This is one of the most common uses of type casting!

### Integer Input

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old")
print(type(age))  # <class 'int'>
```

### Float Input

```python
salary = float(input("Enter your salary: "))
print(f"Your salary is ${salary}")
print(type(salary))  # <class 'float'>
```

### Complete Example

```python
# Get user input and convert
name = input("Enter your name: ")  # Already a string
age = int(input("Enter your age: "))  # Convert to int
height = float(input("Enter your height (in feet): "))  # Convert to float

# Use the converted values
print(f"{name} is {age} years old and {height} feet tall")
```

---

## 5. Type Casting Between Data Types

Here's a comprehensive table showing conversions between different data types:

| From → To | Example | Result | Notes |
|-----------|---------|--------|-------|
| `int` → `float` | `float(5)` | `5.0` | Always works |
| `float` → `int` | `int(5.9)` | `5` | Truncates (cuts off decimal) |
| `int` → `str` | `str(10)` | `"10"` | Always works |
| `str` → `int` | `int("20")` | `20` | Must be valid number string |
| `str` → `float` | `float("2.5")` | `2.5` | Must be valid number string |
| `int` → `bool` | `bool(5)` | `True` | 0 = False, others = True |
| `str` → `bool` | `bool("")` | `False` | Empty = False, others = True |

**Important Notes:**

- `int(3.7)` = `3` (truncates, doesn't round)
- `int("10.5")` = **ERROR** (can't convert float string directly)
- `float("10")` = `10.0` (works fine)
- `bool("")` = `False` (empty string is falsy)
- `bool(" ")` = `True` (space is not empty!)

---

## 6. Checking Type After Casting

Always verify your type conversions using the `type()` function:

```python
x = float(10)
print(type(x))  # <class 'float'>

y = str(25)
print(type(y))  # <class 'str'>

z = int(3.14)
print(type(z))  # <class 'int'>
print(z)        # 3
```

**Practical example:**

```python
user_input = input("Enter a number: ")
print(f"Before conversion: {type(user_input)}")  # <class 'str'>

number = int(user_input)
print(f"After conversion: {type(number)}")  # <class 'int'>
```

---

## 7. Type Casting Errors (Very Important)

### ValueError

Occurs when the conversion is **invalid** or **impossible**.

**Common causes:**

```python
# Trying to convert non-numeric string to int
int("abc")        # ValueError: invalid literal for int()
int("10.5")       # ValueError: invalid literal for int()

# Trying to convert non-numeric string to float
float("hello")    # ValueError: could not convert string to float
```

**How to handle:**

```python
try:
    age = int(input("Enter age: "))
    print(f"Age: {age}")
except ValueError:
    print("Please enter a valid number!")
```

### TypeError

Occurs when the conversion function doesn't accept that type.

```python
int(None)         # TypeError: int() argument must be a string, a bytes-like object or a number
int([1, 2, 3])    # TypeError: int() argument must be a string, a bytes-like object or a number
```

---

## 📝 Complete Example: Safe Type Conversion

Here's a practical example with error handling:

```python
def get_integer_input(prompt):
    """Safely get integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_float_input(prompt):
    """Safely get float input from user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Usage
age = get_integer_input("Enter your age: ")
height = get_float_input("Enter your height: ")

print(f"You are {age} years old and {height} feet tall")
```

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Understand why type casting is needed
- [ ] Differentiate between implicit and explicit type casting
- [ ] Use `int()`, `float()`, `str()`, and `bool()` functions
- [ ] Convert user input to the correct data type
- [ ] Understand which conversions are valid and which cause errors
- [ ] Handle `ValueError` when type conversion fails
- [ ] Check types after conversion using `type()`
- [ ] Know that `int()` truncates (doesn't round) decimal numbers

---

## 🎯 Practice Exercises

### Exercise 1: Number Converter

Create a program that:
1. Takes a number as string input
2. Converts it to int and float
3. Displays both versions

**Example solution:**

```python
num_str = input("Enter a number: ")
num_int = int(float(num_str))  # Convert to float first, then int
num_float = float(num_str)

print(f"Integer: {num_int}")
print(f"Float: {num_float}")
```

### Exercise 2: Age Calculator

Ask for birth year and current year, then calculate and display age.

**Example solution:**

```python
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter current year: "))
age = current_year - birth_year

print(f"You are {age} years old")
```

### Exercise 3: Type Checker

Create a program that takes any input and tells you:
- The original type
- What types it can be converted to
- Show the conversions

---

## 💡 Pro Tips

1. **Always convert `input()` when you need numbers:**
   ```python
   # Good
   age = int(input("Age: "))
   
   # Bad
   age = input("Age: ")  # This is a string!
   ```

2. **Remember: `int()` truncates, doesn't round:**
   ```python
   int(3.9)  # 3, not 4!
   ```

3. **For float strings, convert to float first, then int:**
   ```python
   # Wrong
   int("3.5")  # ValueError
   
   # Right
   int(float("3.5"))  # 3
   ```

4. **Use `bool()` to check if values are "truthy":**
   ```python
   if bool(user_input):  # Checks if input is not empty
       print("Input provided")
   ```

5. **Handle errors gracefully:**
   ```python
   try:
       num = int(input("Enter number: "))
   except ValueError:
       print("Invalid number!")
   ```

---

## 🚀 Next Steps

Once you've mastered type casting, move on to:
- Operators (arithmetic, comparison, logical)
- Control Flow (if/else, loops)
- Functions
- More complex data structures

---

**Happy Coding! 💻**

