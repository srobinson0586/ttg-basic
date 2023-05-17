""" List requested JQR signatures for all trainees

The intent is for reviewers to have local clones of all trainee's JQR repos,
stored in one root directory. The jqr-source repo (the repo containing this
file) should also be stored in the same root directory. The structure should
look something like this:

jqr
- janicki
  - [janicki's jqr contents]
- avila
  - [avila's jqr contents]
- craig
  - [craig's jqr contents]
- jqr-source
  - [the contents of this repo]

Then you should run this script from the jqr root directory:

$ ./jqr-source/review/find_signature_requests.py

This will use the list in `trainees.py` (in the same directory as this script)
to determine which trainee directories it should work in. For all the
trainees listed it will do a git pull in their directory and then look for
"?"s in their README.


You will need to make sure you're added to all the trainees' gitlab projects
and clone them before you can run this at all.
You should also do periodic pulls from this repo to keep your list of
trainees up-to-date.
"""

import os

import trainees

def git_pull(path):
    """ Perform a git pull in `path`. """

    orig_dir = os.getcwd()
    os.chdir(path)
    pull = os.popen("git pull")
    rtn = pull.read().strip()
    os.chdir(orig_dir)
    return rtn

def find_requested_sections(filename):
    """ Find sections requested for signoff in the given README. """

    sections = list()
    with open(filename, "r") as f:
        for line in f:
            if "?" in line:
                parts = line.split()
                assert parts[0] == "|"
                sections.append(parts[1])
    return sections

def main():
    """ Output all requested signatures for all active trainees. """
    indent = "    "

    for path in trainees.active:
        print("Working on {}:".format(path))
        if not os.path.isdir(path):
            print(indent + "!!! You're missing {}'s repo !!!\n".format(path))
            continue

        pull_output = git_pull(path)
        print(indent + pull_output)

        requested_sections = find_requested_sections(path + "/README.md")
        if requested_sections:
            print(indent + "Pending requests:")
            for sec in requested_sections:
                print(indent*2 + sec)
        else:
            print(indent + "No pending requests.")
        print()

if __name__ == "__main__":
    main()
