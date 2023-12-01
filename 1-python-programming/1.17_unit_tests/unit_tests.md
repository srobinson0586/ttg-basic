# Python Unit Tests

[Back to README](README.md)

"Unit testing is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation."    
        - _A Gentle introduction to Unit Testing in Python_, 2022

Use unit testing to programmatically examine small segments of code for bugs and errors. 

## The `unittest.testcase` class

This is the engine which allows this programmatic problem checking.

For our case, we will define a class Rectangle as follows:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height
```

If we wanted to perform a unittest on rectangle area, we would implement the following:

```py
class TestGetAreaRectangle(unittest.TestCase):
    def runTest(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
```

_Focus on the implementation of `self.assertEqual`_

This is a perfect explanation of the unittest case. This given example will **assert** if the given value, 6, in the parameters is equal to the instantiated rectangle's area.

In this case, the outcome is true, and the outcome will look something like this:
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

[More reading on UnitTesting](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)

## Customized Unit Testing

As a developer, you are free to design your own unit testing for your software. You can make test scripts which compare output, custom exception handlers, and/or use improved open source testing suites that you can find. 

As long as you understand how your code is being tested, and can communicate that clearly to others, you can use whichever methodology you see fit.

[More resources on testing your code](https://realpython.com/python-testing/)

## Resources
- [Machine Learning Mastery | Python Unit Testing](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)
- [RealPython | Testing](https://realpython.com/python-testing/)

## Sources
- [Python Docs | `unittest`](https://docs.python.org/3/library/unittest.html)

[Back to README](README.md)