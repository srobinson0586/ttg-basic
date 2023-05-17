import test as test
import intro as intro

print("Welcome to the 1.3.1 verifier!\n")
success = True

### String section.

string_section = test.TestSection("string")

f1 = test.TestFunc(intro.greet)
f1.add(("Bob",), "Hello Bob!")
f1.add(("",), "Hello !")
string_section.add(f1)

f2 = test.TestFunc(intro.abba)
f2.add(("Hi", "Bye"), "HiByeByeHi")
f2.add(("hob", "nob"), "hobnobnobhob")
string_section.add(f2)

f3 = test.TestFunc(intro.split_and_insert)
f3.add(("Hi", "Bye"), "HByei")
f3.add(("<<<>>>", "hi"), "<<<hi>>>")
string_section.add(f3)

f4 = test.TestFunc(intro.dup_last_2)
f4.add(("word", 4), "rdrdrdrd")
f4.add(("mocha", 3), "hahaha")
string_section.add(f4)

f5 = test.TestFunc(intro.short_long_short)
f5.add(("a big string", "hi"), "hia big stringhi")
f5.add(("hi", "a big string"), "hia big stringhi")
string_section.add(f5)

success = string_section.run()

### Integer section.

if success:
    integer_section = test.TestSection("integer")

    f1 = test.TestFunc(intro.adding)
    f1.add((3, 5), 8)
    f1.add((2, 3.5), 5.5)
    f1.add((3.2, 3.2), 12.8)
    integer_section.add(f1)

    f2 = test.TestFunc(intro.abs_diff)
    f2.add((17,), 4)
    f2.add((25,), 8)
    f2.add((21,), 0)
    integer_section.add(f2)

    f3 = test.TestFunc(intro.tens)
    f3.add((3, 10), True)
    f3.add((2, -10), False)
    f3.add((2.3, 7.7), True)
    integer_section.add(f3)

    f4 = test.TestFunc(intro.hundreds)
    f4.add((95,), True)
    f4.add((105,), True)
    f4.add((89,), False)
    f4.add((111,), False)
    integer_section.add(f4)

    f5 = test.TestFunc(intro.negatives)
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

    f1 = test.TestFunc(intro.ends_are_the_same)
    f1.add(([1, 2, 3, 4, 5, 1],), True)
    f1.add(([6],), False)
    f1.add(([],), False)
    f1.add(([1, 2, 3],), False)
    list_section.add(f1)

    f2 = test.TestFunc(intro.count_sixes)
    f2.add(([6, 2, 4, 6, 3, 6],), 3)
    f2.add(([6],), 1)
    f2.add(([],), 0)
    f2.add(([1, 2, 3],), 0)
    list_section.add(f2)

    f3 = test.TestFunc(intro.sum_list)
    f3.add(([],), 0)
    f3.add(([6],), 6)
    f3.add(([1, 2, 3],), 6)
    f3.add(([1, -1],), 0)
    list_section.add(f3)

    f4 = test.TestFunc(intro.rotate_2_spaces_left)
    f4.add(([1, 2, 3, 4, 5],), [3, 4, 5, 1, 2])
    f4.add(([6, 7],), [6, 7])
    list_section.add(f4)

    f5 = test.TestFunc(intro.append_product_and_sum)
    f5.add(([1, 2, 3, 4],), [1, 2, 12, 3])
    f5.add(([6, 7, 8],), [6, 56, 62])
    list_section.add(f5)

    success = list_section.run()

### Boolean section.

if success:
    bool_section = test.TestSection("boolean")

    f1 = test.TestFunc(intro.count_trues)
    f1.add((True, True, True), 3)
    f1.add((False, False, False), 0)
    f1.add((False, True, False), 1)
    f1.add((False, True, True), 2)
    bool_section.add(f1)

    f2 = test.TestFunc(intro.positive_product)
    f2.add((1, 0), False)
    f2.add((1, 1.0), True)
    f2.add((1, -1.0), False)
    f2.add((-1.0, -3), True)
    bool_section.add(f2)

    f3 = test.TestFunc(intro.has_7_before_6)
    f3.add([1, 2, 3, 4, 5, 6, 7], False)
    f3.add([], False)
    f3.add([1, 2, 3, 4, 5, 7, 6], True)
    f3.add([7], True)
    f3.add([1, 2, 3, 4, 5, 6], False)

    f4 = test.TestFunc(intro.greater_than_both)
    f4.add((1, 2, 3), False)
    f4.add((4, 3, 5), False)
    f4.add((1, 2, 0), False)
    f4.add((5, 3, 2), True)

    f5 = test.TestFunc(intro.close_and_far)
    f5.add((1, 5, 2), True)    ### a close, b far
    f5.add((5, 1, 2), True)    ### a far, b close
    f5.add((3, 5, 1), False)   ### no close
    f5.add((2, 4, 3), False)   ### no far
    bool_section.add(f3)

    success = bool_section.run()

### Loop section.

if success:
    loop_section = test.TestSection("loop")

    # Note: Only change the prefix!
    f1 = test.TestFunc(intro.copy_xkcd_to_calvin, copy_input = True)
    f1.add(["cow", "xkcdabc", "xkcd ball", "donkey xkcd"],
           ["cow", "calvinabc", "calvin ball", "donkey xkcd"])
    f1.add([], [])
    loop_section.add(f1)

    f2 = test.TestFunc(intro.even_odd_product)
    f2.add([1, 2, 3, 4, 6], 48)
    f2.add([1, 3, 5, 7], 0)
    f2.add([], 0)
    loop_section.add(f2)

    f3 = test.TestFunc(intro.pop_while)
    f3.add([1, 2, 3, 4, 5, 6], 21)
    f3.add([], 0)
    f3.add([1], 1)
    loop_section.add(f3)

    success = loop_section.run()

### Function section.

if success:
    function_section = test.TestSection("function")

    if "my_affirmer" not in dir(intro):
        raise NameError("You still need to create the function `my_affirmer`!")

    f1 = test.TestFunc(intro.my_affirmer)
    f1.add(tuple(), True)
    function_section.add(f1)

    if "my_product" not in dir(intro):
        raise NameError("You still need to create the function `my_product`!")

    f2 = test.TestFunc(intro.my_product)
    f2.add((3, 4), 12)
    f2.add((6, -7), -42)
    f2.add((9, 0), 0)
    function_section.add(f2)

    success = function_section.run()

### Congratulate them if they're done.
if success:
    print("Congratulations! You've completed 1.3.1!")
