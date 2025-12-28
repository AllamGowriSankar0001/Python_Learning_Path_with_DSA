# Input / Output in Python

Input and Output allow a program to **interact with the user**:

- **Input** → taking data from the user
- **Output** → displaying results to the user

These are fundamental skills for creating interactive Python programs!

---

## 1. input() Function (Taking Input)

The `input()` function is used to accept input from the user.

### Basic Syntax

```python
variable = input("message")
```

**Example:**

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Important:** 👉 Whatever the user enters is **always stored as a string** (`str`), even if they type a number!

```python
age = input("Enter your age: ")
print(type(age))  # <class 'str'> (not int!)
```

---

## 2. Input with Type Conversion

Since `input()` returns a string, you **must convert it** if you want to use it as a number.

### Integer Input

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old")
print(type(age))  # <class 'int'>
```

### Float Input

```python
price = float(input("Enter price: "))
total = price * 1.1  # Add 10% tax
print(f"Total with tax: {total}")
```

### Common Mistake

**❌ Without conversion:**

```python
x = input("Enter a number: ")
print(x + 5)  # ERROR: can't add string and int
```

**✅ With conversion:**

```python
x = int(input("Enter a number: "))
print(x + 5)  # Works perfectly!
```

---

## 3. Multiple Inputs

### Method 1: Using Multiple input() Calls

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
sum_result = a + b
print(f"Sum: {sum_result}")
```

### Method 2: Using split() (Advanced but Useful)

```python
# User enters: 10 20
a, b = map(int, input("Enter two numbers: ").split())
print(f"a = {a}, b = {b}")
```

**How it works:**
- `input()` gets the string: `"10 20"`
- `.split()` splits by space: `["10", "20"]`
- `map(int, ...)` converts each to integer: `[10, 20]`
- `a, b = ...` unpacks into two variables

**Example with more values:**

```python
# User enters: 10 20 30
x, y, z = map(int, input("Enter three numbers: ").split())
```

---

## 4. print() Function (Displaying Output)

The `print()` function is used to display output on the screen.

### Basic Syntax

```python
print(value)
```

**Example:**

```python
print("Hello, Python")
print(42)
print(3.14)
```

**Output:**

```
Hello, Python
42
3.14
```

---

## 5. Printing Multiple Values

You can print multiple values separated by commas:

```python
name = "Alice"
age = 20
city = "New York"

print(name, age, city)
```

**Output:**

```
Alice 20 New York
```

**Note:** By default, values are separated by a space.

---

## 6. sep Parameter (Separator)

Used to **change the separator** between printed values.

```python
print("2025", "12", "28", sep="-")
```

**Output:**

```
2025-12-28
```

**More examples:**

```python
print("Python", "is", "awesome", sep=" ")      # Python is awesome
print("Python", "is", "awesome", sep="***")   # Python***is***awesome
print(1, 2, 3, sep=", ")                       # 1, 2, 3
```

---

## 7. end Parameter

Controls **what is printed at the end** (default is newline `\n`).

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```
Hello World
```

**More examples:**

```python
print("Loading", end="...")
print("Complete")
# Output: Loading...Complete

print("First line", end="")
print("Second line")
# Output: First lineSecond line
```

---

## 8. Printing with Variables (Formatted Output)

There are several ways to print variables with text:

### Method 1: Using Commas (Simple)

```python
name = "Alice"
age = 20
print("Name:", name, "Age:", age)
```

**Output:** `Name: Alice Age: 20`

### Method 2: Using + (Only for Strings)

```python
name = "Alice"
print("Name: " + name)
```

**⚠️ Warning:** This only works with strings. If you try to add a number, you'll get an error:

```python
age = 20
print("Age: " + age)  # ERROR: can't concatenate str and int
```

**Fix:** Convert to string first:

```python
age = 20
print("Age: " + str(age))  # Works!
```

### Method 3: Using f-strings (Best & Modern) ⭐

```python
name = "Alice"
age = 20
print(f"Name: {name}, Age: {age}")
```

