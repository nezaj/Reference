## Chapter 4: Functions

#### Function Literal
Function objects are created with function literals:
```javascript
// Create a variable called add and store a function
     // in it that adds two numbers.
var add = function (a, b) { return a + b;
};
```
A function literal has four parts. The first part is the reserved word function.
The optional second part is the function’s name. The function can use its name to call itself recursively. The name can also be used by debuggers and development tools to identify the function. If a function is not given a name, as shown in the previous example, it is said to be anonymous.

The third part is the set of parameters of the function, wrapped in parentheses. Within the parentheses is a set of zero or more parameter names, separated by com- mas. These names will be defined as variables in the function. Unlike ordinary variables, instead of being initialized to undefined, they will be initialized to the arguments supplied when the function is invoked.

The fourth part is a set of statements wrapped in curly braces. These statements are the body of the function. They are executed when the function is invoked.

A function literal can appear anywhere that an expression can appear. Functions can be defined inside of other functions. An inner function of course has access to its parameters and variables. An inner function also enjoys access to the parameters and variables of the functions it is nested within. The function object created by a function literal contains a link to that outer context. This is called *closure*. This is the source of enormous expressive power.


#### Invocation
There are four patterns of invocation in JavaScript: the method invocation pattern, the function invocation pattern, the constructor invocation pattern, and the apply invocation pattern. The patterns differ in how the bonus parameter **this** is initialized.

The invocation operator is a pair of parenthesis that follow any expression that produces a function value. The parenthesis can contain zero or more expressions, separated by commas. Each expression produces one argument value. Each of the argument values will be assigned to the function's parameter names. There is no runtime error when the number of arguments and the number of parameters do not match. If there are too many argument values, the extra values will be ignored. If there are two few argument values, the *undefined* value will be substituted for the missing values. There is no type checking on the argument values: any type of value can be passed to any parameter.

##### Method Invocation Pattern
When a function is stored as a property of an object, we call it a *method*. When a method is invoked, **this** is bound to that object. If an invocation expression contains a refinement (usually a . or a [*subscript*] expression), it is invoked as a method.
```javascript
// Create myObject. It has a value and an increment
// method. The increment method takes an optional
// parameter. If the argument is not a number, then 1
// is used as the default.

var myObject = {
    value: 0,
    increment: function (inc) {
        this.value += typeof inc === 'number' ? inc : 1;
    }
};

myObject.increment();
document.writeln(myObject.value);   // 1

myObject.increment(2);
document.writeln(myObject.value);   // 3
```
A method can use **this** to access the object so that it can retrieve values from the object or modify the object. The binding of **this** to the object happens at invocation time. This very late binding makes functions that use this highly re-usable. Methods that get their object context from **this** are called *public methods*

##### Function Invocation Pattern
When a function is not a property of an object, then it is invoked as a function.
```javascript
var sum = add(3, 4)     // sum is 7
```
When a function is invoked with this pattern, it is bound to the global object. This is problematic an inner function can't be used as a helper for the outer function because the inner function's this is bound to a different object. However, using the "that" trick there is a simple workaround.
```javascript
myObject.double = function() {
    var that = this;        // this is bound to myObject

    var helper = function() {
        that.value *= 2;    // Still bound to myObject
    }

    helper();               // Invoked helper as a function
};

myObject.double(); // Invoke double as a method
document.writeln(myObject.value);   // 6
```

##### Constructors
Functions that are intended to be used with the new prefix are called *constructors*. By convention, they are kept in variables with a capitalized name. If a constructor function is called without the new prefix very strange behavior may occur at run-time without any warning. As a result is extremely important to follow the convention.

##### Constructor Invocation Pattern
This pattern has one define functions one an object's prototype and then instantiate and invoke the functions method style. This is not recommended.

##### Apply Invocation Pattern
Because JavaScript is a functional object-oriented language, functions can have methods. The **apply** method accepts a value to bind to **this** and an array of parameters for the function. It can be useful when invoking a function to bind **this** to object that does not have that function defined. For example
```javascript
var Quo = function (status) {
    this.status = status;
}

Quo.prototype.get_status = function() {
    return this.status
};

var statusObject = {
    status: "A-OK"
};

var status = Quo.get_status.apply(statusObject); // status is "A-OK'
```
#### Return
A function always returns a value. If a **return** value is not specified, then **undefined** is returned. If the function was invoked with the **new** prefix and the return value is not an object, then **this** (the new object) is returned instead.

