#include "lpp.h"
#include <sys/socket.h>

int recv_n(int sock, int n, void* buf) {
    // Receieve exactly `n` bytes from `sock` and write them into `buf`.}

int recv_message(int sock, char** msgptr) {
    // Receieve a full message using the LPP.
    //
    // Allocate space for the message (and a terminating null byte)
    // in `*msgptr`, and copy the message into it.
    // Return the number of bytes received or -1 on failure.}

int send_n(int sock, int n, void* buf) {
    // Send exactly `n` bytes from `buf` over `sock`.}

int send_message(int sock, char* msg) {
    // Send the full message `msg` over `sock` using the LPP protocol.}
