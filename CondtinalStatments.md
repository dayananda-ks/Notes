# Python — Conditional Statements

Conditional statements are used when a program needs to **make decisions**.

A program does not always execute every statement in the same way. Depending on a condition, it may:

- Execute some statements
- Skip some statements
- Choose between two alternatives
- Choose one option from multiple possibilities
- Check another condition inside an existing condition

---

# 1. Why Do We Need Conditional Statements?

Consider a real-world example:

> A person can vote only if their age is 18 or above.

The program needs to check:

```text
Is age >= 18?
```

If the answer is `True`:

```text
Person can vote
```

If the answer is `False`:

```text
Person cannot vote
```

This decision-making ability is provided by **conditional statements**.

---

# 2. Basic Structure of a Condition

A condition generally produces a Boolean result:

```text
True
```

or

```text
False
```

Example:

```python
age = 20

age >= 18
```

The condition:

```python
age >= 18
```

is evaluated as:

```text
20 >= 18
```

Therefore:

```text
True
```

---

# 3. Boolean Values in Python

Python has two Boolean values:

```python
True
False
```

Notice that the first letter is uppercase.

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

---

# 4. Comparison Operators

Comparison operators are commonly used to create conditions.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

---

# 5. Understanding Comparison Operators

Suppose:

```python
a = 10
b = 5
```

### Equal to

```python
a == b
```

Means:

```text
Is 10 equal to 5?
```

Result:

```text
False
```

---

### Not equal to

```python
a != b
```

Means:

```text
Is 10 not equal to 5?
```

Result:

```text
True
```

---

### Greater than

```python
a > b
```

Means:

```text
Is 10 greater than 5?
```

Result:

```text
True
```

---

### Less than

```python
a < b
```

Means:

```text
Is 10 less than 5?
```

Result:

```text
False
```

---

### Greater than or equal to

```python
a >= b
```

Means:

```text
Is 10 greater than or equal to 5?
```

Result:

```text
True
```

---

### Less than or equal to

```python
a <= b
```

Means:

```text
Is 10 less than or equal to 5?
```

Result:

```text
False
```

---

# 6. `if` Statement

The `if` statement executes a block of code **only when the condition is `True`**.

## Syntax

```python
if condition:
    # statements
```

The colon `:` is compulsory.

---

## Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

### Execution

First:

```python
age >= 18
```

becomes:

```text
20 >= 18
```

Result:

```text
True
```

Therefore, Python executes:

```python
print("Eligible to vote")
```

Output:

```text
Eligible to vote
```

---

# 7. What Happens When the Condition Is False?

Consider:

```python
age = 15

if age >= 18:
    print("Eligible to vote")
```

Condition:

```text
15 >= 18
```

Result:

```text
False
```

Therefore, the statement inside the `if` block is skipped.

Output:

```text
No output
```

---

# 8. Important Rules of `if`

### Rule 1 — The condition comes after `if`

```python
if age >= 18:
```

---

### Rule 2 — Colon `:` is compulsory

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18
    print("Eligible")
```

---

### Rule 3 — The body must be indented

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18:
print("Eligible")
```

Python uses indentation to identify the block of code.

---

# 9. Understanding Indentation

Consider:

```python
age = 20

if age >= 18:
    print("Eligible")
    print("Adult")
```

Both `print()` statements belong to the `if` block because both are indented.

Execution:

```text
Condition
   ↓
True
   ↓
print("Eligible")
   ↓
print("Adult")
```

---

# 10. Multiple Statements Inside `if`

```python
marks = 80

if marks >= 40:
    print("Pass")
    print("Congratulations")
    print("You cleared the examination")
```

All three statements execute because they belong to the same indented block.

Output:

```text
Pass
Congratulations
You cleared the examination
```

---

# 11. `if-else` Statement

Sometimes we need to execute one block when the condition is `True` and another block when the condition is `False`.

For this, we use `if-else`.

## Syntax

```python
if condition:
    # statements when condition is True
else:
    # statements when condition is False
```

---

## Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

Condition:

```text
16 >= 18
```

Result:

```text
False
```

Therefore, the `else` block executes.

Output:

```text
Not eligible to vote
```

---

