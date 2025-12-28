# Variables in Python

A **variable** is a name that refers to a value stored in memory. In Python, variables are used to store data so it can be reused and manipulated throughout your program.

---

## 1. Creating Variables

You do **not** need to declare a variable's type in Python. A variable is created when you assign a value to it.

```python
x = 10
name = "Alice"
price = 99.5
```

That's it! Python automatically knows what type of data you're storing.

---

## 2. Dynamic Typing (Very Important)

Python is **dynamically typed**, meaning:

- The type of a variable is decided at runtime
- A variable can change its type during execution

**Example:**

```python
x = 10        # x is an integer
x = 3.14      # x is now a float
x = "Python"  # x is now a string
```

✅ **No type declaration needed**  
✅ **Flexible and beginner-friendly**

---

## 3. Naming Rules for Variables

Python has strict naming rules that you must follow:

### ✅ Allowed

- Must start with a letter (a–z, A–Z) or underscore (`_`)
- Can contain letters, numbers, and underscores
- **Case-sensitive** (`age` ≠ `Age`)

**Examples:**

```python
age = 25
_name = "Bob"
total_marks = 450
studentName = "Alice"  # camelCase works too
```

### ❌ Not Allowed

- Cannot start with a number
- Cannot contain spaces or special characters
- Cannot use Python keywords

**❌ Invalid examples:**

```python
2name = "Tom"      # ❌ starts with number
total marks = 90    # ❌ space not allowed
class = 10          # ❌ 'class' is a keyword
my-name = "John"    # ❌ hyphen not allowed
```

---

## 4. Python Keywords (Cannot Be Variable Names)

These are **reserved words** that have special meanings in Python. You cannot use them as variable names.

**Common keywords:**

```python
if, else, for, while, True, False, None, class, def, return, 
import, from, in, is, and, or, not, break, continue, pass
```

**Tip:** If you're unsure whether a word is a keyword, try using it as a variable name. Python will give you an error if it's reserved.

---

## 5. Assigning Multiple Variables

### a) Multiple Assignment

Assign different values to multiple variables in one line:

```python
a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3
```

### b) Same Value to Multiple Variables

Assign the same value to multiple variables:

```python
x = y = z = 0
print(x, y, z)  # 0 0 0
```

---

## 6. Variable Types (Common Data Types)

Python variables can store different types of data:

| Type | Example | Description |
|------|---------|-------------|
| `int` | `x = 10` | Integer (whole numbers) |
| `float` | `pi = 3.14` | Floating-point (decimal numbers) |
| `str` | `name = "Python"` | String (text) |
| `bool` | `is_active = True` | Boolean (True/False) |
| `NoneType` | `value = None` | None (represents absence of value) |

### Checking Variable Type

You can check the type of a variable using the `type()` function:

```python
x = 10
print(type(x))  # <class 'int'>

name = "Python"
print(type(name))  # <class 'str'>

is_active = True
print(type(is_active))  # <class 'bool'>
```

---

## 7. Type Conversion (Type Casting)

You can convert one type to another using built-in functions:

```python
# String to integer
x = int("10")
print(x)        # 10
print(type(x)) # <class 'int'>

# Integer to float
y = float(5)
print(y)        # 5.0
print(type(y))  # <class 'float'>

# Number to string
z = str(100)
print(z)        # "100"
print(type(z))  # <class 'str'>
```

**Common conversion functions:**
- `int()` - Convert to integer
- `float()` - Convert to float
- `str()` - Convert to string
- `bool()` - Convert to boolean

---

## 8. Variable Scope (Basic Idea)

### Local Variable

- Defined inside a function
- Accessible only within that function

### Global Variable

- Defined outside all functions
- Accessible everywhere in the program

**Example:**

```python
x = 10  # global variable

def show():
    y = 5  # local variable
    print(f"Local y: {y}")
    print(f"Global x: {x}")

show()
# Output:
# Local y: 5
# Global x: 10

print(x)  # ✅ Works - x is global
# print(y)  # ❌ Error - y is local to the function
```

---

## 9. Good Naming Practices (Best Practices)

Follow these guidelines to write clean, readable code:

### ✅ Good Practices

- Use **meaningful names** that describe what the variable stores
- Use **lowercase letters** for variable names
- Use **underscores** for multi-word names (snake_case)

**Good examples:**

```python
total_price = 500
student_name = "John"
is_logged_in = True
number_of_students = 25
```

### ❌ Bad Practices

- Avoid single letters (unless in loops)
- Avoid abbreviations that aren't clear
- Avoid names that don't describe the purpose

**Bad examples:**

```python
tp = 500              # What is 'tp'?
sn = "John"           # What is 'sn'?
x = True              # What does 'x' represent?
```

**Remember:** Code is read more often than it's written. Make it easy to understand!

---

## 10. Deleting Variables

You can delete a variable using the `del` keyword:

```python
x = 10
print(x)  # 10

del x
print(x)  # ❌ Error: name 'x' is not defined
```

**Note:** This is rarely needed in practice, but it's useful to know it exists.

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Create variables and assign values to them
- [ ] Understand that Python is dynamically typed
- [ ] Follow Python's variable naming rules
- [ ] Know which words are Python keywords
- [ ] Assign multiple variables in different ways
- [ ] Identify common data types (int, float, str, bool)
- [ ] Check the type of a variable using `type()`
- [ ] Convert between different data types
- [ ] Understand the basic concept of variable scope
- [ ] Write variables using good naming practices

---

## 🎯 Practice Exercise

Try creating these variables:

1. Store your name in a variable
2. Store your age as an integer
3. Store your height as a float
4. Store whether you're a student (True/False)
5. Check the type of each variable
6. Convert your age to a string and print it

**Example solution:**

```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>

age_as_string = str(age)
print(f"My name is {name} and I am {age_as_string} years old")
```

---

## 🚀 Next Steps

Once you've mastered variables, move on to:
- Data Types (deep dive)
- Input/Output operations
- Operators
- Control Flow (if/else, loops)

---

**Happy Coding! 💻**

