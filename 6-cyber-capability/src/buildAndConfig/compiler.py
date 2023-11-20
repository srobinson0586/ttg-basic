#!/usr/bin/env python3
import datetime
import argparse
import csv
import subprocess
import sys
from time import sleep as sleep
import os
import http.server
import socketserver


# Use ParseArgs() to get commands from the command line
def parseCommands():
    # TODO
    pass

# Run a python script that starts a local http server in the /backdoor directory.
def start_server():
    # TODO
    pass


# Parse the commands for gcc. Outputs (valCommand, backCommand) for compilation of both exe's
def interpretCommands(args):

    # TODO
    pass

# Simple log implementation in the local logCompiler.csv file
def logCmd(msg):
    # TODO
    pass

# Checks if the CompleteInstance obj returned from subprocess.run() has any errors or output
def subProcessErrorCheck(subprocess, testName, exitOnStdOut=False,exitOnStdErr=False):
    # TODO
    pass

# ==============  MAIN ==============

args = parseCommands()
validatorCompile, backdoorCompile = interpretCommands(args)

# TODO: Compile it depending on the specified arguments
try:
    pass
except KeyboardInterrupt:
    if args.debug:print("Keyboard Interrupt.\n")
    