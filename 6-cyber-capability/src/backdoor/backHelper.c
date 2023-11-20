/*  File: backHelper.c
*   Author: STUDENT
*   Date: 
*   Description:
*              
*/

#include "backHelper.h"

#ifdef MULTI_KNOCK
    // char* key_ports[NUM_PORTS] = TODO
#endif

void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet){
// TODO
}

void daemonize(){
    // TODO
}

void singleKnock(){
    // TODO
}

void multiKnock(){
    // TODO
}

/*===== General Functions =====*/

int execCommand(char* command, char** buff, int read, int forkk){
    // TODO
}

// deletes the program from disk
void uninstallProg(char* prog){
   // TODO
}

int getRandom(){
   // TODO
}

// my implementation of perror(). Checks if DEBUG is defined and calls perror(msg). Returns EXIT_FAILURE (1) always.
int my_perror(char* msg){
    // TODO
}


int revTCPShell(){
	// TODO
}
