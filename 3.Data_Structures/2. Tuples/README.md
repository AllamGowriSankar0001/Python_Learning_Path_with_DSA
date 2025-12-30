

---

## 1\. Tuples in Python 

### What is a tuple?

A **tuple** is a built-in Python data type used to store **multiple values in a single variable**, just like a list.

```python
t = (1, 2, 3)
```

### Key characteristics of tuples

| Feature | Tuple |
| --- | --- |
| Ordered | ✅ Yes |
| Indexed | ✅ Yes |
| Allows duplicates | ✅ Yes |
| Mutable (changeable) | ❌ No |
| Faster than list | ✅ Yes |
| Uses parentheses | `()` |

---

### Creating tuples

```python
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.5)
```

**Single-item tuple (important!)**

```python
t = (5,)   # comma is required
```

Without comma → not a tuple:

```python
t = (5)    # int, not tuple
```

---

### Accessing tuple elements

```python
t = (10, 20, 30)

print(t[0])     # 10
print(t[-1])    # 30
```

### Slicing

```python
t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)
```

---

### Tuples are **immutable**

You **cannot change** values:

```python
t = (1, 2, 3)
t[0] = 10   # ❌ ERROR
```

But you *can*:

-   Convert tuple → list
    
-   Modify list
    
-   Convert back to tuple
    

```python
t = (1, 2, 3)
lst = list(t)
lst[0] = 10
t = tuple(lst)
```

---

### Looping through a tuple

```python
t = (1, 2, 3)

for x in t:
    print(x)
```

---

### Tuple packing & unpacking

```python
# Packing
t = 1, 2, 3

# Unpacking
a, b, c = t
print(a, b, c)
```

---

### Why use tuples?

-   Data should **not change**
    
-   Faster than lists
    
-   Used for **fixed collections** (coordinates, RGB values)
    
-   Used as **dictionary keys**
    

```python
point = (3, 4)
```

---

## 2\. All Tuple Methods

Tuples have **only 2 built-in methods** (because they are immutable):

### 1\. `count()`

Returns how many times a value appears.

```python
t = (1, 2, 2, 3)
print(t.count(2))   # 2
```

---

### 2\. `index()`

Returns the index of the first occurrence.

```python
t = (10, 20, 30)
print(t.index(20))  # 1
```

❌ Error if value not found.

---

### Built-in functions that work with tuples

```python
t = (1, 2, 3)

len(t)      # 3
max(t)      # 3
min(t)      # 1
sum(t)      # 6
sorted(t)   # [1, 2, 3] → returns list
```

---

## 3\. List Methods vs Tuple Methods (Important)

### Why tuples don’t have list methods?

Because **tuples cannot change**.

---

### Common **list-only methods** (❌ not in tuples)

| Method | Purpose |
| --- | --- |
| append() | Add item |
| extend() | Add multiple items |
| insert() | Insert at position |
| remove() | Remove item |
| pop() | Remove by index |
| clear() | Remove all |
| sort() | Sort list |
| reverse() | Reverse list |

Example (list only):

```python
lst = [1, 2, 3]
lst.append(4)
```

Trying this on tuple:

```python
t = (1, 2, 3)
t.append(4)   # ❌ ERROR
```

---

### Methods common to **both lists and tuples**

| Method | Works on tuple? |
| --- | --- |
| count() | ✅ |
| index() | ✅ |
| len() | ✅ |
| slicing | ✅ |
| iteration | ✅ |

---
