# Let's go through the "application" binary in GDB

1. Start GDB with the compiled executable:
```sh
gdb application
```
2. Run the program inside GDB:
```sh
gef➤ run
```
3. Set a breakpoint at the main function:
```sh
gef➤ break main
```
5. Run the program again (it will stop at the breakpoint):
```sh
gef➤ run
```
6. Step through the code line by line:
```sh
gef➤ next
```
Keep pressing "enter" and see what happens. It will go to the next line again. Keep going until you see "return 0"

7. Inspect variables:
```sh
gef➤ print a  # Prints the value of variable 'a'
gef➤ print b  # Prints the value of variable 'b'
gef➤ print sum  # Prints the value of variable 'sum'
```
8. Continue running the program until the next breakpoint or the end:
```sh
gef➤ continue
```
9.  List the source code around the current line:
```sh
gef➤ list
```
10.  Exit GDB:
```sh
gef➤ quit
```