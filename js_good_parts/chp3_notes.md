## Objects

#### Javascript Types
* numbers
* strings
* booleans (*true* and *false*)
* null
* undefined

Numbers, string, and booleans are object-like in that they have methods, but they are *immutable*. Objects in JavaScript are mutable keyed collections. In JavaScript, arrays are objects, functions are objects, regular expression are objects, and, of course, objects are objects.

#### Objects
An object is a container of properties, where a property has a name and a value. A property name can be any string, including the empty string. A property value can be any JavaScript value except for *undefined*.

Objects in JavaScript are class-free. There is no constraint on the names of the new properties or on the values of properties. Objects are useful for collecting and organizing data. Objects can contain other objects, so they can easily represent tree or graph structures.

#### Object Literals
An object literal is a pair of curly braces surronding zero or more name/value pairs. An object literal can appear anywhere an expression can appear:
```javascript
var empty_object = {}

var stooge = {
    "first-name": "Jerome",
    "last-name": "Howard"
};
```

A property's name can be any string, including the empty string. The quotes around a property's name in an object literal are optional if the name would be a legal JavaScript name and not a reserved word. So quotes are required around "first-name", but are optional around first_name. Commas are used to separate the pairs.

#### Retrieval
Values can be retrieved from an object by wrapping a string expression in a [ ] suffix. If the string expression is a constant, and if it is a legal JavaScript name and not a reserved word, then the . notation can be used instead. The . notation is preferred because it is more compact and it reads better:
```javascript
stooge["first-name"]    // "Joe"
flight.departure.IATA   // "SYD"
```
Attempt to retrieve values from *undefined* will throw a *TypeError* exception. This can be guared against with the && operator:
```javascript
flight.equipment                            // undefined
flight.equipment.model                      // throw "TypeError"
flight.equipment && flight.equipment.model  // undefined
```

#### Reference
Objects are passed around by reference. They are never copied:
```javascript
var x = stooge;
x.nickname = 'Curly';
var nick = stooge.nickname;
    // nick is 'Curly' because x and stooge
    // are references to the same object
var a = {}, b = {}, c = {};
    // a, b, and c each refer to a
    // different empty object
a = b = c = {};
    // a, b, and c all refer to
    // the same empty object
```

#### Enumeration
The *for in* statement can loop over all of the property names in an object. The enumeration will include all of the properties -- including functions and prototype properties that you might not be interested in -- so it is neccesary to filter ou the values you don't want. The most common filters are the *hasOwnProperty* method and using *typeof* to exclude functions.

There is no guarentee on the order of the names, so be prepared for the names to appear in any order. If you want to assure that the properties appear in a particular order, it is best to avoid the *for in* statement entirely and instead make an array consisting of the names of the properties in the correct order.
```javascript
var i;
var properties = [
    'first-name',
    'middle-name',
    'last-name',
    'profession'
];
for (i = 0; i < properties.length; i += 1) {
    document.writeln(properties[i] + ': ' +
            another_stooge[properties[i]]);
}
```

#### Delete
The *delete* operator can be used to remove a property from an object. It will remove a property from the object is has one. It will not touch any of the objects in the protype linkage. Removing a property from an object may allow a property from the protoype linkage to shine through:
```javascript
another_stooge.nickname     // 'Moe'

// Remove nickname from another_stooge, revealing
// the nickname of the prototype.
delete another_stooge.nickname;
another_stookge.nickname    // 'Curly'
```

#### Global Abatement
JavaScript makes it easy to define global variables that can hold all of the assets of your application. Unfortunately, global variables weaken the resilency of programs and should be avoided.

One way to minimize the use of global variables is to create a single global variable for your application:
```javascript
var MYAPP = {}
```
That variable then becomes the container for your application:
```javascript
MYAPP.stooge = {
         "first-name": "Joe",
         "last-name": "Howard"
};

MYAPP.flight = {
    airline: "Oceanic",
    number: 815,
    departure: {
        IATA: "SYD",
        time: "2004-09-22 14:55",
        city: "Sydney"
       },
       arrival: {
        IATA: "LAX",
        time: "2004-09-23 10:42",
        city: "Los Angeles"
       }
};
```
By reducing your global footprint to a single name, you significantly reduce the chance of bad interactions with other applications, widgets, or libraries. Your pro- gram also becomes easier to read because it is obvious that MYAPP.stooge refers to a top-level structure. In the next chapter, we will see ways to use closure for informa- tion hiding, which is another effective global abatement technique.
