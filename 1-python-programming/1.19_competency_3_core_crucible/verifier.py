import test
import core
import os

def test_intro_funcs():
    success = True

    ### String section.

    string_section = test.TestSection("string")

    f1 = test.TestFunc(core.greet)
    f1.add(("Bob",), "Hello Bob!")
    f1.add(("",), "Hello !")
    string_section.add(f1)

    f2 = test.TestFunc(core.abba)
    f2.add(("Hi", "Bye"), "HiByeByeHi")
    f2.add(("hob", "nob"), "hobnobnobhob")
    string_section.add(f2)

    f3 = test.TestFunc(core.split_and_insert)
    f3.add(("Hi", "Bye"), "HByei")
    f3.add(("<<<>>>", "hi"), "<<<hi>>>")
    string_section.add(f3)

    f4 = test.TestFunc(core.dup_last_2)
    f4.add(("word", 4), "rdrdrdrd")
    f4.add(("mocha", 3), "hahaha")
    string_section.add(f4)

    f5 = test.TestFunc(core.short_long_short)
    f5.add(("a big string", "hi"), "hia big stringhi")
    f5.add(("hi", "a big string"), "hia big stringhi")
    string_section.add(f5)

    success = string_section.run()

    ### Integer section.

    if success:
        integer_section = test.TestSection("integer")

        f1 = test.TestFunc(core.adding)
        f1.add((3, 5), 8)
        f1.add((2, 3.5), 5.5)
        f1.add((3.2, 3.2), 12.8)
        integer_section.add(f1)

        f2 = test.TestFunc(core.abs_diff)
        f2.add((17,), 4)
        f2.add((25,), 8)
        f2.add((21,), 0)
        integer_section.add(f2)

        f3 = test.TestFunc(core.tens)
        f3.add((3, 10), True)
        f3.add((2, -10), False)
        f3.add((2.3, 7.7), True)
        integer_section.add(f3)

        f4 = test.TestFunc(core.hundreds)
        f4.add((95,), True)
        f4.add((105,), True)
        f4.add((89,), False)
        f4.add((111,), False)
        integer_section.add(f4)

        f5 = test.TestFunc(core.negatives)
        f5.add((1, -1, False), True)
        f5.add((-1, -1, False), False)
        f5.add((1, 1, False), False)
        f5.add((-1, 1, False), True)
        f5.add((1, 0, False), False)

        f5.add((1, -1, True), False)
        f5.add((-1, -1, True), True)
        f5.add((1, 1, True), False)
        f5.add((-1, 1, True), False)
        f5.add((0, -1, True), False)
        integer_section.add(f5)

        success = integer_section.run()

    ### List section.

    if success:
        list_section = test.TestSection("list")

        f1 = test.TestFunc(core.ends_are_the_same)
        f1.add(([1, 2, 3, 4, 5, 1],), True)
        f1.add(([6],), False)
        f1.add(([],), False)
        f1.add(([1, 2, 3],), False)
        list_section.add(f1)

        f2 = test.TestFunc(core.count_sixes)
        f2.add(([6, 2, 4, 6, 3, 6],), 3)
        f2.add(([6],), 1)
        f2.add(([],), 0)
        f2.add(([1, 2, 3],), 0)
        list_section.add(f2)

        f3 = test.TestFunc(core.sum_list)
        f3.add(([],), 0)
        f3.add(([6],), 6)
        f3.add(([1, 2, 3],), 6)
        f3.add(([1, -1],), 0)
        list_section.add(f3)

        f4 = test.TestFunc(core.rotate_2_spaces_left)
        f4.add(([1, 2, 3, 4, 5],), [3, 4, 5, 1, 2])
        f4.add(([6, 7],), [6, 7])
        list_section.add(f4)

        f5 = test.TestFunc(core.append_product_and_sum)
        f5.add(([1, 2, 3, 4],), [1, 2, 12, 3])
        f5.add(([6, 7, 8],), [6, 56, 62])
        list_section.add(f5)

        success = list_section.run()

    ### Boolean section.

    if success:
        bool_section = test.TestSection("boolean")

        f1 = test.TestFunc(core.count_trues)
        f1.add((True, True, True), 3)
        f1.add((False, False, False), 0)
        f1.add((False, True, False), 1)
        f1.add((False, True, True), 2)
        bool_section.add(f1)

        f2 = test.TestFunc(core.positive_product)
        f2.add((1, 0), False)
        f2.add((1, 1.0), True)
        f2.add((1, -1.0), False)
        f2.add((-1.0, -3), True)
        bool_section.add(f2)

        f3 = test.TestFunc(core.has_7_before_6)
        f3.add([1, 2, 3, 4, 5, 6, 7], False)
        f3.add([], False)
        f3.add([1, 2, 3, 4, 5, 7, 6], True)
        f3.add([7], True)
        f3.add([1, 2, 3, 4, 5, 6], False)
        bool_section.add(f3)

        f4 = test.TestFunc(core.greater_than_both)
        f4.add((1, 2, 3), False)
        f4.add((4, 3, 5), False)
        f4.add((1, 2, 0), False)
        f4.add((5, 3, 2), True)
        bool_section.add(f4)

        f5 = test.TestFunc(core.close_and_far)
        f5.add((1, 5, 2), True)    ### a close, b far
        f5.add((5, 1, 2), True)    ### a far, b close
        f5.add((3, 5, 1), False)   ### no close
        f5.add((2, 4, 3), False)   ### no far
        bool_section.add(f5)

        success = bool_section.run()

    ### Loop section.

    if success:
        loop_section = test.TestSection("loop")

        # Note: Only change the prefix!
        f1 = test.TestFunc(core.copy_xkcd_to_calvin, copy_input = True)
        f1.add(["cow", "xkcdabc", "xkcd ball", "donkey xkcd"],
            ["cow", "calvinabc", "calvin ball", "donkey xkcd"])
        f1.add([], [])
        loop_section.add(f1)

        f2 = test.TestFunc(core.even_odd_product)
        f2.add([1, 2, 3, 4, 6], 48)
        f2.add([1, 3, 5, 7], 0)
        f2.add([], 0)
        loop_section.add(f2)

        f3 = test.TestFunc(core.pop_while)
        f3.add([1, 2, 3, 4, 5, 6], 21)
        f3.add([], 0)
        f3.add([1], 1)
        loop_section.add(f3)

        success = loop_section.run()

    ### Function section.

    if success:
        function_section = test.TestSection("function")

        if "my_affirmer" not in dir(core):
            raise NameError("You still need to create the function `my_affirmer`!")

        f1 = test.TestFunc(core.my_affirmer)
        f1.add(tuple(), True)
        function_section.add(f1)

        if "my_product" not in dir(core):
            raise NameError("You still need to create the function `my_product`!")

        f2 = test.TestFunc(core.my_product)
        f2.add((3, 4), 12)
        f2.add((6, -7), -42)
        f2.add((9, 0), 0)
        function_section.add(f2)

        success = function_section.run()
    return success

