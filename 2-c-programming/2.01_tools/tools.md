# C Programming Tools

One of the key distinctions between C and Python lies in their approach to code execution, specifically their interpretive and compiled natures. C is a **compiled** language, which means that the source code is first translated entirely into machine code by a compiler before the program is executed. This compilation process optimizes the code for performance and produces an executable binary that can be directly run on the target hardware. 

On the other hand, Python is an **interpreted** language, where the source code is executed line by line by an interpreter at runtime. This [Tutorials Point Article](https://www.tutorialspoint.com/cprogramming/c_overview.htm) provides an overview of the potential usage of C applications.

As such, to start programming in C you'll need a few additional tools to compile and run your programs on your Linux Operating System: 

- Compiler: `gcc` (GNU Compiler Collection)
- Build Tool: `make` (a build automation tool to manage compilation and linking)
- Debugger: `gdb` (gnu debugger) and `gef` (gdb addon tool; pronounced "Jeff")

## Development Environment

The following guide will walk you through the step-by-step process of installing a C complier and configuring Visual Studio Code (VSCode) on your Linux Operating System.

### Step 1: Install build-essential Package and additional tools
The build-essential package contains the dependencies to setup your C programming environment tools, i.e gcc, make, etc.  Run the following command in a Terminal to update and install the package:

```bash
$ sudo apt update && sudo apt install build-essential gdb
```

Enter your system password when prompted, Press `Y` when asked for confirmation and wait for the installation to complete.

To verify versions of `gcc`, `make` and `gdb` installed, you may run the following commands:

```bash
$ gcc --version
$ make --version
$ gdb --version
```
### GEF via the install script

GEF is an add-on to GDB that adds a set of commands to assist exploit developers and reverse engineers. We will explore GEF later in the JQR. There are multiple ways you may install GEF:

#### using curl
```bash
$ sh -c "$(curl -fsSL http://gef.blah.cat/sh)"
```

#### manually
```bash
$ wget -O ~/.gdbinit-gef.py -q http://gef.blah.cat/py
$ echo source ~/.gdbinit-gef.py >> ~/.gdbinit
```

#### Check GEF install
```bash
$ gdb -q /path/to/my/bin
```

### Step 2: Install the Microsoft C Extension in VSCode
1. Open up VSCode, then click on the `Extensions` icon in the left sidebar (represented by four squares).
1. In the `Extensions` search bar, type "C/C++" and press `Enter`.
1. Look for the official C/C++ extension by Microsoft and click on the `Install` button.
1. Wait for the installation to complete, and then click on the `Reload` button to activate the extension.

### Step 3: Install the clangd Extension in VSCode
1. Open up VSCode, then click on the `Extensions` icon in the left sidebar (represented by four squares).
1. In the `Extensions` search bar, type "clangd" and press `Enter`.
1. Click on the `Install` button.
1. Wait for the installation to complete, and then click on the `Reload` button to activate the extension.

## Resources

- [Tutorialspoint - Basic Syntax](https://www.tutorialspoint.com/cprogramming/c_overview.htm)
- [GCC Official Website](https://gcc.gnu.org/)
- [Ubuntu build-essential package](https://packages.ubuntu.com/focal/build-essential)
- [GEF GitHub Repository](https://github.com/hugsy/gef)
- [C/C++ for Visual Studio Code](https://code.visualstudio.com/docs/languages/cpp)

[Back to README](README.md)