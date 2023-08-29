#!/bin/python
# Python <subject> - Pytest Suite

import application
import subprocess

def test_loops():
    expected = "".join([str(i)+"\n" for i in range(1, 51)])
    expected += "".join(i+"\n" for i in application.cars)
    expected += "".join(i+"\n" for i in application.animals if i[0] == 'c')
    completed = subprocess.run(["python3", "application.py"], capture_output=True)
    assert completed.stdout.decode() == expected, "Incorrect output"