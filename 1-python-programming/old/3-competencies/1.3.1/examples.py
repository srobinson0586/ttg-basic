###################################################
#   AN EXPLANATION OF BASIC TYPES AND FUNCTIONS   #
#  Use this section as REFERENCE as you practice! #
###################################################

def basic_types():
    ''' Integers! '''
    print(2 + 3)  # 2+3 = 5
    print(2 - 3)  # 2-3 = -1
    print(2 * 3)  # 2*3 = 6
    print(14 / 7)  # 14 divided by 7 = 2
    print(13 // 7)  # 13 divided by 7 = 1 (// does integer division)
    print(13 / 7)  # 13 divided by 7 = 1.857 ...  (/ does a float division)
    print(13 % 7)  # 13 modulus 7 = 6. This is the remainder!
    print(101 % 2)  # simple way to determine even or odd.  If remainder is 0:even, else:odd.
    print(2 ** 3)  # 2 to the power of 3 = 8 (2*2*2)

    a = 1  # a is an int, with the value of 1
    print(type(a))  # prints <type 'int'>
    print(a)  # 1
    a + 1
    print(a)  # 1, notice we did not update the value of a
    a = a + 1
    print(a)  # 2, this time we did
    a += 1
    print(a)  # 3, this is another way of doing the same thing

    ''' Strings! '''
    b = "Hello, World!"  # b is a string, with the value of "Hello, World!"
    print(type(b))  # prints <type 'str'>
    print(b)  # prints "Hello, World!"
    print(len(b))  # prints the length of string b -> 13
    print(b * 3)  # multiplying a string, causes it to repeat -> "Hello, World!Hello, World!Hello, World!"
    print("Oh... " + b)  # adding strings together concatonates -> "Oh... Hello, World!"

    ''' Lists are what they sound like, a list of values '''
    c = [1, "two", "three", 4]  # c is a list with 4 values of different types
    print(type(c))  # prints <type 'list'>
    print(len(c))  # print length of c -> "4"
    print(c[0])  # value at offset 0 (first item in the list) -> 1
    print(c[3])  # value at offset 3 (fourth item in the list) -> 4
    print(c[-1])  # last value of the list -> 4
    print(c[-2])  # 2nd to last value of thelist -> "three"
    print(c[0:2])  # print values from offset 0 to 2, NOT INCLUDING offset 2 -> [1,"two"]
    print(c[1:])  # print values from offset 1, through the end -> ["two","three",4]
    c[2] = 3
    print(c)  # [1,"two",3,4], you have changed the value of c[2]

    ''' Strings are "sort of" like a list of characters, you can operate on them similarly '''
    d = "I LOVE PYTHON!"
    print(d[0:5])  # prints -> "I LOV"
    print(d[5:])  # prints -> "E PYTHON!"
    print(d[-1])  # prints -> "!".  -2, -3, -4, etc... iterate backwards!

    return


def boolean_examples():
    ''' Booleans! True or False? '''
    a = True
    b = False
    if a:  # a == True...
        print(a)  # so this will run!
    if b:  # b == False
        print(b)  # so this will NOT run!
    if a == b:  # equality operator (==) returns "True" or "False"
        print(a, b)  # a does not equal b, this will not print
    if a != b:  # not equal (!=) also evaluates to "True" or "False"
        print(a, b) # this will print
    # Also keep in mind that <, <=, >, >=, will also evaluate to True or False

    ''' Basic types... used like booleans? What? '''
    a = 0  # ints with value 0
    b = ""  # empty strings
    c = []  # and empty lists ALL EVALUATE TO FALSE
    # ints > or < 0, non-empty strings, and non-empty lists all evalue to TRUE
    if a:
        print(a)  # will not run!
    if b:
        print(b)  # will not run!
    if c:
        print(c) # will not run!

    ''' and / or '''
    a = True
    b = False
    if (a and b):
        print(a)  # This will not run
    if (a or b):
        print(b)  # This will run

    return


def if_elif_else_examples():
    a, b, c = 1, 2, 3  # defining similar types this way is allowed, a=1, b=2, c=3

    ''' the basics of logic are if->then statements, here are some examples '''
    if a == 1:  # if the value of a is equal to 1
        print(a)  # then do this

    ''' if the condition of "if" is NOT met, we can use alternate conditions '''
    if a == 2:  # if a equals 2
        print(a)
    elif b == 2:  # else if b equals 2
        print(b)  # this will run
    # However, if the condition of "if" IS met, then elif will NOT be run.
    # if BOTH checks are needed, use two "if"s.

    ''' else is a "catchall", and will run if no other conditions are met '''
    if a == 3:  # nope
        print(a)  # will not run
    elif b == 3:  # nope
        print(b)  # will not run
    else:
        print(c)  # will run

    return


def loop_examples():
    ''' there are two basic loops in python, "while" and "for" '''
    a = 0  # this is a counter-loop
    while (a < 100):  # while a is less than 100
        print(a)  # print a
        a += 1  # add one to a
        # prints 0->99.  Will not print 100, why?

    st = "Hello, World!"  # this is standard iteration
    for ch in st:  # read it like this "For character in string"
        print(ch)  # print character.  Try this in the interpreter
        # prints each character in "Hello, World!" on a new line

    '''Sometimes we'll want to use a counter for iterating a list'''
    ls = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    for n in range(len(ls)):  # xrange returns a range of numbers from 0 to the number provided.
        print(ls[n])  # in this case, n equals 0-8.  Notice there are 9 items in ls, but the iteration starts at 0!
    # this will print each character in ls on a new line
    return


def an_example_of_how_to_pause_your_program():
    # the input() cheat - makes the script stop until you press a key
    # this can be useful for debugging, or if you just want to pause for a moment
    print("I AM ON YOUR SCREEN")
    input()   
    print("TAKING UP YOUR SPACE")
    input("(this time there is a message)")
    print("HERP HERP")
    a = input("now type a bunch of things and press enter")
    print(a)
    input("paused again")
    return

if __name__ == "__main__":
    basic_types()

    boolean_examples()

    if_elif_else_examples()
    
    loop_examples()

    an_example_of_how_to_pause_your_program()
