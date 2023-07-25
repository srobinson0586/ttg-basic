
# Challenge 1.1: Setup Global Variable
def setup_increment_counter():
    '''
    Create a global integer variable named `counter` and set its initial value to 0
    This variable will be used in increment_counter()
    '''
    global counter
    counter = 0

# Challenge 1.2: Function with Global Variable
def increment_counter():
    '''
    This function increments the value of `counter` by 1 each time it is called. Return the current value of `counter` after incrementing it.
    '''
    global counter
    counter += 1
    return counter

# Challenge 2: Function with Default Argument
def greet_person(name, greeting="Hello"):
    '''
    This function takes two arguments:
        - `name` (a string)
        - `greeting` (a string with a default value "Hello")
    Return the greeting message along with the name separated only by a space. If the greeting argument is not provided, it should use the default value "Hello"
    Example: 
        greet_person('TRAINO') --> "Hello TRAINO"
    '''
    return f"{greeting} {name}"

# Challenge 3: Recursive Function
def calculate_factorial(n):
    '''
    Takes a non-negative integer `n` as an argument and returns the factorial of `n`
    Use the recursive approach to solve this problem.
    Example:
        calculate_factorial(5)  # Output should be 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
    '''
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Challenge 4: Function with Variable-Length Arguments
def sum_numbers(*args):
    '''
    Takes any number of integer arguments and returns their sum. 
    Example 1:
        sum_numbers(1, 2, 3)       # Output should be 6
    Example 2:
        sum_numbers(10, 20, 30, 40)  # Output should be 100
    '''
    return sum(args)
