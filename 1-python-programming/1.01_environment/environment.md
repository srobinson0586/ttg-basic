# Python Environment


This guide will walk you through the step-by-step process of installing Python and configuring Visual Studio Code (VSCode) on your Linux Operating System. 

**The JQR teaches python following Python 3 specifications**. There are 2 versions of Python, Python2 and Python3. There are slight differences between them, and Python 2 is considered deprecated. Therefore, everything in the JQR is to be taken in the context of a Python3 application. For more on the difference between the two, this [Tutorialspoint Article](https://www.tutorialspoint.com/python3/python3_whatisnew.htm) provides a brief overview.


## Installing Visual Studio Code

First, you need to install VS Code, a beginner developer's best friend. According to the [official website](https://code.visualstudio.com/docs), "Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux." Feel free to follow along with their videos for a good introduction to the power of VS Code.

You can easily install VS Code on Windows from the Microsoft Store. For Linux, please follow the [Official Docs](https://code.visualstudio.com/docs/setup/linux), or find a good video.

Once you've installed VS Code, feel free to personalize it by setting your own Key Bindings, changing the Color Theme, and fonts! Just click FILE &rarr; PREFERENCES at the top left.

## Installing Python / Pytest

For Windows, python can be installed from the Microsoft Store. However that version may be out of date. It is recommended to download the latest *stable* release from the [Python Website](https://www.python.org/downloads/windows/). 

Installation on Linux requires more command line work. If you aren't familiar with the Linux command line, inform the TRAINO so that you can be pointed to resources and learn the basics needed to complete the JQR. A strong foundation of linux command line knowledge is required for any good CNO Developer, but its not currently something taught in the JQR. Many JQR students learn about it on their own time.

### Step 1: Installing Python in Linux
1. Open a terminal
2. Check if Python is already installed by running the command:
    ```bash
    $ python3 --version
    ```
    If Python is installed, you'll see the version number; otherwise, you'll need to install it.
3. Install Python by running the following command:
    ```bash
    $ sudo apt install python3
    ```
    Enter your system password when prompted and wait for the installation to complete.
4. Now, we need to install `pip`, the Python package manager (like `apt` for python)
    ```bash
    sudo apt install python3-pip
    ```
5. Lastly, we need to install the [`pytest` package](https://pypi.org/project/pytest/) which we use extensively throughout these modules and cover in detail in module [1.30_pytest](../1.30_pytest/README.md). 
    ```bash
    pip3 install pytest
    ```
> Its important to not use `sudo` when installing python packages with `pip`. BLUF: You will have to use `sudo` every time you try using a package that you installed with `sudo pip install`.
> More information on this nightmare can be found in this [stackoverflow thread](https://stackoverflow.com/questions/29310688/sudo-pip-install-vs-pip-install-user) (important read).

### Step 2: Installing the Python Extension in VSCode
1. Open up VSCode, then click on the Extensions icon in the left sidebar (represented by four squares).
2. In the Extensions search bar, type "Python" and press Enter.
3. Look for the official "Python" extension by Microsoft and click on the "Install" button.
4. Wait for the installation to complete, and then click on the "Reload" button to activate the extension.


### Step 3: Running Python Code
1. To run your Python code, you may use the VSCode terminal. Click on "View" &rarr; "Terminal" or press ``` "Ctrl + `" ``` to open the integrated terminal.
    - Keep in mind this is just a fancy window to integrate your native OS terminal. On Windows, VS Code simply opens a Powershell terminal. On Linux, it usually opens a Bash terminal (depends on your default shell).
2. In the terminal, make sure the correct Python interpreter is selected by running `python3 --version`.
3. To run a Python file, use the command: `python3 <filename.py>`. Replace `<filename.py>` with the actual name of your Python file.
4. The output of your code will be displayed in the terminal.

Congratulations! You have successfully installed Python and set up VSCode for Python development on your Linux system. Now you're ready to explore the world of Python programming with a powerful and user-friendly development environment.

## Programming in a Python Shell

The Python standard shell, or REPL (Read-Eval-Print Loop), allows you to run Python code interactively while working on a project or learning the language. This tool is available in every Python installation, so you can use it at any moment.

As a Python developer, you’ll spend a considerable part of your coding time in a REPL session because this tool allows you to test new ideas, explore and experiment with new tools and libraries, refactor and debug your code, and try out examples.

If you see three greater-than signs (`>>>`) and then python code either in the JQR or online, that means the code was written and ran in a python shell. Below is an example:
```py
>>> def my_func(): 
...     print("Hello")
... 
>>> my_func()
Hello
>>> a = "In a terminal, you don't have to call print() to print a variable's value!!!"  
>>> a
"In a terminal, you don't have to call print() to print a variable's value!!!"
```

It can be incredibly useful to debug small code snippets, and has some differences to running python code from a file. For a brief overview on it, checkout the quick [Python 101- The REPL](https://www.youtube.com/watch?v=ucllf6bDgnw) video (note IDLE isn't installed by default, contrary to his claim). For an in-depth overview, read the [Realpython Article](https://realpython.com/python-repl/) on it.

It is **HIGHLY** recommended that you run the small code snippets shown throughout the JQR yourself, not simply take us at our word. You can play around with the variables in the shell to truly understand the concepts.

> If the Python REPL shell isn't intuitive enough for you, try out the [python `IPython` module](https://pypi.org/project/ipython/)! It has syntax highlighting, tab completion, and many other features (check out the link).
> You can install it with `pip install ipython`. To run it from the terminal, do `python -m IPython`. To run it from within a script, you can use this one-liner: `import IPython; IPython.embed()`, and you will be able to execute python in the context of your script! This is useful for analyzing values of variables and any actions performed on them.

## Resources

- [Tutorialspoint- Python3 vs Python2](https://www.tutorialspoint.com/python3/python3_whatisnew.htm)
- [VS Code Docs](https://code.visualstudio.com/docs)
- [VS Code Linux Setup](https://code.visualstudio.com/docs/setup/linux)
- [Python Download- Windows](https://www.python.org/downloads/windows/)
- [Python 101- The REPL](https://www.youtube.com/watch?v=ucllf6bDgnw)
- [Realpython Article](https://realpython.com/python-repl/)
- [`IPython`](https://pypi.org/project/ipython/)
- 
[Back to README](README.md)