**Output:** `Name: Alice, Age: 20`

**Why f-strings are great:**
- ✅ Easy to read
- ✅ Works with all data types
- ✅ Can include expressions

**More f-string examples:**

```python
x = 10
y = 5
print(f"Sum: {x + y}")           # Sum: 15
print(f"Product: {x * y}")       # Product: 50
print(f"x is {x}, y is {y}")     # x is 10, y is 5
```

---

## 9. Escape Characters in print()

Escape characters allow you to include special characters in strings.

| Escape | Meaning | Example |
|--------|---------|---------|
| `\n` | New line | `print("Hello\nPython")` |
| `\t` | Tab | `print("Hello\tPython")` |
| `\"` | Double quote | `print("He said \"Hello\"")` |
| `\\` | Backslash | `print("Path: C:\\Users")` |

**Examples:**

```python
print("Hello\nPython")
# Output:
# Hello
# Python

print("Name:\tAlice")
# Output: Name:    Alice

print("He said \"Hello\"")
# Output: He said "Hello"

print("Path: C:\\Users\\Documents")
# Output: Path: C:\Users\Documents
```

---

## 10. Common Errors (Important)

### ❌ Error 1: Forgetting Type Conversion

```python
age = input("Enter age: ")
if age > 18:  # ERROR: comparing string with int
    print("Adult")
```

**✅ Correct:**

```python
age = int(input("Enter age: "))
if age > 18:
    print("Adult")
```

### ❌ Error 2: Using + with String and Number

```python
age = 20
print("Age: " + age)  # ERROR: can't concatenate str and int
```

**✅ Correct:**

```python
age = 20
print("Age:", age)              # Method 1: Use comma
print("Age: " + str(age))       # Method 2: Convert to string
print(f"Age: {age}")            # Method 3: Use f-string (best)
```

### ❌ Error 3: Wrong Indentation

```python
name = input("Enter name: ")
    print(name)  # ERROR: unexpected indentation
```

**✅ Correct:**

```python
name = input("Enter name: ")
print(name)  # No indentation needed here
```

---
---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Use `input()` to get user input
- [ ] Understand that `input()` always returns a string
- [ ] Convert input to integers and floats
- [ ] Use `print()` to display output
- [ ] Print multiple values with commas
- [ ] Use `sep` and `end` parameters
- [ ] Format output using f-strings
- [ ] Use escape characters (`\n`, `\t`, etc.)
- [ ] Avoid common input/output errors
- [ ] Create interactive programs

---

## 🎯 Practice Exercises

### Exercise 1: Personal Information Form

Create a program that asks for:
- Name
- Age
- City
- Favorite color

Then display all information in a formatted way.

**Example solution:**

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
color = input("Enter your favorite color: ")

print(f"\n=== Your Information ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Favorite Color: {color}")
```

### Exercise 2: Number Operations

Ask for two numbers and display:
- Their sum
- Their difference
- Their product
- Their quotient

### Exercise 3: Temperature Converter

Ask for temperature in Celsius and convert it to Fahrenheit.

**Formula:** `F = (C * 9/5) + 32`

---

## 💡 Pro Tips

1. **Always convert input when you need numbers:**
   ```python
   # Good
   age = int(input("Age: "))
   
   # Bad
   age = input("Age: ")  # This is a string!
   ```

2. **Use f-strings for formatted output:**
   ```python
   # Best practice
   print(f"Name: {name}, Age: {age}")
   ```

3. **Add helpful prompts:**
   ```python
   # Good
   age = int(input("Enter your age (in years): "))
   
   # Less helpful
   age = int(input("Age: "))
   ```

4. **Handle errors gracefully:**
   ```python
   try:
       age = int(input("Enter age: "))
   except ValueError:
       print("Please enter a valid number!")
   ```

---

## 🚀 Next Steps

Once you've mastered Input/Output, move on to:
- Operators (arithmetic, comparison, logical)
- Control Flow (if/else, loops)
- Functions
- Error handling (try/except)

---

**Happy Coding! 💻**

