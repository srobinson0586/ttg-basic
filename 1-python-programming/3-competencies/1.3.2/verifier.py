import os

import intermediate as student

def verify_file_contents(filename, correct_contents, iteration):
    """ Verify that the file contents match what we expect.
    Return True if they do, False otherwise. """
    rtn = True
    if not os.path.exists(filename):
        print("File '{}' doesn't even exist!".format(filename))
        rtn = False

    else:
        with open(filename, "r") as f:
            contents = f.read()

        if contents != correct_contents:
            print("Incorrect file contents! (iteration {})".format(iteration))
            print("We wanted '{}', but found '{}'".format(correct_contents,
                                                          contents))
            rtn = False

    return rtn

def test_file_ops():
    """ Test the student's file operation implementations.
    Return True if all tests pass, False otherwise. """
    print("<<< Testing file operations >>>")

    filename = "test.txt"
    correct_contents = "Hooyah Navy"
    to_append = " BEAT ARMY\n"

    ### Testing initialize_file().
    student.initialize_file(filename, correct_contents)
    if not verify_file_contents(filename, correct_contents, 0):
        return False


    ### Testing file information.
    print("File information:")
    student.get_file_info(filename)


    ### Testing edit (capitalizing the contents).
    ### Update correct contents.
    correct_contents = correct_contents.upper()

    student.edit_existing_file(filename)
    if not verify_file_contents(filename, correct_contents, 1):
        return False


    ### Testing appending.
    correct_len = len(correct_contents)
    correct_contents += to_append
    if student.append_to_file(filename, to_append) != correct_len:
        print("Incorrect return value from append_to_file")
        return False

    if not verify_file_contents(filename, correct_contents, 2):
        return False


    ### Testing deletion.
    student.delete_file(filename)
    if os.path.exists(filename):
        print("The file still exists after you were supposed to delete it!")
        return False

    return True

def test_multiply(a, b):
    """ Test the student's recursive multiply implementation.
    Return True for success, False otherwise. """
    rtn = True
    if student.recursive_multiplication(a, b) != a * b:
        print(f"recursive_multiplication({a}, {b}) - Wrong value")
        rtn = False
    return rtn

### No docs! Very secret!
def secret_func(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def test_compare(a, b):
    """ Test the student's compare implementation.
    Return True for success, False otherwise. """
    rtn = True
    if student.compare(a, b) != secret_func(a, b):
        print("compare(a, b) - Wrong value")
        rtn = False
    return rtn


def test_generic_functions():
    """ Test the student's generic function implementations.
    Return True if all tests pass, False otherwise. """
    print("<<< Testing generic functions >>>")

    ### Testing multiple return values.
    a = 42
    b = 314
    if student.return_multiple_values(a, b) != (a, b):
        print(f"return_multiple_values({a}, {b}) - Wrong return value")
        return False

    ### Testing recursive multiplication.
    if not test_multiply(a, b):
        return False
    a *= -1
    if not test_multiply(a, b):
        return False
    b *= -1
    if not test_multiply(a, b):
        return False

    ### Testing parity.
    n = 32443
    if student.parity(n) != n%2:
        print(f"parity({n}) - Wrong value")
        return False
    n = 32442
    if student.parity(n) != n%2:
        print(f"parity({n}) - Wrong value")
        return False

    ### Testing comparison.
    a = 1
    b = 5
    if not test_compare(a, b):
        return False
    a = 5
    if not test_compare(a, b):
        return False
    a = 6
    if not test_compare(a, b):
        return False

    return True


def main():
    """ Test all functions in intermediate.py. """
    ### Test file operations.
    if test_file_ops():
        print("<<< Automatic file tests passed! >>>\n")
    else:
        print("\n" + "#" * 40)
        print("At least one automatic file test failed")
        print("#" * 40 + "\n")

    ### Test generic functions.
    if test_generic_functions():
        print("<<< Automatic generic tests passed! >>>\n")
    else:
        print("\n" + "#" * 40)
        print("At least one automatic generic test failed")
        print("#" * 40 + "\n")

    ### Run exception handling function.
    print("<<< Running your exception-handling function (no auto checks) >>>")
    student.exception_handling()


if __name__ == "__main__":
    main()
