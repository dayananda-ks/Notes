# Python — Functions

A function is one of the most important concepts in programming.

A function allows us to write a block of code once and **reuse it whenever required**.

---


# 1. What is a Function?

A function is an **independent block of code that performs a specific action based on the input provided to it**.

A function can be executed only when it is **called**.

For example:

```python
def greet():
    print("Hello Daya")
```

The above code only **defines** the function.

It does not execute the `print()` statement yet.

To execute the function:

```python
greet()
```

Output:

```text
Hello Daya
```

---

# 2. Why Do We Need Functions?

Suppose we need to check whether a number is even or odd multiple times.

Without a function:

```python
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


num = 25

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

The same logic has to be written repeatedly.

With a function:

```python
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

Now we can reuse the same logic:

```python
even_odd(10)
even_odd(25)
even_odd(100)
```

The main advantage is:

```text
Write once
    ↓
Call whenever required
    ↓
Reuse the logic
```

---

# 3. Basic Function Syntax

## Function Definition

```python
def function_name(parameters):
    # body of the function
    # logic
    return
```

## Function Call

```python
variable_name = function_name(arguments)
```

However, the assignment to a variable is required **only when the function returns a value**.

For a function that only prints:

```python
function_name(arguments)
```

is enough.

---

# 4. Parts of a Function

Consider:

```python
def add(a, b):
    result = a + b
    return result
```

There are several parts:

```text
def
 ↓
Function name
 ↓
Parameters
 ↓
Function body
 ↓
return
```

More clearly:

```python
def add(a, b):
    result = a + b
    return result
```

| Part | Meaning |
|---|---|
| `def` | Keyword used to define a function |
| `add` | Function name |
| `a, b` | Parameters |
| `:` | Starts the function block |
| `result = a + b` | Function logic |
| `return result` | Sends the result back |

---

# 5. `def` Keyword

Python uses the `def` keyword to define a function.

Example:

```python
def greet():
    print("Hello")
```

Here:

```text
def
```

tells Python:

> I am defining a function.

---

# 6. Function Name

The function name identifies the function.

Example:

```python
def calculate_sum():
    print("Calculating")
```

Here:

```text
calculate_sum
```

is the function name.

A good function name should describe what the function does.

Examples:

```python
calculate_sum()
check_even()
find_maximum()
calculate_average()
print_details()
```

---

# 7. Function Body

The statements written inside the function are called the **function body**.

Example:

```python
def greet():
    print("Hello")
    print("Welcome")
```

The function body is:

```python
print("Hello")
print("Welcome")
```

Both statements belong to the function because they are indented.

---

# 8. Function Scope

The block of code belonging to a function is called the **scope/body of the function**.

Example:

```python
def greet():
    print("Hello")
    print("Welcome")

print("Outside function")
```

The statements:

```python
print("Hello")
print("Welcome")
```

are inside the function.

The statement:

```python
print("Outside function")
```

is outside the function.

---

# 9. Function Call

Defining a function does not execute it.

Example:

```python
def greet():
    print("Hello")
```

At this point:

```text
Function created
       ↓
Function not executed
```

To execute it:

```python
greet()
```

Now:

```text
Function called
       ↓
Function body executes
       ↓
Hello
```

---

# 10. Function Definition vs Function Call

This difference is very important.

### Function Definition

```python
def greet():
    print("Hello")
```

Meaning:

> Create/define a function named `greet`.

### Function Call

```python
greet()
```

Meaning:

> Execute the `greet` function.

---

# 11. Execution Flow of a Function

Consider:

```python
def greet():
    print("Hello")

print("Start")

greet()

print("End")
```

Execution:

```text
Start
  ↓
greet() is called
  ↓
Enter greet()
  ↓
print("Hello")
  ↓
Function finishes
  ↓
Return to the function call
  ↓
print("End")
```

Output:

```text
Start
Hello
End
```

---

# 12. Parameters

Parameters are the **input variables required by a function to perform its action**.

Example:

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name
```

is a parameter.

The function needs a name to perform its operation.

---

# 13. Arguments

Arguments are the **actual values passed as input to a function when the function is called**.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Daya")
```

Here:

```text
name
```

is the parameter.

```text
"Daya"
```

is the argument.

---

# 14. Parameter vs Argument

Consider:

```python
def add(a, b):
    return a + b

add(10, 20)
```

Here:

```text
a, b
```

are parameters.

```text
10, 20
```

are arguments.

### Simple Difference

```text
Parameter
    ↓
Variable defined in function definition

Argument
    ↓
Actual value passed during function call
```

---

# 15. Relationship Between Parameters and Arguments

Consider:

