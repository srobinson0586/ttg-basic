#ifndef UTILS_H
#define UTILS_H

#include <arpa/inet.h>
int get_server_address(int argc, char** argv, struct sockaddr_in* server_addr);

#endif
