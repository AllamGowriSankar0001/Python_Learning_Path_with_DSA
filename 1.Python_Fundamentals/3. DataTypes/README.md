# Data Types in Python

A **data type** defines the kind of value a variable can store. Python automatically decides the data type when a value is assigned to a variable — you don't need to declare it explicitly!

---

## 1. int (Integer)

Stores **whole numbers** (no decimal point).

- Can be positive, negative, or zero
- Used for counting and discrete values

**Examples:**

```python
x = 10
y = -5
z = 0
```

**Common uses:**
- Counting items
- Age
- Number of students
- Index positions

---

## 2. float (Floating-Point Number)

Stores **decimal numbers** (values with fractions).

- Used for precise measurements and calculations
- Can be positive or negative

**Examples:**

```python
pi = 3.14
price = 99.99
temperature = -2.5
height = 5.6
```

**Common uses:**
- Measurements (height, weight, distance)
- Prices and money
- Scientific values
- Percentages

---

## 3. str (String)

Stores **text or characters**.

- Enclosed in single quotes (`'`) or double quotes (`"`)
- Can contain letters, numbers, symbols, and spaces

**Examples:**

```python
name = "Python"
message = 'Hello World'
greeting = "Hello, I'm learning Python!"
```

**String Concatenation:**

You can combine strings using the `+` operator:

```python
greeting = "Hello " + "Python"
print(greeting)  # Hello Python

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe
```

**Common uses:**
- Names and labels
- Messages and descriptions
- File paths
- User input

---

## 4. bool (Boolean)

Stores only **two values**: `True` or `False`.

- Used for conditions and logical decisions
- Essential for control flow (if/else statements)

**Examples:**

```python
is_student = True
is_logged_in = False
has_permission = True
is_empty = False
```

**Common uses:**
- `if` conditions
- Comparisons (`x > 5`)
- Logical operations (`and`, `or`, `not`)
- Flags and status indicators

**Note:** In Python, `True` and `False` must be capitalized!

---

## 5. type() Function (Very Important)

The `type()` function is used to **check the data type** of a variable.

**Syntax:**

```python
type(variable_name)
```

**Examples:**

```python
x = 10
print(type(x))        # <class 'int'>

y = 3.14
print(type(y))        # <class 'float'>

name = "Python"
print(type(name))     # <class 'str'>

is_active = True
print(type(is_active)) # <class 'bool'>
```

**Why it's useful:**
- Debugging: Check what type your variable actually is
- Learning: Understand how Python interprets your values
- Validation: Ensure variables have the expected type

---

## 6. Dynamic Typing Reminder

Python allows a variable to **change its data type** during execution. This is called dynamic typing.

**Example:**

```python
x = 10
print(type(x))        # <class 'int'>

x = "Ten"
print(type(x))        # <class 'str'>

x = 3.14
print(type(x))        # <class 'float'>
```

✅ **Same variable, different data types** — Python handles this automatically!

**Important:** While this is flexible, it's generally good practice to keep variables consistent in type for clarity and to avoid bugs.

---

## 7. Type Conversion (Type Casting)

You can **convert between data types** using built-in functions. This is called type casting.

### Converting to Integer

```python
x = int(3.5)      # 3 (truncates decimal)
y = int("10")     # 10 (string to int)
z = int(True)     # 1 (True = 1, False = 0)
```

### Converting to Float

```python
x = float(10)     # 10.0
y = float("3.14") # 3.14
z = float(5)      # 5.0
```

### Converting to String

```python
x = str(100)      # "100"
y = str(3.14)     # "3.14"
z = str(True)     # "True"
```

### Converting to Boolean

```python
x = bool(1)       # True
y = bool(0)       # False
z = bool("")      # False (empty string)
w = bool("Hello") # True (non-empty string)
```

**Common use cases:**
- Converting user input (which comes as string) to numbers
- Formatting numbers for display
- Type validation and error handling

---

## 📊 Quick Reference Table

| Data Type | Example | Description |
|-----------|---------|-------------|
| `int` | `x = 10` | Whole numbers |
| `float` | `y = 3.14` | Decimal numbers |
| `str` | `name = "Python"` | Text/characters |
| `bool` | `is_active = True` | True or False |

---

## ✅ Quick Check

After completing this section, you should be able to:

- [ ] Identify the four main data types (int, float, str, bool)
- [ ] Create variables of each data type
- [ ] Use the `type()` function to check variable types
- [ ] Understand that Python is dynamically typed
- [ ] Convert between different data types
- [ ] Combine strings using concatenation
- [ ] Know when to use each data type appropriately

---

## 🎯 Practice Exercise

Try these exercises to test your understanding:

1. **Create variables of each type:**
   ```python
   # Your code here
   age = ?
   height = ?
   name = ?
   is_student = ?
   ```

2. **Check their types:**
   ```python
   # Print the type of each variable
   ```

3. **Type conversions:**
   ```python
   # Convert "25" to an integer
   # Convert 100 to a string
   # Convert 5 to a float
   ```

4. **String operations:**
   ```python
   # Combine "Hello" and "World" into one string
   ```

**Example solution:**

```python
# 1. Create variables
age = 25
height = 5.9
name = "Alice"
is_student = True

# 2. Check types
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>

# 3. Type conversions
age_str = int("25")
number_str = str(100)
decimal = float(5)

# 4. String operations
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World
```

---

## 💡 Pro Tips

1. **Use meaningful variable names** that indicate the data type (e.g., `age` for int, `price` for float)

2. **Be careful with type conversions:**
   - `int(3.7)` gives `3` (truncates, doesn't round)
   - `int("abc")` will cause an error (can't convert text to number)

3. **String vs Number:**
   - `"10" + "5"` = `"105"` (string concatenation)
   - `10 + 5` = `15` (addition)

4. **Boolean truthiness:**
   - `bool(0)` = `False`
   - `bool(1)` = `True`
   - `bool("")` = `False` (empty string)
   - `bool("anything")` = `True` (non-empty string)

---

## 🚀 Next Steps

Once you've mastered data types, move on to:
- Input/Output operations
- Operators (arithmetic, comparison, logical)
- Control Flow (if/else, loops)
- More complex data structures (lists, dictionaries)

---

**Happy Learning! 💻**

