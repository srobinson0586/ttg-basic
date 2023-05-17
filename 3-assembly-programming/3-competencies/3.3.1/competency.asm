section .text

GLOBAL lab1_1
GLOBAL lab1_2
GLOBAL lab1_3
GLOBAL lab1_4
GLOBAL lab1_5
GLOBAL lab1_6
GLOBAL lab1_7
GLOBAL lab2_1
GLOBAL lab2_2
GLOBAL lab2_3
GLOBAL lab2_4
GLOBAL lab3_1
GLOBAL lab3_2
GLOBAL lab3_3
GLOBAL lab3_4
GLOBAL lab3_5
GLOBAL optional_1
GLOBAL optional_2
; +---------------------------------+
; |     /\       _______            |
; |    /  \     |          |\    /| |
; |   /____\    |_______   | \  / | |
; |  /      \           |  |  \/  | |
; | /        \  ________|  |      | |
; +---------------------------------+

;; The basics of the Linux x64 calling convention:
;; - Arguments are passed in rdi, rsi, rdx, rcx, r8, r9, in that order.
;; - The return value is stored in rax.
;; You can reference the System V ABI manual for more details.

;; The Intel Manual, Volume 2 has detailed information about how each
;; instruction behaves.

;; Good luck! Have fun!

;; N.B.: You can make a label local to the scope of the current function
;; by prefixing it with a "." (e.g., ".locallabel:").
;; This can be helpful if you want to have lots of "loop" or "ret" labels
;; in different functions. You can name them all ".loop" and ".ret"
;; instead of coming up with a name-mangling scheme to keep them all
;; unique.
;; In general, all your labels except actual functions should be local.

;; lab1 recommended instructions:
;; add, sub, imul, idiv, mul, div, shl, shr, xor, ror, rol, xchg

;; int lab1_1(int a, int b);
;; Return the product of `a` and `b`.
lab1_1:
    ;; TODO: Implement this function.





;; int lab1_2(int n);
;; Return `a` * 8.
lab1_2:
    ;; TODO: Implement this function WITHOUT USING mul or imul.





;; No C prototype.
lab1_3:
    ;; TODO: Exhange the values in rcx and rdx WITHOUT USING xchg.





;; long lab1_4(long a, long b, long c, long d);
;; Return (c - b) * d / a.
lab1_4:
    ;; TODO: Implement this function.





;; short lab1_5(short a, short b);
;; Return a new short with the high byte from `a` and the low byte from `b`.
;; E.g., lab1_5(0x1234, 0xabcd) would be 0x12cd.
lab1_5:
    ;; TODO: Implement this function.





;; void lab1_6(int* p);
;; Return *p - 20.
lab1_6:
    ;; TODO: Implement this function.





;; int lab1_7(int x);
;; Return the result of interpreting `x` as big-endian instead of little-endian.
lab1_7:
    ;; TODO: Implement this function WITHOUT USING `bswap`.
    ;; Hint: I think the cleanest solution uses 3 `ror` instructions.






;; lab2 recommended instructions:
;; jmp, jcc, cmp, dec, inc

;; No C prototype.
lab2_1:
    ;; TODO: Implement the following pesudocode:
    ;; if(rdi != 0)
    ;;   if(rdi == 17)
    ;;       rbx = 1
    ;;   else
    ;;       rbx = 2
    ;;   if(rsi == 17)
    ;;       rcx = 1
    ;;   else
    ;;       rcx = 2
    ;; else
    ;;   rcx = 100





lab2_2:
    ;; TODO: Implement the following pseudocode:
    ;; do {
    ;;    rsi *= 2
    ;;    rdi *= 3
    ;; } while(rsi > rdi)





;; int lab2_3(int a, int b, int c, int d);
;; Return:
;;  c + 42  (if a is 1)
;;  0,      (if a is 2)
;;  b - d   (if a is 3 or 4)
;;  50      (otherwise)
lab2_3:
    ;; TODO: Implement this function.





;; int lab2_4(int n);
;; Return the number of integer factors of `n`.
;; E.g., lab2_4(8) is 4 because 8 is divisible by 1, 2, 4, and 8.
lab2_4:
    ;; TODO: Implement this function.





;; void lab3_1(char* s);
;; Change the 4th character of `s` to 'a'.
lab3_1:
    ;; TODO: Implement this function.






;; long lab3_2(char* s);
;; Return the length of the null-terminated string `s`.
lab3_2:
    ;; TODO: Implement this function, without calling `strlen`.





;; void lab3_3(char* dst, char* src, int len);
;; Copy over the string `src` to `dst` for `len` characters, but change all
;; lowercase 'a' and 'o' characters to their uppercase equivalent.
lab3_3:
    ;; TODO: Implement this function.





extern strncpy
;; void lab3_4(int len, char* dst, char* src);
;; Equivalent to strncpy(dst, src, len).
lab3_4:
    ;; TODO: Implement this function by rearranging the arguments and
    ;; calling `strncpy`.
    ;; You will need to declare `strncpy` as `extern`.





;; void lab3_5(char* filename, char* s, int len);
;; Write the null-terminated `s` (with length `len`) to the file named
;; `filename`.
;; This will create the file if it does not exist or truncate it if it does.
lab3_5:
    ;; TODO: Implement this function.
    ;; You must use system calls to perform the file operations (open,
    ;; write, and close).

    ;; Hint: you can find the system call numbers online, or you can grep
    ;; for their definitions in /usr/include/. They are defined as
    ;; `SYS_open`, etc., which is an alias for `__NR_open`, which is defined
    ;; in a bunch of different header files for different architectures.
    ;; You should look at the ones with "amd64" in the header name.

    ;; Hint: Pay really close attention to the `flags` and `mode` you pass
    ;; to open. You can find all the details in the open(2) man page. Then
    ;; you can find the actual numerical definition of the flags you're
    ;; interested in by grepping for them in /usr/include/.

    ;; You can use the `strace` utility to debug the system calls you're
    ;; making. It can also tell you what flags you're actually passing to
    ;; the system calls.






optional_1:
;Implement the following Function-
; Take in 2 buffers
; Capitalize all letters in null-terminated src
; and save off the changed string to the dst buffer
; int capitalize(char *dst, char *src)
    ;; TODO: Implement this function.





optional_2:
;Requirement:
; read user input from stdin and
; echo what user inputted to stdout
; void echoInput(char *buf, int strLen)
    ;; TODO: Implement this function.




