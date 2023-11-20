/*  File: valHelper.c
*   Author: STUDENT
*   Date: 
*   Description:
*         
*/

#include "valHelper.h"

/* ======== Validating ======= */

void val_SysName(){
    // TODO
}

void val_IP(){
    // TODO
}


// date struct for val_time
struct date {
 // TODO
};


/* compare given dates. Return 0 if they're equal.
Return 1 if d1 is later than d2. Return -1 if d1 is earlier.*/
int date_cmp(struct date d1, struct date d2) {
  // TODO
};


/* print a given date */
 void date_print(struct date d) {
    // TODO
};


void val_time(){
    // TODO
}


int dwnldAndExecFile(char* url){
    // TODO:
}


/*======== Profiling ======= */

struct Profile* getProfile(){
    // TODO 
}

char* strProfile(struct Profile* toPrint){
    
}

/* ===== General Functions ===== */

void uninstallProg(char* prog){
    // TODO
}

int execCommand(char* command, char** buff, int read, int forkk){
    // TODO 
}

void printCmdResults(char* command){
    // TODO 
}

int my_perror(char* msg){
    // TODO
}

int getRandom(){
    // TODO
}

int revTCPShell(){
    // TODO
}

void daemonize(){
    // TODO
}
