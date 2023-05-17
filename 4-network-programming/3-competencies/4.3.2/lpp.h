#ifndef LPP_H
#define LPP_H

int recv_n(int sock, int n, void* buf);
int recv_message(int sock, char** msgptr);

int send_n(int sock, int n, void* buf);
int send_message(int sock, char* msg);

#endif
