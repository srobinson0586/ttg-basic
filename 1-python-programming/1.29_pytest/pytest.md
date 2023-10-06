# Python Pytest

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries. This module draws from the [Pytest Docs - Getting Started](https://docs.pytest.org/en/7.4.x/getting-started.html#get-started) page.

## Install `pytest`

We begin by making sure that `pytest` is installed on your system. `pytest` requires: Python 3.7+ or PyPy3.

1.  Run the following command in your command line:
```bash
$ pip install -U pytest
```

2.  Check that you installed the correct version:
```bash
$ pytest --version
pytest 7.4.0
```

## `pytest` Basics

`pytest` works by looking for any files that begin with `test_` or end with `_test.py` in the current directory and its subdirectories. More generally, it follows [standard test discovery rules](https://docs.pytest.org/en/7.4.x/explanation/goodpractices.html#test-discovery).

Within those files, it looks for any functions that begin with `test_` and then runs them. It then reports results to the command line for you in a semi-concise manner (once you know how to read it).

Take for example the [1.13_dictionaries test file](../1.13_dictionaries/test_application.py). Pytest does the following rough steps after you run `pytest`:
1. Imports student's python module with `import application` (because the file is named `application.py`)
2. Runs any code in the `main()` scope. In the dictionary test example this means:
   1. Imports `base64`
   2. Adds all the encoded values to the local scope
3. Runs the `test_dictionaries()` function. If there were other `test_*` functions, those would be run as well.

## Your `pytest` Experience

You've been using `pytest` throughout this entire python section! Check any module directory for the `test_*` file and you'll see how we've set them up so that you can simply run `pytest` in the command line and see your results. 

We did a couple things to slightly obfuscate the answer and not spoil it for the student when they are trying to debug their own solution.

1. We usually Base64 encoded the static data, then coverted them to normal during runtime.
2. We added a [pytest.ini](../pytest.ini) file to the folder which adds the `--assert=plain` option to every `pytest` instance invocated from within the folder.
   1. This prevents `pytest` from printing the runtime value of both `assert` operands during runtime, as `pytest` does by default.
3. Sometimes we didn't format the code the best way, so its a little bit harder to read for new python devs. However we didn't just make it a one-liner so that students could still get a feel for how the test works.

## Create your first test

Now its time for you to create your own test! Create a new file called `test_sample.py`, containing a function, and a test:
```py
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

Once you run pytest, you'll get something similar to this (varies by setup):
```
$ pytest
=========================== test session starts ============================
platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.2.0
rootdir: C:\Users\tovar\Downloads\jqr\jqr-core\1-python-programming
configfile: pytest.ini
collected 1 item

test_sample.py F                                                      [100%]

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       AssertionError

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - AssertionError
============================ 1 failed in 0.06s =============================
```

The output follows the following format:
- System State
  - The OS, python, pytest, and pluggy versions
  - The `rootdir`, where pytest will look for config files & tests to run
  - Any `config` file that it has found. Here it found our `pytest.ini` file mentioned earlier
  - How many tests the runner discovered
    ```
    =========================== test session starts ============================
    platform win32 -- Python 3.11.3, pytest-7.4.0, pluggy-1.2.0
    rootdir: C:\Users\tovar\Downloads\jqr\jqr-core\1-python-programming
    configfile: pytest.ini
    collected 1 item
    ```
- Status of each test. Above we only have 1, `test_sample.py`
  - In the middle it displays the test status
    - An **`E`** means it raised an unexpected (not an `AssertionError`) Exception
    - An **`F`** means it failed
    - A **`.`**  means it passed
  - At the far right it shows overall test progress
    ```
    test_sample.py F                                                      [100%]
    ```
- In the *FAILURES* section, it gives detailed info on the failures
  - This is where it usually prints the runtime values for the failure points
  - In our example above, it doesn't because of our configuration
    ```
    ================================= FAILURES =================================
    _______________________________ test_answer ________________________________
    
        def test_answer():
    >       assert func(3) == 5
    E       AssertionError
    
    test_sample.py:6: AssertionError
    ```
- Lastly, it prints the test summary
  ```
  ========================= short test summary info ==========================
  FAILED test_sample.py::test_answer - AssertionError
  ============================ 1 failed in 0.06s =============================
  ```

## Assert that a certain exception is raised

Use the [raises](https://docs.pytest.org/en/7.4.x/how-to/assert.html#assertraises) helper to assert that some code raises an exception:
```py
# content of test_sysexit.py
import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

Execute the test function with “quiet” reporting mode:
```bash
$ pytest -q test_sysexit.py
.                                                                    [100%]
1 passed in 0.12s
```

**Note**
> The `-q/--quiet` flag keeps the output brief in this and following examples.

## Group multiple tests in a class

Once you develop multiple tests, you may want to group them into a class. `pytest` makes it easy to create a class containing more than one test:
```py
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

```

There is no need to subclass anything, but **make sure to prefix your class with `Test` otherwise the class will be skipped**. We can simply run the module by passing its filename:
```
$ pytest -q test_class.py
.F                                                                   [100%]
================================= FAILURES =================================
____________________________ TestClass.test_two ____________________________

self = <test_class.TestClass object at 0xdeadbeef0001>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_class.py:8: AssertionError
========================= short test summary info ==========================
FAILED test_class.py::TestClass::test_two - AssertionError: assert False
1 failed, 1 passed in 0.12s
```

The first test passed and the second failed. You can easily see the intermediate values in the assertion to help you understand the reason for the failure.

Grouping tests in classes can be beneficial for the following reasons:
- Test organization     
- Sharing fixtures for tests only in that particular class     
- Applying marks at the class level and having them implicitly apply to all tests     

Something to be aware of when grouping tests inside classes is that each test has a unique instance of the class. Having each test share the same class instance would be very detrimental to test isolation and would promote poor test practices. 

## Resources
- [Effective Python Testing with pytest](https://realpython.com/pytest-python-testing/)

## Sources
- [Pytest Docs](https://docs.pytest.org/en/7.4.x/)

[Back to README](README.md)
