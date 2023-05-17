#include <stdio.h>
#include "linked_list.h"

int main() {
    struct node* head = new_node(0x1337);
    struct node* node;

    int idx;
    for (idx = 0; idx < 10; idx++) {
        node = new_node(idx*idx);
        add_node(head, node);
    }
    print_list(head);
    free_list(head);

    return 0;
}
