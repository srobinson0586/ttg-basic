# C Programming Stack - Knowledge Check

[Back to README](README.md)

1. Explain the significance of the stack pointer in C programming. How does it dynamically adjust during push and pop operations?
```
ANSWER:

```

```SOLUTION
The stack pointer is a register or memory location that points to the top of the stack in C programming. It dynamically adjusts during push and pop operations, ensuring accurate tracking of the top of the stack. During push, the stack pointer is decremented to allocate space, and during pop, it is incremented to release space. It plays a central role in managing the stack's memory.
```

2. What is the purpose of the deallocation process in the C programming stack?
```
ANSWER:

```

```SOLUTION
The deallocation process in the C programming stack involves releasing or freeing up the memory occupied by a function's stack frame after the function completes its execution and returns. Proper deallocation ensures efficient memory management, prevents memory leaks, and contributes to resource efficiency. 
```
3. Explain one consequence of a stack overflow in a C program.
```
ANSWER:

```

```SOLUTION
One consequence of a stack overflow is a program crash or termination. When the stack surpasses its maximum capacity, it can lead to undefined behavior, and the program may no longer execute correctly.
```

[Back to README](README.md)