# 12. Execution Flow of `if-else`

```text
             Condition
                 |
          ┌──────┴──────┐
          |             |
        True          False
          |             |
      if block       else block
          |             |
          └──────┬──────┘
                 |
              Continue
```

Only **one** of the two blocks executes.

---

# 13. Important Rule of `if-else`

For an `if-else` statement:

```text
Condition = True
       ↓
if block executes
       ↓
else block is skipped
```

or:

```text
Condition = False
       ↓
if block is skipped
       ↓
else block executes
```

Both blocks do not execute.

---

# 14. `if-elif-else`

Sometimes there are more than two possibilities.

For example:

```text
90+  → Grade A
75+  → Grade B
50+  → Grade C
Below 50 → Fail
```

For this situation, we use:

```text
if
elif
else
```

## Syntax

```python
if condition1:
    # statements
elif condition2:
    # statements
elif condition3:
    # statements
else:
    # statements
```

---

# 15. Example of `if-elif-else`

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Execution:

```text
marks = 82
```

First condition:

```text
82 >= 90
```

Result:

```text
False
```

Next condition:

```text
82 >= 75
```

Result:

```text
True
```

Therefore:

```text
Grade B
```

is printed.

Python does not check the remaining `elif` conditions after finding the first `True` condition.

---

# 16. Important Rule of `if-elif-else`

Python checks conditions from **top to bottom**.

```text
if
 ↓
elif
 ↓
elif
 ↓
else
```

As soon as Python finds a `True` condition:

```text
Execute that block
        ↓
Skip remaining conditions
        ↓
Continue after the conditional statement
```

---

# 17. Example to Understand the Order

Consider:

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Grade A")
```

Output:

```text
Pass
```

Why?

Because Python checks:

```text
95 >= 50
```

which is already `True`.

Therefore, it executes the first block and does not reach:

```python
elif marks >= 90:
```

### Correct ordering

More specific conditions should generally come before broader conditions.

```python
if marks >= 90:
    print("Grade A")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

# 18. Nested `if`

An `if` statement inside another `if` statement is called a **nested `if`**.

## Syntax

```python
if condition1:
    if condition2:
        # statements
```

---

## Example

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```

Execution:

```text
age >= 18
     ↓
   True
     ↓
has_id
     ↓
   True
     ↓
Entry allowed
```

---

# 19. Why Use Nested `if`?

Nested conditions are useful when the second condition should only be checked after the first condition is satisfied.

Example:

```text
First check:
Is the user an adult?

        ↓ Yes

Second check:
Does the user have valid ID?

        ↓ Yes

Allow entry
```

---

# 20. Multiple Conditions

Sometimes a decision depends on more than one condition.

Python provides logical operators for this:

```text
and
or
not
```

---

# 21. `and` Operator

`and` returns `True` only when **both conditions are True**.

Example:

```python
age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

Conditions:

```text
age >= 18 → True
has_id    → True
```

Therefore:

```text
True and True → True
```

Output:

```text
Entry allowed
```

---

# 22. `and` Truth Table

| Condition 1 | Condition 2 | Result |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Easy Rule

```text
and → Everything must be True
```

---

# 23. `or` Operator

`or` returns `True` when **at least one condition is True**.

Example:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

First condition:

```text
day == "Saturday"
```

is:

```text
True
```

Therefore:

```text
True or anything → True
```

Output:

```text
Weekend
```

---

# 24. `or` Truth Table

| Condition 1 | Condition 2 | Result |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Easy Rule

```text
or → At least one must be True
```

---

# 25. `not` Operator

`not` reverses a Boolean value.

```text
not True  → False
not False → True
```

Example:

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

Since:

```text
is_raining = False
```

then:

```text
not False = True
```

Output:

```text
Go outside
```

---

# 26. Logical Operators Summary

| Operator | Meaning |
|---|---|
| `and` | All conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the Boolean result |

---

# 27. Combining Comparison and Logical Operators

We can combine comparison operators with logical operators.

Example:

```python
age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible")
```

Two conditions exist:

```text
age >= 18
salary >= 30000
```

Both are `True`.

Therefore:

```text
True and True
```

Result:

```text
True
```

Output:

```text
Eligible
```

---

# 28. Complex Conditions

Python allows multiple conditions in one statement.

```python
age = 25
salary = 50000
experience = 2

if age >= 18 and salary >= 30000 and experience >= 1:
    print("Eligible")
```

All three conditions must be `True` because `and` is used.

---

# 29. Using Parentheses in Conditions

Parentheses can make complex conditions easier to understand.

```python
age = 20
has_id = True
is_member = False

if age >= 18 and (has_id or is_member):
    print("Allowed")
```

The parentheses make it clear that:

```text
has_id OR is_member
```

is evaluated as one logical group.

---

# 30. Truthy and Falsy Values

Python conditions do not always have to contain an explicit comparison.

Some values are automatically treated as `True` or `False`.

Examples of commonly falsy values:

```python
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are considered truthy.

---

# 31. Example of Truthy Value

```python
name = "Daya"

if name:
    print("Name exists")
```

A non-empty string is truthy.

Therefore:

```text
Name exists
```

is printed.

---

# 32. Example of Falsy Value

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

An empty string is falsy.

Output:

```text
Name is empty
```

---

# 33. `=` vs `==`

This is one of the most important mistakes for beginners.

## `=`

Assignment operator.

```python
age = 20
```

Means:

```text
Store 20 in age
```

---

## `==`

Comparison operator.

```python
age == 20
```

Means:

```text
Is age equal to 20?
```

Example:

```python
age = 20

if age == 20:
    print("Age is 20")
```

Output:

```text
Age is 20
```

---

# 34. Conditional Expression

Python also provides a short form of `if-else`.

## Normal Form

```python
age = 20

if age >= 18:
    result = "Adult"
else:
    result = "Minor"
```

---

## Conditional Expression

The same logic can be written as:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)
```

Output:

```text
Adult
```

### General Syntax

```python
value_if_true if condition else value_if_false
```

This is useful for simple conditions.

---

# 35. Conditional Statement Execution Model

Consider:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

print("Program continues")
```

Execution:

```text
Start
  ↓
age = 20
  ↓
Check age >= 18
  ↓
True
  ↓
Print "Adult"
  ↓
Skip else
  ↓
Print "Program continues"
  ↓
End
```

---

# 36. Multiple `if` vs `if-elif`

These two are different.

### Multiple `if`

```python
marks = 95

if marks >= 50:
    print("Pass")

if marks >= 90:
    print("Grade A")
```

Both conditions are checked independently.

Output:

```text
Pass
Grade A
```

---

### `if-elif`

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Grade A")
```

Only the first `True` block executes.

Output:

```text
Pass
```

---

# 37. Important Difference

### Multiple `if`

```text
Check condition 1
       ↓
Check condition 2
       ↓
Check condition 3
       ↓
...
```

Every `if` is independent.

### `if-elif-else`

```text
Check condition 1
       ↓
   True? ── Yes → Execute → Skip remaining
       |
      No
       ↓
Check condition 2
       ↓
   True? ── Yes → Execute → Skip remaining
       |
      No
       ↓
      ...
       ↓
     else
```

---

# 38. Real-World Example — Login

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
```

The program checks two conditions:

```text
username is correct
AND
password is correct
```

Both must be true.

---

# 39. Real-World Example — ATM

```python
balance = 5000
withdraw = 2000

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")
```

Condition:

```text
withdraw <= balance
```

If true, withdrawal happens.

Otherwise, the transaction is rejected.

---

# 40. Real-World Example — Temperature

```python
temperature = 35

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Normal")
else:
    print("Cold")
```

Output:

```text
Hot
```

Python checks from top to bottom.

---

# 41. Real-World Example — Positive, Negative or Zero

```python
num = -10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

Output:

```text
Negative
```

---

# 42. Real-World Example — Even or Odd

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

The `%` operator gives the remainder.

For:

```text
10 % 2
```

the result is:

```text
0
```

Therefore the number is even.

---

# 43. Common Mistakes