```python
def add(a, b):
    return a + b

add(10, 20)
```

Python maps the values:

```text
a ← 10
b ← 20
```

Therefore:

```python
a + b
```

becomes:

```python
10 + 20
```

Result:

```text
30
```

---

# 16. Order of Parameters and Arguments

The order of arguments normally corresponds to the order of parameters.

Example:

```python
def student(name, age):
    print(name)
    print(age)

student("Daya", 21)
```

Mapping:

```text
name ← "Daya"
age  ← 21
```

Output:

```text
Daya
21
```

If the values are passed in the wrong order:

```python
student(21, "Daya")
```

Python will still pass them positionally:

```text
name ← 21
age  ← "Daya"
```

The function may then produce incorrect results for the intended meaning.

---

# 17. Function Without Parameters

A function does not always require input.

Example:

```python
def greet():
    print("Hello Daya")
```

Call:

```python
greet()
```

Output:

```text
Hello Daya
```

Here:

```text
Parameters = 0
Arguments  = 0
```

---

# 18. Function With One Parameter

```python
def square(num):
    print(num * num)
```

Call:

```python
square(5)
```

Mapping:

```text
num ← 5
```

Calculation:

```text
5 × 5 = 25
```

Output:

```text
25
```

---

# 19. Function With Multiple Parameters

```python
def add(a, b):
    print(a + b)
```

Call:

```python
add(10, 20)
```

Mapping:

```text
a ← 10
b ← 20
```

Output:

```text
30
```

---

# 20. `return` Statement

`return` is a Python keyword used inside a function.

It mainly helps us:

1. Return a value from the called function to the function call.
2. Transfer the execution flow back to the point where the function was called.
3. Reuse the returned output in another part of the program.

---

# 21. Simple `return` Example

```python
def add(a, b):
    return a + b
```

Call:

```python
result = add(10, 20)
```

Execution:

```text
add(10, 20)
      ↓
a = 10
b = 20
      ↓
a + b
      ↓
10 + 20
      ↓
30
      ↓
return 30
      ↓
result = 30
```

Therefore:

```python
print(result)
```

Output:

```text
30
```

---

# 22. Why Do We Need `return`?

Suppose:

```python
def add(a, b):
    print(a + b)
```

Calling:

```python
result = add(10, 20)
```

prints:

```text
30
```

But `result` does not contain `30`.

The function only printed the value.

---

With `return`:

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Now:

```text
result = 30
```

The returned value can be reused.

---

# 23. `print()` vs `return`

This is one of the most important concepts.

## `print()`

Displays a value on the screen.

```python
def add(a, b):
    print(a + b)
```

The function displays the result.

---

## `return`

Sends a value back to the caller.

```python
def add(a, b):
    return a + b
```

The caller can store and reuse the result.

Example:

```python
result = add(10, 20)

double = result * 2

print(double)
```

Output:

```text
60
```

---

# 24. `return` Takes Back Execution Flow

Consider:

```python
def test():
    print("Inside function")
    return 10

print("Before call")

result = test()

print("After call")
```

Execution:

```text
Before call
     ↓
test() called
     ↓
Inside function
     ↓
return 10
     ↓
Execution returns to:
result = test()
     ↓
result becomes 10
     ↓
After call
```

Output:

```text
Before call
Inside function
After call
```

---

# 25. `return` Ends Function Execution

Once Python executes a `return`, the function immediately ends.

Example:

```python
def test():
    print("Statement 1")
    return 10
    print("Statement 2")
```

Call:

```python
test()
```

Output:

```text
Statement 1
```

`Statement 2` does not execute because:

```python
return 10
```

already ended the function.

---

# 26. Returning Multiple Values

Python allows a function to return multiple values.

Example:

```python
def calculate(a, b):
    return a + b, a - b
```

Call:

```python
sum_value, difference = calculate(10, 5)
```

The function returns:

```text
15, 5
```

Therefore:

```text
sum_value  = 15
difference  = 5
```

---

# 27. Returning Different Data Types

A function can return different types of values.

### Integer

```python
def get_number():
    return 10
```

### String

```python
def get_name():
    return "Daya"
```

### List

```python
def get_numbers():
    return [10, 20, 30]
```

### Boolean

```python
def is_even():
    return True
```

---

# 28. Function With Input and Return Value

This is a very common function pattern.

```python
def square(num):
    return num * num
```

Call:

```python
result = square(5)
```

Execution:

```text
num = 5
   ↓
5 * 5
   ↓
25
   ↓
return 25
   ↓
result = 25
```

---

# 29. Even or Odd

One of the simplest function problems is checking whether a number is even or odd.

Before writing the function, understand the operators involved.

---

