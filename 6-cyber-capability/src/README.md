# Contents 

> You will update this as you go, but for now you've got my templates and starter code in here. **EVERYTHING IN THIS DIRECTORY IS A TEMPLATE**. You can change it up as you like, as long as you meet the specified requirements!

In this directory you will find the actual programs that you will be using.

The [BuildAndConfig](#buildandconfig) directory contains the Macros, `#includes`, and functions used in both programs. It also contains the compiler python script that *Builders* would use to build both stages.

The [Validator](#validator) directory contains the code used to run the first stage program.

The [Backdoor](#backdoor) directory contains the code used to listen for portknocks and establish a return shell.

---
# `BuildAndConfig/`

This directory holds the script used to compile, which is what builders/operators will use to create and customize their payloads.

It also holds `functionality.h` which is used to keep things used in both of the programs.

Lastly, it holds a log file that keeps track of the arguments used in the compiler script as well as any failure or success messages.

## compiler.py
This python script provides an easy to use interface that is used to compile both programs at the same time. The user is able to specify options listed using `./compiler.py -h`. All the options have default values, providing convenience and reducing user burden.

The script can also be used to run the validator program with the `-r` option or `-v` for valgrind.

## functionality.h
This file is used to define configurable compile-time Macros, `#includes`, and functions for both programs in one place.

The names for the Macros used here are used throughout the program and script so be conscious of dependencies when refactoring.

Uncomment them if you aren't working with the python build script and don't want to write them all out on the command line. They each have some defaults.

Only one of `SINGLE_KNOCK` or `MULTI_KNOCK` should be defined at a time.

### Macros
| Macro | Default | Description |
| ----- | ------- | ----------- |
| DEBUG | 1 | Used for debugging. Mostly console printing. |
| INTERFACE | TODO | Interface to listen on. |
| NO_DAEMON | NOT_DEFINED | Define when you DON'T want to run the backdoor as a daemon. |
| SINGLE_KNOCK | TODO | Used for listening on a single port. Specifies the port value. |
| MULTI_KNOCK | TODO | Used for listening on multiple ports.  Specifies the port values, in order. |
| NUM_PORTS | TODO | Amount of ports that will be knocked. Required only for MULTI_KNOCK. `len(MULTI_KNOCK).` |
| REV_SHELL_IP | "127.0.0.1" | Used to open a reverse tcp shell on the specified ip & port. |
| REV_SHELL_PORT | 8008 | Remote port to connect to. |
| SLEEP | 3 | If defined, the programs will sleep for x seconds after process execution. If not defined, sleeps `Rand([1,6])` seconds. |
| PERSIST | 1 | Use to prevent uninstalling of the executables after execution. The backdoor also establishes a cron job. |
| VALID_SYSNAME | "Linux" | Target OS. |
| VALID_IP | "127.0.0.1" | Target IP. |
| VALID_TIME | 1 | Time is only validated if this is defined. |
| WORK_START | 8  | Used to only download backdoor during 'work hours'. |
| WORK_END   | 19 | Used to only download backdoor during 'work hours'. |
| START_DATE | TODO | If defined ("*MM/DD/YYYY*") and date < START_DATE, validator will sleep until after the start_date. |
| END_DATE | TODO | If defined  ("*MM/DD/YYYY*") and date > END_DATE, validator will exit and uninstall.
| URL | "http://0.0.0.0:9009/backdoor.out" | URL at which to download the backdoor payload. |

### Functions
| Function | Short Description |
| -------- | ----------- |
| `void uninstallProg(char* prog);` | Deletes the program from disk |
| `int my_perror(char* msg);` | My implementation of perror() |
| `int execCommand(char* command, char** buff, int read, int forkk);` | Executes the command using `popen` & forks if `forkk==1` |
| `int getRandom();` | Returns a random num between 1 & 15. Used for `sleep()`s |
| `int revTCPShell();` | Creates a reverse tcp shell that tries connecting to `IP:Port` |
| `void daemonize();` | Used when running the dropper as a Daemon is specified as an option. Returns EXIT_FAILURE on failure. |

---
# `validator/`

This directory contains the code for the **first stage implant**. The program takes compile-time arguments in the form of macros and verifies that the host it is run on meets the parameters.

## validator.c
This is the `main()` program that drives the first stage. If the verification parameters are satisfied, this downloads a second stage backdoor at `URL` to `/tmp/syslogd/<filename>`.

The download will fail if there is another file in the `/tmp/syslogd` directory, which doesn't normally exist. The directory is created during the file download process.

It also deletes itself after it's done executing. More profiling will be implemented in future versions.

## valHelper.h
This is the header file for the validator first stage. It declares auxiliary functions used in the validator program for various tasks. It also contains includes used specifically by the validator.

### Structs
|  Struct  | Description |
| -------- | ----------- |
| `struct Profile`| Struct used to create a detailed profile of the host machine |

### Functions
| Function | Description |
| -------- | ----------- |
| `void val_IP();` | Exits if VALID_IP macro is not the hosts's actual ip address. Does nothing otherwise |
| `void val_SysName();` | Exits if VALID_SYSNAME macro is not the hosts's actual ip address. Does nothing otherwise |
| `void val_time();` | Called after making sure it is a target machine with above functions. Sleeps until `WORK_START_T < localtime < WORK_END_T`. Exits in failure if current date is after the `END_DATE` |
| `int dwnldAndExecFile(char* url);` | Downloads a file at the specified url to `/tmp/syslogd/<file>`. Returns 0 if successful, 1 otherwise. |
| `struct Profile* getProfile();` | Returns a Profile with `NAN/-1` for invalid responses |
| `char* strProfile(struct Profile* toPrint);` | Returns a string with a bunch of profile info. User must free() the returned str when done. |
| `void printCmdResults(char* command);` | For debugging. Calls execCommand(), prints it, and frees the memory |

## valHelper.c
Defines the functions declared in `valHelper.h` as well as functions declared in the [functionality.h](buildAndConfig/functionality.h) file that are used by both the validator and backdoor programs.

---
# `backdoor/`
This directory contains the second stage backdoor program. The resulting executable program is downloaded by the validator from whatever URL you specify at compile time.

## backdoor.c
This is the `main()` driver of the backdoor second stage program. It sniffs the specified `INTERFACE` (thus it requires sudo privIleges) for port knocking on the ports specified at compile time with either `SINGLE_KNOCK` or `MULTI_KNOCK`.

It starts a shell connection (`/bin/sh`) using a socket at `REV_SHELL_IP`:`REV_SHELL_PORT`. When using `MULTI_KNOCK`, they must be knocked in order.

If daemonized, it deletes itself from the directory but still listens and returns a connection when knocked!

## backHelper.h

Declares auxiliary functions and Macros used in the backdoor program. Contains includes used specifically by the backdoor.

### Structs
| Function | Description |
| -------- | ----------- |
| `struct sniff_ethernet {}` | Ethernet Header |
| `struct sniff_ip {}` | IP Header |
| `struct sniff_tcp {}` | Used to define / compute tcp header offset |

### Macros
| Macro | Default | Description |
| ----- | ------- | ----------- |
| `SNAP_LEN` | TODO | Default snap length to be set on a pcap handle |
| `SIZE_ETHERNET` | TODO | Ethernet Header Size |
| `ETHER_ADDR_LEN` | TODO | Ethernet addresses bytes |

### Functions
| Function | Short Description |
| -------- | ------------------------------- |
| `void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet);` | Verify and keep track of successful port knocks. Then call the corresponding functions |
| `void singleKnock();` | Gets called when the single knock port option is activated. |
| `void multiKnock();` | Multiple knocked ports |

## backHelper.c
Defines the functions declared in backHelper.h as well as functions declared in the [functionality.h](buildAndConfig/functionality.h) file that are used by both the validatory and backdoor programs.
