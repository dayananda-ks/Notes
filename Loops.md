# Python `for` Loop

The `for` loop is used when we want to execute a block of statements repeatedly.

In Python, the `for` loop can be used mainly in two ways:

1. **`for` loop with `range()`**

2. **`for` loop without `range()` using an iterable**

---

# 1. `for` Loop with `range()`

`range()` is commonly used when we want to generate a sequence of numbers.

## Syntax


```python
for var_name in range(start, end, step):
    # logic
```

### Important Point

The `end` value in `range()` is **excluded**.

For example:

```python
range(1, 5)
```

produces:

```text
1 2 3 4
```

It does **not** produce `5`.

---

# 2. Incrementing Loop

An incrementing loop moves from a smaller value to a larger value.

### Syntax

```python
for var_name in range(start, end, positive_step):
    # logic
```

## Rules for an Incrementing Loop

### Rule 1 — Step should be positive

For an incrementing loop, the step should be positive.

Example:

```python
range(1, 10, 1)
```

Here:

```text
start = 1
step  = +1
```

---

### Rule 2 — Start should be less than the mentioned end

```text
start < mentioned_end
```

Example:

```python
range(1, 5, 1)
```

Here:

```text
1 < 5
```

Therefore, the loop can move forward.

---

### Rule 3 — To include the actual end value

If the actual end value also needs to be included in the sequence:

```text
mentioned_end = actual_end + 1
```

### Example

Suppose we want:

```text
1 2 3 4 5
```

The actual end is:

```text
5
```

But `range()` excludes the end value.

Therefore:

```python
for i in range(1, 6, 1):
    print(i, end=" ")
```

Output:

```text
1 2 3 4 5
```

Because:

```text
actual end = 5
mentioned end = 5 + 1 = 6
```

---

# 3. Understanding `range()` in an Incrementing Loop

Consider:

```python
for i in range(1, 5, 1):
    print(i, end=" ")
```

Execution:

```text
Start = 1
End   = 5
Step  = +1
```

The values generated are:

```text
1 → 2 → 3 → 4
```

When `i` becomes `5`, the loop stops because the end value is excluded.

Output:

```text
1 2 3 4
```

---

# 4. Decrementing Loop

A decrementing loop moves from a larger value to a smaller value.

### Syntax

```python
for var_name in range(start, end, negative_step):
    # logic

# remaining statements
```

The step must be negative.

---

## Example

### Problem

Write a program to display:

```text
-5 -6 -7 -8
```

in decrementing order.

### Expected Output

```text
-5 -6 -7 -8
```

We have:

```text
start     = -5
actual end = -8
step      = -1
```

Since `range()` excludes the end value, we need to mention:

```text
actual end - 1
```

For negative numbers:

```text
-8 - 1 = -9
```

Therefore:

```python
for i in range(-5, -9, -1):
    print(i, end=" ")

print("\nLast Updated i:", i)
```

Output:

```text
-5 -6 -7 -8
Last Updated i: -8
```

---

# 5. Rules for a Decrementing Loop

### Rule 1 — Step must be negative

A decrementing loop must use a negative step.

Example:

```python
range(10, 1, -1)
```

Here:

```text
step = -1
```

---

### Rule 2 — Start should be greater than the mentioned end

For a decrementing loop:

```text
start > mentioned_end
```

Example:

```python
range(10, 5, -1)
```

Here:

```text
10 > 5
```

Therefore, the loop can move backwards.

---

### Rule 3 — To include the actual end value

If the actual end value also needs to be included:

```text
mentioned_end = actual_end - 1
```

### Example

Suppose we want:

```text
10 9 8 7 6 5
```

The actual end is:

```text
5
```

Because `range()` excludes the end value, we mention:

```text
5 - 1 = 4
```

Therefore:

```python
for i in range(10, 4, -1):
    print(i, end=" ")
```

Output:

```text
10 9 8 7 6 5
```

---

# 6. Incrementing vs Decrementing Loop

| Feature | Incrementing | Decrementing |
|---|---|---|
| Direction | Small → Large | Large → Small |
| Step | Positive | Negative |
| Start condition | `start < end` | `start > end` |
| Include actual end | `actual_end + 1` | `actual_end - 1` |
| Example | `range(1, 6, 1)` | `range(5, 0, -1)` |

---

# 7. `for` Loop Without `range()`

A `for` loop does not always require `range()`.

Python's `for` loop can directly iterate over an **iterable object**.

### Syntax

```python
for var_name in iterable:
    # logic

# remaining statements
```

An **iterable** is an object whose elements can be accessed one by one.

Examples of iterables:

```text
List
Tuple
String
Set
Dictionary
Range
```

---

# 8. Iterating Through a List

Consider:

```python
arr = ["daya", 55, 10]

for i in arr:
    print(i)
```

Output:

```text
daya
55
10
```

### How it works

The variable `i` receives one element at a time.

```text
i = "daya"
i = 55
i = 10
```

Therefore:

```python
print(i)
```

prints each element.

---

# 9. Iterating Through Multiple Values

Python allows multiple values to be written as a tuple.

```python
for i in (1, 2, 3, 4, "saoik"):
    print(i)
```

Output:

```text
1
2
3
4
saoik
```

Each value is accessed one by one.

---

# 10. Tuple and `for` Loop

Consider:

```python
n = (1, 2, 1)

for i in n:
    print(type(n))
```

