import random

def get_words(filename):
    """ Reads the entire set of valid words from a file.

    The file will have all words in lowercase, each on
    their own line, with no extra punctuation or whitespace
    besides new lines.

    Return value: a set of all the words """


def validate_guess(guess, valid_words):
    """ Checks if a guess is valid.

    Print out informative messages if any of these conditions
    are violated (in which case this function should return
    False):
    a. The guess must contain only letters (no spaces or punctuation).
    b. The guess must contain exactly 5 letters.
    c. The guess must be in the valid word set.

    Return value: True if conditions (a), (b), and (c) above
    are met; False otherwise. """

def get_guess(guess_num, valid_words):
    """ Gets a valid guess from the user.

    Print out a prompt for the user, including the current
    guess number (out of 6), and then get their input.
    Make sure their guess is valid using `validate_guess` above.
    If the guess is not valid, continue prompting the user for
    input until a valid one is given.

    Return value: the user's valid guess, converted to lowercase. """

def evaluate_guess(guess, correct):
    """ Evaluates each letter in the guess to determine if
    Wordle would mark it gray, yellow, or green.

    If you're not familiar with Wordle you'll need to look up the
    coloring scheme.

    Return value: a new 5-character string in which each character
    indicates the correct-ness of the corresponding letter in the
    guess:
    a. '-' => gray
    b. '.' => yellow
    c. '*' => green

    E.g., if the correct word is 'mouse' and the guess was
    'sound', then the return value should be '.**  '. Summary:
        correct: 'mouse'
        guess:   'sound'
        return:  '.**--'

    This is by far the trickiest part of the exercise! Be sure to
    account for letters that appear twice in the guess or the actual
    word. Here's a good test case to think about:
        correct: 'robot'
        guess:   'oodle'
        return:  '.*---'
    """

def play():
    """ Runs a game of Wordle for the user.

    Give them 6 guesses. Print out some sort of separator
    between guesses to make things easier to read. If they
    guess the word correctly within 6 tries, congratulate
    them and exit. Otherwise, print out the correct word and
    then exit.

    Return value: None. """

def test_evaluate():
    """ Run some test cases for evaluate_guess. """

    corrects = ["mouse", "robot", "scale", "hello", "hello", "robot", "petal", "flail"]
    guesses  = ["sound", "oodle", "shall", "label", "later", "tutor", "tutor", "lilly"]
    results  = [".**--", ".*---", "*-**-", ".--..", ".--.-", ".--*.", "--*--", "...--"]

    success = True
    for c, g, r in zip(corrects, guesses, results):
        if evaluate_guess(g, c) != r:
            print("Error: evaluate_guess({}, {}) should be {}".format(g, c, r))
            print("Your function returned {}".format(evaluate_guess(g, c)))
            success = False

    if success:
        print("The built-in evaluate_guess tests passed!")
    else:
        print("At least 1 built-in evaluate_guess test failed :(")

if __name__ == "__main__":
    play()
