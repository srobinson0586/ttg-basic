# Python Classes and Objects

In Python 3, an **object** is a fundamental concept that represents a real-world entity, concept, or thing. Objects are created from *classes*, which are templates for objects. Just about everything in Python is an object, including built-in data types like integers, strings, lists, dictionaries, and much more. You have already worked with many Python objects from the following built-in class types:

- **`int`**, **`float`**, and **`complex`**: Represent numerical values.
- **`str`**: Represent sequences of characters.
- **`list`**, **`tuple`**, and **`set`**: Represent collections of elements.
- **`dict`**: Represent key-value mappings.
- Files: Represent file objects for input/output operations.
- Functions: Represent callable objects.
- **`module`**: Represent collections of related functions, classes, and variables.
- Exceptions: Represent errors or exceptional situations.


In Python, classes play a central role in implementing object-oriented programming (OOP) concepts such as *encapsulation*, *abstraction*, *inheritance*, and *polymorphism*. If this is your first time hearing about these object-oriented programming concepts, check out [this video](https://www.youtube.com/watch?v=pTB0EiLXUC8) for a more detailed explanation.

- Classes use **encapsulation** to bundle an objects attributes and behaviors. Encapsulation can shield the complexity of an object and provide a high level of modularity and understanding of code.

- Classes use **abstraction** to simplify the details of complex objects by focusing on the essential aspects of an object and ignoring unnecessary details. Abstraction focuses on what an object is and what it can do, not so much how it exists and how its behaviors work.

- Classes can make use of [**inheritance**](#inheritance), where a child class can inherit attributes and behaviors from a parent class. Inheritance promotes code reuse for similar objects.

- Classes can make use of **polymorphism**, where different classes can be treated uniformly so long as they share a common interface.

Since Python is not the only language that supports object-oriented programming, understanding the general ideas of OOP can be helpful in development projects where other object-oriented programming languages are used.

## Classes Define Objects

In object-oriented programming, a **class** is a template or blueprint for creating objects. A class specifies the *attributes* and *methods* that each object of the class will possess. An object is a realized *instance* of a class. Many objects can be created from a single class template.

> Note: In most contexts, the terms 'object' and 'instance' refer to the same thing: a realized instance of a class. As such, you will often see them used interchangeably when searching on Google for programming documentation or help forums.

- An **attribute** is a property or characteristic of an object. In code, attributes look like variables that represent information about an object. In Python, attributes of an object can be accessed using the `.` operator.

- A **method** is a behavior of an object. In code, it is essentially a function that is specific to an object. Whereas functions are general sets of instructions that work independently, methods are specialized sets of instructions that define actions that objects can perform. In Python, object methods can be accessed using the `.` operator.

A simple example of a class could be one called `Dog` that provides a template to represent any dog. The attributes of `Dog` can include `name` and `age`, and it can have a method called `bark`. We will make this class in the subsection below to show how you can create objects and interact with them in Python.

## Declaring Classes and Creating Objects

You can create a class using the `class` keyword in Python. The standard way of creating a class is the following:

1. **Class Declaration**: To create a class, use the `class` keyword followed by the class name. The class name should follow the CamelCase naming convention (capitalize the first letter of each word). 

2. **Constructor (`__init__`)**: Inside the class, define the `__init__` method, which serves as the **constructor**. A constructor is a method that is called when an instance of a class is created. Constructors typically initialize the default values of the object.

3. **Attributes**: Declare attributes within the `__init__` method using the `self` parameter. The `self` parameter refers to the instance of the object being created. Attributes define the data associated with each object.

> Note: When creating your own classes, it is convention to use `self` as the name of the first parameter of a constructor or method any time you are attempting to access attributes or methods of the class. If you do not use `self` (or some other named reference to the instance of the class) when attempting to access a class attribute or method, Python will not know to check in the scope of the class to see if they exist. This may lead to exceptions being thrown, or access of variables that exist in different scopes outside of the class.

4. **Methods**: Define methods within the class. Methods are functions that can be called on objects of the class. They can operate on the object's attributes and perform actions.

Here's an example using the `Dog` example from above:

```python
# Class declaration and name
class Dog:
    # Constructor: takes `name` and `age` as arguments and uses them to initialize a dog's attributes
    def __init__(self, name, age):
        # Attributes
        self.name = name
        self.age = age

    # Method: creates the `bark` action that any `Dog` object can use
    def bark(self):
        print(f"{self.name} barks!")
```

We can now create instances using the `Dog` class and interact with them by doing the following:

```python
# Create an object from the `Dog` class
my_dog = Dog("Buddy", 3)

# Access the `age` attribute of `my_dog`
print(f"My dog is {my_dog.age} years old")

# Invoking the `bark` method for `my_dog`
my_dog.bark()

# Creating another `Dog` object
your_dog = Dog("Spot", 5)

# Invoking the `bark` method for `your_dog`
your_dog.bark()
```

```
My dog is 3 years old
Buddy barks!
Spot barks!
```

### Leveraging Constructors for Default Values

We use constructors to declare and initialize attributes when an instance of a class is created. Since a constructor is ultimately just a function that belongs to a class, we can use concepts from [1.15_functions](../1.15_functions/functions.md) to craft constructors with features that make it easier to create new objects. For example, we can make use of *keyword* and *default* arguments to initialize default values for attributes, even if an argument was not explicitly passed to the constructor.

```python
class Person:
    # `age` is a default argument; if no value is passed for `age`, then it is set to 30 by default for the object being created
    def __init__(self, name, age=30):
        self.name = name
        self.age = age

# Creating objects using the class constructor
person1 = Person(name="Alice", age=25)
person2 = Person(name="Bob")  # Age will default to 30 for `person2`

# Accessing object attributes
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

```
```
Alice is 25 years old.
Bob is 30 years old.
```

### Getter and Setter Methods

In Python, you are able to directly access an object's attributes using the `.` operator (like in the above example with `my_dog.age`). This makes it very easy to retrieve or update an attribute, but it is not always best practice. Depending on the situation (or programming language used), it might be better to create **getter** and **setter** methods.

Getters and setters are object methods that are often created to interface with its attributes. They are useful since they:

- Abstract the object's implementation details from the outside world.
- Allow for a way to validate and control the data being set or retrieved from an object's attributes.
- Allow for modification of data without affecting the external interface of the class.
- Can include additional logic or behavior when setting a value, such as triggering certain actions, updating related attributes, or logging changes.

The example below shows getter and setter methods being implemented for the `Dog` class and how they are invoked:

```Python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} barks!")

    # Getters that simply return object attributes
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # Setters that provide some input validation before modifying object attributes
    def set_name(self, name):
        if name and type(name) == str:  # check if `name` argument is a string before assignment
            self.name = name

    def set_age(self, age):  
        if age > -1:        # check that `age` is non-negative before assignment
            self.age = age



# Creating an instance of `Dog`
my_dog = Dog("Buddy", 3)

# Checking the attributes of `my_dog`
print(f"{my_dog.get_name()} is {my_dog.get_age()} years old")

# Attempting to set `age` to something impossible
my_dog.setAge(-10000)

# Checking the attributes of `my_dog` again (`age` should not have been set to negative value)
print(f"{my_dog.get_name()} is {my_dog.get_age()} years old")

# Setting age to something valid and checking attributes again
my_dog.set_age(4)
print(f"{my_dog.get_name()} is {my_dog.get_age()} years old")
print(f"Happy birthday {my_dog.get_name()}!")
my_dog.bark()
```
```
Buddy is 3 years old
Buddy is 3 years old
Buddy is 4 years old
Happy birthday Buddy!
Buddy barks!
```

> Note: The convention shown above for implementing getter and setter methods is a generalized convention that you are likely to see used in other object-oriented languages. There is a more "Pythonic" way to implement getter and setter methods using `@property` tags. This is covered in [1.39_property_tags](../1.39_property_tags).

### Inheritance

Python supports class inheritance such that one class can inherit the attributes and methods of another class. This can be useful for code reuse and building hierarchies of related classes. A child or subclass can inherit properties from their parent or superclass, promoting code reuse.

To have a subclass inherit attributes and methods from another class, it should be declared like `class Child(Parent):`, where `Parent` is the class to inherit from. Below is an example:

```python
# Parent/Superclass
class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


# Child/Subclass (Inheriting from the Parent/Superclass `Person`)
class Developer(Person):
    pass    # We put `pass` since we are not adding more attributes or methods to the child class


# Creating an instance of the child class (child uses parent's constructor with argument "Bob")
i_am = Developer("Bob")

# Using the child class to invoke an inherited method
i_am.greet()
```
```
Hello, I am Bob
```

The above example is simple, but we would likely not create an entirely new child class just to have it copy the parent's characteristics exactly. In addition to what it inherits, we can extend the functionality of a child class by giving it new attributes and methods. If we need to overwrite an inherited method (by creating a method with the same name) in the child class, we can still make use of the parent's methods through the `super()` function, which is used to access attributes and methods of the parent class.

```python
# Parent/Superclass
class Person():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


# Child/Subclass (Inheriting from the Parent/Superclass `Person`)
class Developer(Person):

    # Declaring `__init__` in this class's scope overwrites the constructor inherited from the parent
    def __init__(self, name, job, location):
        super().__init__(name)          # Using the parent's constructor through `super`

        self.job = job              # New attribute not inherited from the parent
        self.location = location    # New attribute not inherited from the parent

    # Declaring `greet` in this class's scope overwrites the `greet` method inherited from the parent
    def greet(self):
        super().greet()             # Using the parent's `greet`
        print(f"I am a {self.job} at {self.location}!")   # Adding more to the output of `greet`


# Creating an instance of the child class (the parent constructor is used, so `i_am.name` == "Bob")
person1 = Developer("Bob", "Developer", "A big company")

# Using the child class to invoke an inherited method
person1.greet()
print()

# Compare to the `greet` method of the parent
person2 = Person("Alice, Eater of Mountains and Drinker of Seas")
person2.greet()
```
```
Hello, I am Bob
I am a Developer at A big company!

Hello, I am Alice, Eater of Mountains and Drinker of Seas
```

### Dunder Methods
We briefly introduced you to *dunder methods* in [1.02_basic_syntax](../1.02_basic_syntax), but here is a quick review.

In Python, dunder (short for "double underscore") methods, also known as magic methods or special methods, are methods that have a specific meaning and behavior when defined within a class. These methods are identified by their double underscore prefix and suffix, such as `__init__`, `__str__`, `__add__`, etc. Dunder methods allow you to customize the behavior of your objects and classes, enabling you to define how they interact with built-in functions and operators.

Here are just a few of the dunder methods that you can implement for classes that you make:

- `__init__(self, ...)`: The constructor method is called when an object of the class is created. It initializes the object's attributes.

- `__str__(self)`: This method returns a human-readable string representation of the object. It's called by the built-in `str()` function and the `print()` function.

- `__len__(self)`: This method returns the length of the object. It's called by the built-in `len()` function.

- `__sub__(self, other)`: Similarly, this method allows objects to define their behavior when using the `-` operator for subtraction.

- `__eq__(self, other)`: This method defines the behavior of the `==` operator for object equality.

- `__lt__(self, other)`: This method defines the behavior of the `<` operator for object comparison.

A much more complete list of all the dunder methods you can implement can be found at this [mathspp.com blog on dunder methods](https://mathspp.com/blog/pydonts/dunder-methods).

* * *

The following code creates the template for `Snack` objects:
```python
class Snack:
    def __init__(self, name, price, calories):
        self.name = name        # Name of the snack (string)
        self.price = price      # Price of the snack (float)
        self.calories = calories  # Calories in the snack (int)
```

If we try to execute the following code:

```python
# Creating instances of Snack
snack1 = Snack("Chips", 1.99, 200)
snack2 = Snack("Soda", 1.00, 150)

# Print some information about our snacks
print(snack1)
print(snack2)

# Calculate and print the price of our snacks
total_price = snack1 + snack2
print(f"The price of our snacks is ${total_price}.")
```

we end up with some output that is probably not what we would want to see before getting a TypeError because Python does not know how to perform addition on `Snack` objects.

```
<__main__.Snack object at 0x7f959a2dd300>
<__main__.Snack object at 0x7f959a2dd4e0>
Traceback (most recent call last):
  File "1.21_classes_and_objects/test.py", line 14, in <module>
    total_price = snack1 + snack2
TypeError: unsupported operand type(s) for +: 'Snack' and 'Snack'
```

We can clean up the output of these objects by creating the appropriate dunder methods in the `Snack` class. To make a `Snack` object look tidy when it is called as an argument for `print`, we need to create the `__str__`  method. To avoid getting a TypeError when performing addition, we need to create the `__add__` method and specify addition using the `price` attribute of the object. We create these methods for `Snack` below:

```python
class Snack:
    def __init__(self, name, price, calories):
        self.name = name        # Name of the snack (string)
        self.price = price      # Price of the snack (float)
        self.calories = calories  # Calories in the snack (int)

    def __str__(self):
        # Print snack attributes - show price to two degrees of floating point precision using :.2f
        return f"{self.name} - Price: ${self.price:.2f}, Calories: {self.calories}"

    def __add__(self, other):
        return self.price + other.price
```

Now if we create some `Snack` instances and try to do the same actions as before, we end up with cleanly formatted output and no errors:

```python
# Creating instances of Snack
snack1 = Snack("Chips", 1.99, 200)
snack2 = Snack("Soda", 1.00, 150)

# Print some information about our snacks
print(snack1)
print(snack2)

# Calculate and print the price of our snacks
total_price = snack1 + snack2
print(f"The price of our snacks is ${total_price}.")
```
```
Potato Chips - Price: $2.99, Calories: 150
Soda - Price: $1.00, Calories: 150
The price of our snacks is $3.99.
```

> Note: In the above example, Python knew how to do addition with our `Snack` object because we defined the addition operation for `Snack` in its `__add__` method. If we wanted to do subtraction or checks on equality, we would also need to define the `__sub__`, `__eq__`, `__lt__`, and `__gt__` methods. The functionality of your classes with built-in functions only goes as far as the dunder methods you define.

## Summary

Objects are essential because they promote code organization, reusability, extensibility, and maintainability, making it easier to develop software that models and solves real-world problems effectively. They allow developers to think in terms of entities, interactions, and relationships, leading to more intuitive and structured code. The principles of object-oriented programming extend beyond the scope of Python, but a solid understanding of objects in Python can very effectively translate over to other languages.

Similar to algorithms, object-oriented programming is not something that you can gain an intuitive understanding of in a day. Typically, a college or university will dedicate a quarter or a semester to the practice and comprehension of OOP principles. Understanding of classes, objects, and object-oriented programming as a whole comes with repeated practice. Extra resources are linked below.

## Resources

- [Classes - PyDocs](https://docs.python.org/3/tutorial/classes.html)
- [Python Classes - W3Schools](https://www.w3schools.com/python/python_classes.asp)
- [Object Oriented Programming in 7 Minutes | Mosh](https://www.youtube.com/watch?v=pTB0EiLXUC8)
- [Object Oriented Programming with Python - Full Course for Beginners - FreeCodeCamp.org](https://www.youtube.com/watch?v=Ej_02ICOIgs)
- [Dunder Methods | Pydon't](https://mathspp.com/blog/pydonts/dunder-methods)


[Back to README](README.md)