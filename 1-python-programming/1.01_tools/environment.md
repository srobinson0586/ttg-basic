# Python Environment

[Back to README](README.md)

This guide will walk you through the step-by-step process of installing Python and configuring Visual Studio Code (VSCode) on your Linux system.

Step 1: Installing Python
-------------------------
1. Open a terminal on your Linux system.
1. Check if Python is already installed by running the command -
    ```bash
    $ python3 --version
    ```
    If Python is installed, you'll see the version number; otherwise, you'll need to install it.
1. Install Python by running the following command -
    ```bash
    $ sudo apt install python3
    ```
    Enter your system password when prompted and wait for the installation to complete.

### Step 2: Installing the Python Extension in VSCode
1. Open up VSCode, then click on the Extensions icon in the left sidebar (represented by four squares).
1. In the Extensions search bar, type "Python" and press Enter.
1. Look for the official "Python" extension by Microsoft and click on the "Install" button.
1. Wait for the installation to complete, and then click on the "Reload" button to activate the extension.

### Step 3: Running Python Code
1. To run your Python code, use the VSCode terminal. Click on "View" -> "Terminal" or press `` Ctrl + ` `` to open the integrated terminal.
1. In the terminal, make sure the correct Python interpreter is selected by running `python3 --version`.
1. To run a Python file, use the command: `python3 <filename.py>`. Replace `<filename.py>` with the actual name of your Python file.
1. The output of your code will be displayed in the terminal.
> Note: You can also press the triangle play button in the top right corner to run your code.

Congratulations! You have successfully installed Python and set up VSCode for Python development on your Linux system. Now you're ready to explore the world of Python programming with a powerful and user-friendly development environment.