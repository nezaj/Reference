# Python Doc Notes

### Python scripts can be made directly executable
To do this add this line to the top of your script
```
#! /usr/bin/env python
```
Now give the script an execution mode using chmod
```
chmod u+x myscript.py
```

### Interactive Startup File
By setting an enviornment variable named PYTHONSTARTUP to the name of the file containing startup-commands, you can have standard commands executed every time the interperter is started. This is similar to the .profile feature of the Unix Shells. If you want a file to use this start-commands as well use the following pattern
```
import os
filename = os.enviorn.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    execfile(filename)
```

### Python supports complex numbers
Complex numbers are written with a suffix of j or J. Complex nubmers with a nonzero real componenet are written as (real +imagj) or can be created with te complex(real, imag) function
```
>>> 1j * 1j
(-1+0j)
>>>1j + complex(0,1)
(-1+0j)
>>> 3+1j*3
(3+3j)
```

### _ Variable in Interactive Mode
In python the last printed expression is assigned to the variable _. THis means that when you are using Python as a desk calculator, it is somewhat easier to conitnue calculations, for example
```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
round(_, 2)
113.06
```

### Slice operations create a shallow copy
```
>>> a = ['spam', "egg's", 100, 1234]
<<< a[:]
['spam', 'eggs', 100, 1234]
```

### Python support multiple assignment
Right-hand expressions ar evaluated first before assignment. Evaluation is done from left to right
```
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> a, b = b, a
>>> a
2
>>> b
1
```

### Trailing comma avoids newline after output
```
>>> a = 0
>>> while a < 10:
...     print a,
...     a += 1
0 1 2 3 4 5 6 7 8 9
```

### Functions and Variable Scope
The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

### Default argument values
Default values for a paramter is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls
```
def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print (f3)
```
This will print
```
[1]
[1, 2]
[1, 2, 3]
```

If you do not want the default to be shared between subsequent calls, you can write the function like this instead
```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

### Lambda Expressions
Small anonymous functions can be created with the lambda keyword. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. THey are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope
```
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument
```
>>> pairs = [(1, ’one’), (2, ’two’), (3, ’three’), (4, ’four’)]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, ’four’), (1, ’one’), (3, ’three’), (2, ’two’)]
```

### Style Guide
* Use 4-space indentation, no tabs
* Wrap lines so they don't exceed 79 characters
* Use blank lines to separate functions and classes,
  and larger blocks of code inside functions
* When possible, put comments on a line of their own
* Use docstrings
* Use spaces around operators and after commas, but not directly inside
  bracket constructs: a = f(1, 2), b = g(3, 4)
* Names your classes and functions consistently;
  **CamelCase** for classes
  **snake_case** for functions and methods
* Always use self as the name for first method argument
* Use plain ASCII when working in international enviornments

### Functional Programming Tools
There are three built-in functions that are very useful when used with lists: **filter()**, **map()**, and **reduce()**

*filter(function, sequence)* returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a **list**
```
>>> is_even = lambda x: x % 2 == 0
>>> filter(is_even, range(2, 10))
[2, 4, 6, 8]
```

*map(function, sequence)* calls function(item) for each of the sequence's items and returns a list of the return values. For example, to compute some cubes:
```
>>> cube = lambda x: x*x*x
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

More than one sequence may be passed to map; the function then must have as many arguments as there are sequences and is called with the corresponding item from each sequence (or None if some sequence is shorter thana nother). For example:
```
>>> seq = range(8)
>>> add = lambda x, y: x + y
>>> map(add, seq, seq)
[0, 2, 4, 5, 6, 10, 14]
```

*reduce(function, sequence)* returns a single value constructed by calling the binary function *function* on the first two items of the sequence, then on the result of the next item, and so on. For example to compute the sum of the numbers 1 through 10:
```
>>> reduce(add, range(1, 11))
55
```

If there's only one item in the sequence, its value is returned; if the sequence is empty, an exception is raised. A third argument can be passed to indiciate the startign value. In this case the starting value is returned for the empty sequence and the function is first applied to the starting value and first sequence item.
```
>>> reduce(add, range(1, 11), 10)
65
```
