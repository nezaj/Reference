## Grammar

#### Comments
The /* */ form of block comments came from a language called PL/I. PL/I chose those strange pairs as the symbols for comments because they were unlikely to occur in that language’s programs, except perhaps in string literals. In JavaScript, those pairs can also occur in regular expression literals, so block comments are not safe for commenting out blocks of code. For example:
```javascript
/*
    var rm_a = /a*/.match(s);
*/
```
causes a syntax error. So, it is recommended that /* */ comments be avoided and //
comments be used instead. In this book, // will be used exclusively.

#### Numbers
Javascript has a single number type. Internally, it is represented as 64-bit floating point, the same as Java's double. There is no seperate integer type, so 1 and 1.0 are the same value.

#### Strings
A string literal canb e wrapped in single quotes or double quotes. It can contain zero or more chracters. The \ (backslash) is the escape character. Javascript was built at a time when Unicode was a 16-bit character set, so all chracters in Javascript are 16 bits wide.

Javascript does not have a character type. To represent a character, make a string with just one chracter in it.

THe escape sequences allow for inserting chracters into strings that are not nromally permitted, such as backslahses, quotes, and control characters. the \u convention allows for specifying chracter code points numerically.
```javascript
"A" === "\u0041"
```

Strings are immutable. Once it is made, a string can never be changed. But you can make a new string by concatening other strings together with the + operator.
```javascript
'c' + 'a' + 't' === 'cat'
```

#### Falsy Values
* false
* null
* undefined
* The emtpy string ``
* THe number 0
* THe number NaN

All other values are truthy, including trude, the string 'false', and all objects.

#### Disruptive Statements
The *return* statement causes the early return from a function. It can also specify the value to be returned. If a return expression is not specified, then the return value will be undefined.

The *break* statement causes the exit from a loop statement or a switch statement. It can optionally have a label that will cause an exit from the labeled statement.