#######################
### File operations ###
#######################

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
    core.initialize_file(filename, correct_contents)
    if not verify_file_contents(filename, correct_contents, 0):
        return False


    ### Testing file information.
    print("File information:")
    core.get_file_info(filename)


    ### Testing edit (capitalizing the contents).
    ### Update correct contents.
    correct_contents = correct_contents.upper()

    core.edit_existing_file(filename)
    if not verify_file_contents(filename, correct_contents, 1):
        return False


    ### Testing appending.
    correct_len = len(correct_contents)
    correct_contents += to_append
    if core.append_to_file(filename, to_append) != correct_len:
        print("Incorrect return value from append_to_file")
        return False

    if not verify_file_contents(filename, correct_contents, 2):
        return False


    ### Testing deletion.
    core.delete_file(filename)
    if os.path.exists(filename):
        print("The file still exists after you were supposed to delete it!")
        return False

    return True


#####################
### Generic logic ###
#####################

def test_multiply(a, b):
    """ Test the student's recursive multiply implementation.
    Return True for success, False otherwise. """
    rtn = True
    if core.recursive_multiplication(a, b) != a * b:
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
    if core.compare(a, b) != secret_func(a, b):
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
    if core.return_multiple_values(a, b) != (a, b):
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
    if core.parity(n) != n%2:
        print(f"parity({n}) - Wrong value")
        return False
    n = 32442
    if core.parity(n) != n%2:
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


if __name__ == "__main__":
    
    ########################
    # Test intro functions #
    ########################
    if not test_intro_funcs():
        exit()
    
    ###################################
    # Call file & generic func tester #
    ###################################

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