Output:

```text
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
```

Why?

Because:

```python
type(n)
```

checks the type of `n`, not the type of `i`.

The value of `n` is:

```python
(1, 2, 1)
```

which is a tuple.

If we want to check the type of each element, use:

```python
n = (1, 2, 1)

for i in n:
    print(type(i))
```

Output:

```text
<class 'int'>
<class 'int'>
<class 'int'>
```

---

# 11. Why `for i in 100:` Does Not Work

Consider:

```python
for i in 100:
    print(i)
```

This produces an error.

Why?

Because `100` is an integer.

An integer is **not iterable**.

Python expects something that can provide elements one by one.

For example:

```python
for i in [100]
    print(i)
```

works because a list is iterable.

Output:

```text
100
```

---

# 12. Multiple Values Can Be Iterated

This is valid:

```python
for i in (100, 2, 25):
    print(i, end=" ")
```

Output:

```text
100 2 25
```

The tuple contains three elements:

```text
100
2
25
```

The loop accesses them one by one.

---

# 13. Negative Values Do Not Automatically Mean Decrementing

Consider:

```python
for i in (100, 2, -25):
    print(i, end=" ")
```

Output:

```text
100 2 -25
```

This is **not a decrementing loop**.

Why?

Because these are simply three values stored in a tuple:

```text
100
2
-25
```

The `for` loop is just visiting each element.

There is no concept of:

```text
start
end
step
```

when directly iterating over a tuple.

---

# 14. `range()` vs Iterable

It is important to understand the difference.

### Using `range()`

```python
for i in range(1, 5):
    print(i)
```

Here Python generates a sequence:

```text
1 2 3 4
```

---

### Using a list

```python
for i in [1, 2, 3, 4]:
    print(i)
```

Here Python directly accesses the elements already stored in the list.

---

### Using a tuple

```python
for i in (1, 2, 3, 4):
    print(i)
```

Here Python directly accesses the elements of the tuple.

---

# 15. Important Concept

The following:

```python
for i in range(1, 5):
```

means:

> Generate/access numbers from the `range` object one by one.

While:

```python
for i in [1, 2, 3, 4]:
```

means:

> Access each element of the list one by one.

And:

```python
for i in "Python":
```

means:

> Access each character of the string one by one.

---

# 16. String as an Iterable

A string is also iterable.

```python
name = "Daya"

for i in name:
    print(i)
```

Output:

```text
D
a
y
a
```

Each character is accessed individually.

---

# 17. `for` Loop Mental Model

The easiest way to understand a Python `for` loop is:

```text
for variable in iterable:
        ↓
Take one element
        ↓
Store it in variable
        ↓
Execute loop body
        ↓
Take next element
        ↓
Repeat until no elements remain
```

For example:

```python
arr = ["daya", 55, 10]

for i in arr:
    print(i)
```

Execution:

```text
First iteration:
i = "daya"

Second iteration:
i = 55

Third iteration:
i = 10

No more elements → loop ends
```

---

# 18. Key Rules to Remember

## Incrementing `range()`

```python
range(start, end, +step)
```

Rules:

```text
1. Step should be positive.
2. start < mentioned_end.
3. End value is excluded.
4. To include actual end:
   mentioned_end = actual_end + 1
```

Example:

```python
range(1, 6, 1)
```

Output:

```text
1 2 3 4 5
```

---

## Decrementing `range()`

```python
range(start, end, -step)
```

Rules:

```text
1. Step should be negative.
2. start > mentioned_end.
3. End value is excluded.
4. To include actual end:
   mentioned_end = actual_end - 1
```

Example:

```python
range(5, 0, -1)
```

Output:

```text
5 4 3 2 1
```

---

## `for` Without `range()`

```python
for variable in iterable:
    # logic
```

The iterable can be:

```text
List
Tuple
String
Set
Dictionary
Range
```

Example:

```python
for i in ["Daya", 55, 10]:
    print(i)
```

---

# 19. Common Mistakes

### Mistake 1 — Using an integer directly

```python
for i in 100:
    print(i)
```

Invalid because `100` is not iterable.

Use:

```python
for i in range(100):
    print(i)
```

or:

```python
for i in [100]:
    print(i)
```

depending on what you want.

---

### Mistake 2 — Using the wrong loop variable

Incorrect:

```python
for i in (100, 2, 25):
    print(j)
```

`j` was never defined.

Correct:

```python
for i in (100, 2, 25):
    print(i)
```

---

### Mistake 3 — Forgetting that `range()` excludes the end

```python
range(1, 5)
```

does **not** produce:

```text
1 2 3 4 5
```

It produces:

```text
1 2 3 4
```

To include `5`:

```python
range(1, 6)
```

---

# 20. Quick Revision

```text
                Python for Loop
                       |
          ┌────────────┴────────────┐
          |                         |
      With range()             Without range()
          |                         |
     start/end/step              Iterable
          |                         |
     ┌────┴────┐              ┌────┼─────┐
     |         |              |    |     |
 Increment  Decrement       List Tuple String
     |         |
 +ve step   -ve step
```

### Remember

```text
Increment:
start < end
step = positive
include end → actual_end + 1

Decrement:
start > end
step = negative
include end → actual_end - 1

Without range():
for variable in iterable
```

The most important idea is:

> **`range()` generates a sequence based on start, end, and step, while a normal `for` loop can directly visit the elements of an iterable one by one.**