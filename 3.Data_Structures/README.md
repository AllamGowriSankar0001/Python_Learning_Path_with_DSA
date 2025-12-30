

---

## 1\. What is a list in Python?

A **list** is an **ordered, mutable collection** of items.

```python
my_list = [1, 2, 3, "apple", True]
```

### Key properties

-   **Ordered** → items keep their position
    
-   **Mutable** → you can change, add, or remove items
    
-   **Allows duplicates**
    
-   **Can store mixed data types**
    

---

## 2\. Creating lists

```python
a = []                      # empty list
b = [1, 2, 3]
c = list((4, 5, 6))         # from tuple
d = ["a", "b", "c"]
```

---

## 3\. Accessing list items

```python
nums = [10, 20, 30, 40]

nums[0]     # 10
nums[-1]    # 40 (last item)
```

### Slicing

```python
nums[1:3]   # [20, 30]
nums[:2]    # [10, 20]
nums[::2]   # [10, 30]
```

---

## 4\. Modifying lists

```python
nums[1] = 25
nums.append(50)
nums.remove(10)
```

---

## 5\. All Python list methods (complete)

Python provides **11 built-in list methods**.

---

### 1\. `append(x)`

Adds one item to the **end** of the list.

```python
lst = [1, 2]
lst.append(3)
# [1, 2, 3]
```

---

### 2\. `extend(iterable)`

Adds **multiple items** from another iterable.

```python
lst = [1, 2]
lst.extend([3, 4])
# [1, 2, 3, 4]
```

✅ Difference from `append`:

```python
lst.append([5, 6])   # adds as ONE item
```

---

### 3\. `insert(index, x)`

Inserts an item at a specific position.

```python
lst = [1, 3]
lst.insert(1, 2)
# [1, 2, 3]
```

---

### 4\. `remove(x)`

Removes the **first occurrence** of a value.

```python
lst = [1, 2, 2, 3]
lst.remove(2)
# [1, 2, 3]
```

❌ Error if value not found.

---

### 5\. `pop(index=-1)`

Removes and **returns** an item.

```python
lst = [1, 2, 3]
lst.pop()     # 3
lst.pop(0)    # 1
```

---

### 6\. `clear()`

Removes all items.

```python
lst = [1, 2, 3]
lst.clear()
# []
```

---

### 7\. `index(x, start=0, end=len)`

Returns index of first occurrence.

```python
lst = [10, 20, 30]
lst.index(20)   # 1
```

❌ Error if not found.

---

### 8\. `count(x)`

Counts how many times a value appears.

```python
lst = [1, 2, 2, 3]
lst.count(2)   # 2
```

---

### 9\. `sort(key=None, reverse=False)`

Sorts the list **in place**.

```python
lst = [3, 1, 2]
lst.sort()
# [1, 2, 3]
```

Reverse:

```python
lst.sort(reverse=True)
```

With key:

```python
words = ["apple", "kiwi", "banana"]
words.sort(key=len)
```

---

### 10\. `reverse()`

Reverses the list **in place**.

```python
lst = [1, 2, 3]
lst.reverse()
# [3, 2, 1]
```

---

### 11\. `copy()`

Creates a **shallow copy**.

```python
lst = [1, 2, 3]
new_lst = lst.copy()
```

---

## 6\. Built-in functions that work with lists

(Not methods, but commonly used)

```python
len(lst)       # number of items
max(lst)       # largest value
min(lst)       # smallest value
sum(lst)       # sum of items
sorted(lst)    # returns new sorted list
```

---

## 7\. Looping through lists

```python
for item in lst:
    print(item)
```

With index:

```python
for i, v in enumerate(lst):
    print(i, v)
```

---

## 8\. List comprehension (important)

Short, powerful way to create lists.

```python
squares = [x**2 for x in range(5)]
```

With condition:

```python
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 9\. Nested lists

```python
matrix = [
    [1, 2],
    [3, 4]
]

matrix[1][0]   # 3
```

