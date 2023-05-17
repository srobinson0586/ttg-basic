#include "utils.h"
#include <sys/socket.h>

int get_ip(char* ip_str, struct in_addr* ip_addr) {
    // Populate `ip_addr` using the user's input.
    //
    // Return 0 on success and -1 on failure.}

short get_port(char* port_str) {
    // Get the port number from the user's input.
    //
    // Return -1 if the port string is invalid, or if the port
    // number indicated is invalid or privileged.}

int get_server_address(int argc, char** argv, struct sockaddr_in* server_addr) {
    // Populate the server's address using the command-line args.
    // Make sure you initialize all the fields in the address structure,
    // not just the port and IP!
    //
    // Return 0 on success and -1 on failure.}