#### Augmenting Types
JavaScript allows the basic types of the language to be *augmented*. This means you can make new methods available for objects, functions, arrays, string, numbers, regexs, and booleans. You can simplify defining new methods on a function with the following snippet
```javascript
Function.prototype.method = function(name, func) {
    this.prototype[name] = func;
    return this;
}
```
Now we can use our method function to more easily define new methods for our basic types. For example, JavaScript does not have an integer type and the built-in method
to extract the integer value is ugly. We can define our own integer method using method above.
```javascript
Number.method('integer', function() {
    return Math[this < 0 ? 'ceiling' : 'floor'](this);
});

document.writeln((-10 / 3).integer());  // -3
```
JavaScript also lacks a method to remove trailing spaces from the end of the string. Let's make our own trim method
```javascript
String.method('trim', function() {
    return this.replace(/^\s+|\s+$g, '');
});
```
By augmenting the basic types, we can make JavaScript much more expressive. Methods defined on the prototype are immediately available to all instances, even if they were created before the new method was defined.

You should be careful when mixing libraries and augmenting basic types. Because the prototypes of basic types are public, you may have naming conflicts. A defensive technique for this is to use *hasOwnProperty* to check if the method has not already been defined.
```javascript
Function.prototype.method = function(name, func) {
    if (!this.prototype[name]) {
        this.prototype[name] = func;
    }
    return this;
}
```

#### Recursion
JavaScript currently doesn't support **tail call optimization**, as a result, it may exhaust the stack if there are too many recursive calls.

#### Scope
JavaScript has function scope. So variables defined anywhere inside a function are not visible outside of the function definition.

#### Closure
Good news is that inner functions get access to the parameters and variables of the functions they are defined within (except for *this* and *arguments*). This is a very good thing.

Earlier we made a myObject function with an increment method. Suppose we wanted to make myObject's value variable private. We can do it like so
```javascript
var myObject = function() {
    value = 0;

    return {
        increment: function(inc) {
            value += typeof inc === 'number' ? inc : 1;
        },
        getValue: function() {
            return value;
        }
    };
}();
```
Note we are not assigning a function to myObject. We are assigning the result of invoking that function (see the () on the last line). The function returns an object containing two methods that can access the value variable. However, the value variable can not be accessed or manipulated directly

In an earlier example Quo was defined using a constructor to produce an object with a status property and a get_status method. But that doesn't seem necessary, what's the point of making a get_status method if the status property is directly accessible. It would make more sense if the status variable were private. Instead of using a constructor, lets use a function to achieve the desired behavior.
```javascript
var quo = function(status) {
    return {
        get_status: function() {
            return status;
        }
    };
};

var myQuo = quo("amazed");
document.writeln(myQuo.get_status());
```
Now status is private and can no longer be altered.

It's important to understand that the inner function has access to the actual variables of the outer functions and not copies. Consider the following problem
```javascript
// BAD EXAMPLE

// Make a function that assigns event handler functions to an array of nodes the wrong way.
// When you click on a node, an alert box is supposed to display the ordinal of the node.
// But it always displays the number of nodes instead

var add_the_handlers = function(nodes) {
    var i;
    for (i = 0; i < nodes.length; i++) {
        nodes[i].onclick = function(e) {
            alert(i);
        };
    }
};

// END BAD EXAMPLE
```
The function was intended to give each handler a unique number (i). It fails because the handler functions are bound to the variable i, not the value of the variable i at the time the function was made:
```javascript
// BETTER EXAMPLE

// Make a function that assigns event handler functions to an array of nodes
// the right way.
// WHen you click on a node, an alert box will display the ordinal of the node.

var add_the_handlers = function(nodes) {
    var i;
    for (i = 0; i < nodes.length; i++) {
        nodes[i].onclick = function(i) {
            return function(e) {
                alert(e);
            };
        }(i);
    }
};
