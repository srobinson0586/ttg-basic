import sys
import struct
import datetime

# You can use this as a backdoor to shutdown the client and the server cleanly.
exit_msg = "exit"


def recv_n(socket, n):
    """ Receive exactly `n` bytes of data from `socket`.

    Remember that calling `socket.recv(n)` is NOT guaranteed to receive all
    `n` bytes. It will return the number of bytes received, and you may
    have to call it repeatedly to get all the data.

    Return the bytes read from the socekt, or None on error. """
def recv_msg(socket):
    """ Receive a single complete message on `socket`.

    Return the complete message (as a bytes string) or None on error. """

def send_msg(socket, msg):
    """ Send a complete string message (`msg`) on `socket`.

    Return True on success, False on error. """

#####################
### Miscellaneous ###
#####################

def get_port(port_str):
    """ Return the port number indicated by `port_str`.

    Raise a value error if the string does not represent a valid port
    (either not an integer, or not in the valid port range, or a restricted
    port number. """
def print_usage():
    """ Print out the command-line usage of client.py and server.py. """
    print("Usage: python3 {} <ipv6 address> <port number>".format(sys.argv[0]))

###############
### Logging ###
###############

log_filename = "log-server.txt"

def log(to_log):
    """ Write `to_log` to the log file, prefixed by a timestamp. """
    datetime_fmt = "%H:%M:%S %d/%m/%Y: "
def log_message(msg):
    """ Log a message (`msg`) received from the client. """