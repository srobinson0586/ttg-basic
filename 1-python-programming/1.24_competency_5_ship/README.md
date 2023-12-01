# Python Competency 5 - Ship

[Back to OVERVIEW](../README.md)

Code: [`ship.py`](./ship.py)

## Objectives

In this competency, you will apply the knowledge you learned from previous competencies and recent modules. After completing this competency, you should be comfortable with:

- [Classes and Objects](../1.21_classes_and_objects/README.md)

## Implementation of `Ship` and `Fleet`

In the [`ship.py`](./ship.py) file, there are two partially filled-in classes, `Ship` and `Fleet`. Your task is to complete the TODOs for each class.

The `Ship` class is a template for representing US Navy ships. Each instance of `Ship` has access to  dictionaries which detail the limits of the ship's engine speed, how quick it can turn, how much mass it has, and how it is affected by drag. These dictionaries should be used for implementing the setter and getter methods of ship. There are docstrings in each of the methods that you are required to implement which provide more detail on what is required.

The `Fleet` class is a template to represent a fleet of ships. An instance of `Fleet` serves as an interface to manage multiple ships.

As you read and complete the TODOs, refer back to the section on [Classes and Objects](../1.21_classes_and_objects/classes_and_objects.md) to understand how the attributes and methods of a class work. The [`ship.py`](./ship.py) file has a `main()` function that you can freely overwrite if you want to create your own tests to check your implementation as you work.

## Assignment
- [ ] Implement functionality for both `Ship` and `Fleet` as described above in [`ship.py`](./ship.py)
- [ ] Test your code by running `pytest` in the working directory. If all test cases pass, you have completed this competency.

[Back to OVERVIEW](../README.md)