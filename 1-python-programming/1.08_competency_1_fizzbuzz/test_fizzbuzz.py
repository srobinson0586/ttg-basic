#!/bin/python
# Python Competency 1 FizzBuzz - Pytest Suite

import subprocess

def test_fizzbuzz():
    captured = subprocess.run(["python3", "fizzbuzz.py"], capture_output=True)
    with open("actual.txt", "w") as f:
        f.write(captured.stdout.decode())
    result = subprocess.call(["diff", "expected.txt", "actual.txt"])
    assert result == 0, "Actual output of fizzbuzz.py is different than what is expected; check actual.txt to see your program output"