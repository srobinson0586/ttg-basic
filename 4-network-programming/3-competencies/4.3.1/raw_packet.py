import os
import socket
import struct


def verify_root():
    """ Verify that we are running as root. """
    if os.geteuid() != 0:
        raise ValueError("You must run this script as root!")

def make_raw_socket(interface = "lo"):
    """ Make a socket that can send and receive raw ethernet packets.

    It is bound to the interface given (by default, loopback). """
    protocol = socket.htons(3)
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, protocol)
    sock.bind((interface, 0))
    return sock

verify_root()


# TODO: Craft a raw packet (using the RFCs as a reference) that could be
# part of a TCP connection. Use the following information, and fill in the
# unspecified fields with whatever data is appropriate (some fields may not
# really matter, others may be critical).
#
#   ethernet:
#     dst-mac: c0:ff:33:c0:0c:13
#     src-mac: 12:34:56:78:90:ab
#
#   ipv4:
#     src-ip: 10.20.30.40
#     dst-ip: 50.60.70.80
#
#   tcp:
#     src-port: 1337
#     dst-port: 4567
#     seq-num: 1234567
#     ack-num: 9876543
#     push and fin flags set
#     data: "Hello, world!"
#
# Note: Do not append an ethernet CRC checksum. That is taken care of by
# the kernel.


# Create a socket that can send raw packets on the loopback interface.
sock = make_raw_socket("eth0")

# TODO: Send your packet over `sock`.

# TODO: Close the raw socket.

# TODO: Take a screenshot of the Wireshark parse of your packet and commit
# it so the training staff can verify that all the fields are correct.
