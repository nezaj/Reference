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

### List Comprehensions
List comprehensions provide a concise way to create lists. A list comprehension consists of brackets contianing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list result from evaluating the expression in the context of the for and if clauses which follow it. Here is a list comprehension to flatten an array:
```
>>> arr = [range(1, 2), range(3, 5), range(10, 12)]
>>> arr
[[1], [3, 4], [10, 11]]
>>> [num for elem in arr for num in elem]
[1, 3, 4, 10, 11]
```
Rhis is equivalent to:
```
>>> flatten = []
>>> for elem in arr:
...     for num in elem:
...         flatten.append(num)
...
>>> flatten
[1, 3, 4, 10, 11]
```

### Nested List Comprehensions
The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension. Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
The following list comprehension will transpose rows and columns:
```
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
Remember, the nested listcomp is evaluated in the context of the for that follows it. Thus this is equivalent to the following:
```
>>> transposed = []
>>> for i in range(4):
...     transpose.append([row[i] for row in matrix])
...
>>> transposed
```
Which is also equivalent to the following:
```
>>> transposed = []
>>> for i in range(4):
...     new_row = []
...     for row in matrix:
...         new_row.append(row[i])
...     transposed.append(new_row)
...
>>> tranposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
List comprehensions are nice :)

### The del statement
The way to remove an item from a list fiven its index of its value: the **del** statement. This is different from pop which returns a value. The **del** statement can also be used to remove slices from a list or clear the entire list (similar to assigning an empty slice to the slice). For example
```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5] >>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5] >>> del a[:]
>>> a
[]
```
del can also be used to delete entire variables:
```
>>> del a
```

### Dictionaries
Dic comprehensions can be used to create dictionaries from aribitrary key and value expressions:
```
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
```
>>> dict(sape=4139, guideo=4127, jack=4098)
... {'sape': 4139, 'jack': 4098, 'guido': 4127}
```

### Enumerate
```
When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
>>> for i, v in enumerate([’tic’, ’tac’, ’toe’]):
...     print i, v
...
0 tic
1 tac
2 toe
```

### Zip
To loop over to or more sequences at the same time, the entries can be paired with the **zip()** function
```
>>> questions = [’name’, ’quest’, ’favorite color’]
>>> answers = [’lancelot’, ’the holy grail’, ’blue’]
>>> for q, a in zip(questions, answers):
... print ’What is your {0}? It is {1}.’.format(q, a) ...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

### iteritems
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.
```
>>> alpha_nums = {'a': 1, 'b': 2, 'c': 3}
>>> for k, v in alpha_nums.iteritems():
...     print k, v
...
a 1
c 3
b 2
```

### Boolean operators *and* and *or* are **short-circuit** operators
Their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. It is possible to assign the result of a comparison or other Boolean expression to a variable. For example:
```
>>> string1, string2, string3 = '', 'Trondeim', 'Hammer Dance'
>>> non_null = string1, or tring2, or string3
>>> non_null
'Trondheim'
```

Note that in Python, unlike C, assignment cannot occur inside expressions.

### Comparing Sequences and Other Types
Sequence objects may be compared to other objects with the same type. The comparison uses **lexicographical** ordering.

### The Module Search Path
When a modules named *spam* is imported, the interperter first searches for a built-in module with that name. If not found, it then search for a file named spam.py in a list of directories given by the variable *sys.path* which is initialized from these locations:
* the directory containing the input script (or the current directory).
* **PYHTHONPATH** (a list of directory names, with the same syntax ash the shell varialbe **PATH**).
* the installation-dependent default.

After initialization, Python programs can modify *sys.path.* The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules from the standard library. This is an error unless the replacement was intended. Be aware.

### sys.path.append()
Use sys.path.append('directory') to add an additional search path for PYTHONPATH this is especially useful if you intend to import modules from a different directory. For example, suppose you want to import a module from the parent directory of the current file. You can do it like this:
```
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import module_name_in_parent_dir
```

### Packages
Packages are a way of structuring Python's module namespace by using "dotted modules name." For example, the module name *A.B* designates a submodule named B in a package named A.

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory. The **\_\_init.py\_\_** files are required to make Python treat the directories as containing packages. The **\_\_init\_\_.py** can be just be an empty file, but it can also execute initialization code for the package.

When using *from package import item* the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The *import* statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an **ImportError** exception is raised.

The **\_\_all\_\_** variable can be used to define which submodules are imported when using *from package import **, if it is not defined than only the names defined in the package's **\_\_init\_\_.py** will be loaded

### Intra-package References
Submodules often need to refer to each other. When packages are structured into subpackages you can use absolute import to refer to submodules of sibilings packages. For example, if the modules *sound.filters.vocoder* needs to use the *echo* module in the *sound.effects* package, it can use *from sound.effects import echo*

Note: Explicit and implicit relative imports are base on the name of the current module. Since the name of main module is always **\_\_modules\_\_**, modules intended for use as the main module of a Python application should always use absolute imports.