## Mistake 1 — Forgetting `:`

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 2 — Incorrect indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Mistake 3 — Using `=` instead of `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

## Mistake 4 — Using Python Boolean values like Java

Incorrect:

```python
if value == true:
```

Correct:

```python
if value == True:
```

However, when possible, prefer:

```python
if value:
```

---

# 44. Python vs Java — Conditional Statements

The fundamental logic is similar in Python and Java, but the syntax is different.

## `if`

### Python

```python
if age >= 18:
    print("Adult")
```

### Java

```java
if (age >= 18) {
    System.out.println("Adult");
}
```

---

# 45. `if-else`

### Python

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Java

```java
if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}
```

---

# 46. `elif` vs `else if`

Python uses:

```python
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

Java uses:

```java
if (marks >= 90) {
    System.out.println("A");
} else if (marks >= 75) {
    System.out.println("B");
} else {
    System.out.println("C");
}
```

The major difference is:

```text
Python → elif
Java   → else if
```

---

# 47. Logical Operators — Python vs Java

| Purpose | Python | Java |
|---|---|---|
| AND | `and` | `&&` |
| OR | `or` | `||` |
| NOT | `not` | `!` |

Example:

### Python

```python
if age >= 18 and has_id:
    print("Allowed")
```

### Java

```java
if (age >= 18 && hasId) {
    System.out.println("Allowed");
}
```

---

# 48. Block Structure — Python vs Java

Python uses indentation:

```python
if age >= 18:
    print("Adult")
    print("Eligible")
```

Java uses curly braces:

```java
if (age >= 18) {
    System.out.println("Adult");
    System.out.println("Eligible");
}
```

### Key Difference

```text
Python → indentation defines the block

Java → { } defines the block
```

---

# 49. Boolean Values — Python vs Java

Python:

```python
True
False
```

Java:

```java
true
false
```

Notice the capitalization difference.

---

# 50. Complete Conditional Flow

A typical decision-making structure can be represented as:

```text
                Start
                  |
                  ↓
            Evaluate condition
                  |
          ┌───────┴───────┐
          |               |
        True            False
          |               |
          ↓               ↓
      Execute          Check next
      if block          condition
                          |
                    ┌─────┴─────┐
                    |           |
                  True        False
                    |           |
                    ↓           ↓
                 Execute      else
                  block       block
                    |           |
                    └─────┬─────┘
                          |
                          ↓
                       Continue
```

---

# 51. Important Rules — Final Revision

## `if`

```python
if condition:
    # block
```

Remember:

```text
1. Condition must be written after if.
2. Colon : is compulsory.
3. Body must be indented.
4. Block executes only when condition is True.
```

---

## `if-else`

```python
if condition:
    # True block
else:
    # False block
```

Remember:

```text
1. Exactly one block executes.
2. else does not have a condition.
3. Colon is required after both if and else.
```

---

## `if-elif-else`

```python
if condition1:
    # block
elif condition2:
    # block
else:
    # block
```

Remember:

```text
1. Conditions are checked from top to bottom.
2. First True condition wins.
3. Remaining conditions are skipped.
4. else executes only when all conditions are False.
5. Multiple elif blocks are allowed.
```

---

## Logical Operators

```text
and → All conditions must be True
or  → At least one condition must be True
not → Reverses the result
```

---

# 52. Quick Revision

```text
                 CONDITIONAL STATEMENTS
                         |
          ┌──────────────┼──────────────┐
          |              |              |
         if           if-else       if-elif-else
          |              |              |
       One choice     Two choices    Multiple choices
                         |
                    Nested if
                         |
                 Condition inside
                 another condition
```

### Operators

```text
Comparison:
==  !=  >  <  >=  <=

Logical:
and  or  not
```

### Python Syntax

```python
if condition:
    statement
```

```python
if condition:
    statement
else:

    statement
```

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

---

# 53. Final Mental Model

When you see a conditional statement, think:

```text
1. What decision do I need to make?
              ↓
2. What condition represents that decision?
              ↓
3. Does it have one possibility or multiple?
              ↓
4. Choose:
      if
      if-else
      if-elif-else
              ↓
5. Do I need multiple conditions?
              ↓
6. Use:
      and
      or
      not
              ↓
7. Make sure indentation is correct.
```

The core idea is:

> **A conditional statement evaluates a condition and decides which block of code should execute based on whether that condition is `True` or `False`.**