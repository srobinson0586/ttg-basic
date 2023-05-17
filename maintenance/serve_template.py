""" Create and serve a tar file containing the JQR template

This script creates the JQR template that developer trainees complete at
N7. It does this in roughly 4 steps:

1. It recursively enumerates the contents of this template repo using
   `enumerate.py`.
   - It ignore files whose paths match patterns in `template-ignore.txt`
     (the ignoring functionality is contained in `ignorer.py`).

2. It excises out the solution material from all files, copying the
   remaining lines over to a new copy of the repo.
   - The excision functionality is in `excise.py`.

3. It then zips the copy into a `.tar.gz` file.

4. It then serves the tar file contents on TCP over port 4567.


Options:
- Adding `--dir` will make the script stop after step 2. This can be helpful
  for making sure the enumeration, ignoring, and excising is working as
  intended.

- Adding `--tar` will make the script stop after step 3. This can be useful
  in case you don't want to bother sending the tar file directly over the
  network (e.g., you could just create the tar file and send it over email
  or Slack).
"""

import os
import socket
import sys

from ignorer import Ignorer
from enumerator import recursive_enumerate
import exciser


def rmrf(directory):
    """ Entirely remove a directory. """
    for path in recursive_enumerate(directory, include_dirs = "after"):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)


if __name__ == "__main__":
    # Parse the given arguments.
    if len(sys.argv) > 1:
        if sys.argv[1] == "--dir":
            target = "dir"
        elif sys.argv[1] == "--tar":
            target = "tar"
        else:
            raise ValueError("Didn't understand target '{}'".format(sys.argv[1]))
    else:
        target = "all"


    # Global variables.
    port = 4567
    root_dir = ".."
    template_dir = "basic-jqr"
    ignore_file = "template-ignore.txt"

    tar_filename = template_dir + ".tar.gz"


    # Delete the template directory and tar.gz if they already exist.
    print("[+] Deleting previous template files . . .")
    if os.path.exists(template_dir):
        rmrf(template_dir)
    if os.path.exists(tar_filename):
        os.remove(tar_filename)
        print("[+] Done\n")


    # Get the latest changes from the remote.
    print("[+] Pulling from gitlab . . .")
    os.system("git pull")
    print("[+] Done\n")


    # Create the template directory.
    os.mkdir(template_dir)


    # Now iterate through the whole source directory performing excisisons,
    # ignoring appropriate files.
    print("[+] Performing recursive enumeration and excisions . . .")
    excise_ignorer = Ignorer(ignore_file, verbose = (target != "main"))
    for src_filename in recursive_enumerate("..", ignorer = excise_ignorer):
        # To form the destination filename, strip off the leading "../" and
        # add "basic-jqr/" instead.
        dst_filename = template_dir + os.sep + src_filename[len(root_dir) + 1:]

        # Now make sure that the required destination directories exist.
        dst_dir = dst_filename[:dst_filename.rindex(os.sep)]
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        exciser.excise(src_filename, dst_filename)
    print("[+] Done\n")


    # If our goal was just the directory, we're done.
    if target == "dir":
        print("Successfully created the template directory. Exiting.")
        exit()


    # Create the tar file and read its contents.
    print("[+] Creating the tar.gz file and reading its contents . . .")
    os.system("tar -czf {} {}".format(tar_filename, template_dir))
    with open(tar_filename, "rb") as f:
        tar_contents = f.read()
        print("[+] Done\n")


    # Remove the template directory.
    print("[+] Removing temporary directory . . .")
    rmrf(template_dir)
    print("[+] Done\n")


    # If our goal was just the tar file, we're done.
    if target == "tar":
        print("Successfully created the tar file. Exiting.")
        exit()


    # Remove the tar file.
    print("[+] Removing temporary directory and tar.gz . . .")
    os.remove(tar_filename)
    print("[+] Done\n")


    # Serve the tar.gz contents over the network.
    print("[+] Creating listening socket . . .")
    sock_listen = socket.socket()
    sock_listen.bind(("", port))
    sock_listen.listen()
    print("[+] Waiting for connection . . .")
    sock_talk, client_addr = sock_listen.accept()
    print("[+] Sending tar.gz contents . . .")
    sock_talk.sendall(tar_contents)
    sock_talk.close()
    sock_listen.close()
    print("[+] Finished with everything!")
