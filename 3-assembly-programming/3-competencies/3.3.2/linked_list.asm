bits 64

;; These declarations will allow you to use these functions from libc.
extern malloc
extern free
extern printf

;; These declarations will allow the C program to reference your functions.

global new_node
global add_node
global free_list
global print_list


;; The NASM representation of a struct node.
;; This allows you to use the following macros:
;; - struct_node_size (for 12)
;; - struct_node.data (for 0)
;; - struct_node.next (for 4)
struc struct_node
    .data: resd 1
    .next: resq 1
endstruc
;; Note: Most compilers would add padding to this structure so that
;; the actual offset of `next` would be 8 (because it wants 8-byte
;; values to be located at addresses that are multiples of 8). In
;; our case, it's simpler to do it without the padding.


section .rodata
    ;; TODO: Create a format string to print out an integer using printf.
    ;; Use the `db` NASM command, and make sure you include a null-terminator!





section .text

;; struct node* new_node(int data);
;;
;; Allocate space for a new node, initialize the `data` field using the
;; given argument, and initialize the `next` field to NULL.
;;
;; Return the pointer to the allocated node.
new_node:
    ;; TODO: Implement this function.





;; void add_node(struct node* head, struct node* node);
;;
;; Add `node` at the end of the linked list starting at `head`.
;; You may assume that `head` is not NULL (i.e., that the linked list
;; already has at least 1 node in it).
add_node:
    ;; TODO: Implement this function.





;; void free_list(struct node* head);
;;
;; Free the memory for all nodes contained in the linked list starting at
;; `head`.
free_list:
    ;; TODO: Implement this function.





;; void print_list(struct node* head);
;;
;; Print out the `data` field (in hexadecimal, starting with '0x') for all
;; nodes in the linked list starting at `head`.
print_list:
    ;; TODO: Implement this function.