# 30. Division Operator `/`

The `/` operator performs normal division.

Example:

```python
10 / 2
```

Result:

```text
5.0
```

Even though the mathematical result is `5`, Python returns a floating-point value.

Another example:

```python
5 / 2
```

Result:

```text
2.5
```

So:

```text
/ → True division
```

---

# 31. Floor Division `//`

The `//` operator performs floor division.

Example:

```python
10 // 2
```

Result:

```text
5
```

Example:

```python
5 // 2
```

Result:

```text
2
```

It removes the fractional part by taking the floor of the result.

```text
10 / 2  → 5.0
10 // 2 → 5

5 / 2   → 2.5
5 // 2  → 2
```

> Note: For negative values, `//` performs mathematical floor division, so it is not simply "truncate the decimal part."

Example:

```python
-5 // 2
```

Result:

```text
-3
```

because:

```text
floor(-2.5) = -3
```

---

# 32. Modulo Operator `%`

The `%` operator gives the **remainder** after division.

Example:

```python
10 % 2
```

Result:

```text
0
```

Example:

```python
10 % 3
```

Result:

```text
1
```

Because:

```text
10 ÷ 3
Quotient = 3
Remainder = 1
```

Therefore:

```text
10 % 3 = 1
```

---

# 33. Why `%` Is Used for Even/Odd

A number is even if it is completely divisible by `2`.

That means:

```text
remainder = 0
```

Therefore:

```python
num % 2 == 0
```

means:

> The number is divisible by 2 without any remainder.

So:

```python
if num % 2 == 0:
```

checks whether the number is even.

---

# 34. Example — Check Even or Odd Without a Function

### Problem

Write a program to check whether the given number is even or odd.

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Example Input

```text
Enter a number: 10
```

Execution:

```text
10 % 2
   ↓
0
```

Therefore:

```text
Even
```

---

# 35. Example — Check Even or Odd Using a Function

Now we can place the same logic inside a function.

```python
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

Function call:

```python
even_odd(10)
```

Output:

```text
Even
```

Another call:

```python
even_odd(25)
```

Output:

```text
Odd
```

---

# 36. Even/Odd Function With User Input

```python
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


num = int(input("Enter a number: "))

even_odd(num)
```

Execution:

```text
User enters number
       ↓
input()
       ↓
int()
       ↓
num
       ↓
even_odd(num)
       ↓
Function receives num
       ↓
num % 2
       ↓
Check remainder
       ↓
Even / Odd
```

---

# 37. Even/Odd Function With `return`

Instead of printing inside the function, we can return the result.

```python
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

Call:

```python
num = int(input("Enter a number: "))

result = even_odd(num)

print(result)
```

For input:

```text
10
```

Output:

```text
Even
```

---

# 38. Why Returning Is Better Here

Compare these two approaches.

### Approach 1 — Print inside function

```python
def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

The function directly displays the result.

---

### Approach 2 — Return result

```python
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

Now the caller decides what to do with the result.

```python
result = even_odd(10)

print(result)
```

The returned value can also be reused:

```python
result = even_odd(10)

if result == "Even":
    print("The number is divisible by 2")
```

This makes the function more reusable.

---

# 39. Function Execution Flow — Complete Example

Consider:

```python
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = 15

result = even_odd(num)

print(result)
```

Execution:

```text
Program starts
      ↓
Function definition is created
      ↓
num = 15
      ↓
even_odd(num) is called
      ↓
15 is passed to num
      ↓
15 % 2
      ↓
1
      ↓
1 == 0
      ↓
False
      ↓
else block
      ↓
return "Odd"
      ↓
result = "Odd"
      ↓
print(result)
      ↓
Odd
```

---

# 40. Function Calling Another Function

A function can call another function.

Example:

```python
def square(num):
    return num * num


def display_square(num):
    result = square(num)
    print(result)


display_square(5)
```

Execution:

```text
display_square(5)
        ↓
square(5)
        ↓
5 × 5
        ↓
25
        ↓
return 25
        ↓
display_square receives 25
        ↓
print(25)
```

Output:

```text
25
```

---

# 41. Local Variables

Variables created inside a function are generally local to that function.

Example:

```python
def test():
    num = 10
    print(num)

test()
```

Here:

```text
num
```

is created inside `test()`.

Trying to access it outside:

```python
def test():
    num = 10

test()

print(num)
```

causes an error because `num` is not defined in the outer scope.

---

# 42. Function With No `return`

A function does not always need a `return` statement.

Example:

```python
def greet():
    print("Hello")

greet()
```

This is completely valid.

If a function does not explicitly return a value, Python returns:

```python
None
```

