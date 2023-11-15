import sys
import struct
import datetime

# This should be the msg the client and server listen for to close connections
exit_msg = "exit"

##################################
### `send`/ `recv` Reliability ###
##################################

def recv_n(socket, n):
    """ Receive exactly `n` bytes of data from `socket`.

    Remember that calling `socket.recv(n)` is NOT guaranteed to receive all
    `n` bytes. It will return the number of bytes received, and you may
    have to call it repeatedly to get all the data.

    Return the bytes read from the socket, or None on error. """
    # TODO: Implement
    pass

def recv_msg(socket):
    """ Receive a single complete message on `socket`.

    Return the complete message (as a bytes string) or None on error. """
    # TODO: Implement
    pass

def send_msg(socket, msg):
    """ Send a complete string message (`msg`) on `socket`.

    Return True on success, False on error. """
    # TODO: Implement
    pass

##################
### Validation ###
##################

def validate_ip_port(ip_str, port_str):
    """ Return True if `ip_str` is a valid IPv6 IP and `port_str` is a valid port.
    Raise a ValueError otherwise, with an appropriate message.
    
    Use the Unix port range to determine `port_str` validity.
    Use library functions to determine the `ip_str` validity.
    """
    # TODO: Implement
    pass


def print_usage():
    """ Print out the command-line usage of client.py and server.py. """
    print("Usage: python3 {} <ipv6 address> <port number>".format(sys.argv[0]))

###############
### Logging ###
###############

log_filename = "log-server.txt"

def log(msg):
    """ Write `msg` to the log file, prefixed by a timestamp. """
    datetime_fmt = "%H:%M:%S %d/%m/%Y: "
    # TODO: Implement
    pass