Example:

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
Hello
None
```

---

# 43. Function Definition and Memory

When Python reads:

```python
def add(a, b):
    return a + b
```

the function is defined.

The function body does not execute immediately.

Only when we call:

```python
add(10, 20)
```

does Python execute the function body.

Mental model:

```text
Function Definition
       ↓
Function created
       ↓
Program continues
       ↓
Function Call
       ↓
Function executes
       ↓
return
       ↓
Execution continues from caller
```

---

# 44. Common Mistakes

## Mistake 1 — Defining but not calling

```python
def greet():
    print("Hello")
```

This does not print anything.

You need:

```python
greet()
```

---

## Mistake 2 — Forgetting parameters

Incorrect:

```python
def add(a, b):
    return a + b

add()
```

The function requires two arguments.

Correct:

```python
add(10, 20)
```

---

## Mistake 3 — Wrong number of arguments

```python
def add(a, b):
    return a + b

add(10)
```

The function requires:

```text
2 arguments
```

but only:

```text
1 argument
```

was provided.

---

## Mistake 4 — Confusing `print()` with `return`

```python
def add(a, b):
    print(a + b)
```

This displays the result but does not return it.

If you need to reuse the result:

```python
def add(a, b):
    return a + b
```

---

# 45. Python vs Java — Functions

In Python, functions are defined using:

```python
def
```

Example:

```python
def add(a, b):
    return a + b
```

Java uses a method inside a class.

Example:

```java
static int add(int a, int b) {
    return a + b;
}
```

---

# 46. Python vs Java — Main Differences

| Concept | Python | Java |
|---|---|---|
| Define function/method | `def` | Return type + method name |
| Type declaration | Usually not required | Required |
| Block | Indentation | `{}` |
| Return | `return` | `return` |
| Boolean AND | `and` | `&&` |
| Boolean OR | `or` | `||` |
| Boolean NOT | `not` | `!` |
| Function call | `add(10, 20)` | `add(10, 20)` |
| Parameters | `a, b` | `int a, int b` |

---

# 47. Python vs Java Example

### Python

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Java

```java
static int add(int a, int b) {
    return a + b;
}

int result = add(10, 20);

System.out.println(result);
```

The fundamental concept is the same:

```text
Input
  ↓
Function
  ↓
Processing
  ↓
Return result
```

The syntax is different.

---

# 48. Function Mental Model

The easiest way to understand a function:

```text
                Function
                   |
        ┌──────────┴──────────┐
        |                     |
      Input                 Logic
        |                     |
   Parameters             Processing
        |                     |
   Arguments                   |
        └──────────┬──────────┘
                   ↓
                Return
                   ↓
                Output
```

Example:

```python
def add(a, b):
    return a + b
```

Think:

```text
10 ──┐
     ├──→ add() ──→ 30
20 ──┘
```

---

# 49. Important Rules — Final Revision

### Function

```text
A reusable independent block of code that performs a specific task.
```

### Definition

```python
def function_name(parameters):
    # logic
```

### Call

```python
function_name(arguments)
```

### Parameter

```text
Variable that receives input inside the function definition.
```

### Argument

```text
Actual value passed during the function call.
```

### Return

```text
Sends a value from the called function back to the caller.
```

### `print()`

```text
Displays a value.
```

### `return`

```text
Returns a value and terminates the current function execution.
```

---

# 50. Quick Revision

```text
                    FUNCTION
                       |
                       ↓
                Define Function
                       |
                       ↓
                def function()
                       |
                       ↓
                 Parameters
                       |
                       ↓
                 Function Body
                       |
                       ↓
                   Function
                    Call
                       |
                       ↓
                  Arguments
                       |
                       ↓
                  Execute Logic
                       |
                       ↓
                    return
                       |
                       ↓
                 Caller receives
                    result
```

---

# 51. Core Example

```python
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

result = even_odd(num)

print(result)
```

For:

```text
Input:
10
```

Execution:

```text
10
 ↓
even_odd(10)
 ↓
10 % 2
 ↓
0
 ↓
0 == 0
 ↓
True
 ↓
return "Even"
 ↓
result = "Even"
 ↓
print(result)
```

Output:

```text
Even
```

---

# 52. Final Concept

The complete idea of a function can be remembered as:

```text
             FUNCTION
                 |
          Takes Input
                 |
                 ↓
          Performs Logic
                 |
                 ↓
          Produces Result
                 |
                 ↓
             return
                 |
                 ↓
       Caller receives result
                 |
                 ↓
          Result can be reused
```

> **A function is a reusable block of code that performs a specific task. Parameters define the inputs the function expects, arguments provide the actual values, and `return` sends the result back to the caller.**