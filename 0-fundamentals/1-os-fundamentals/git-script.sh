#!/bin/bash
# Clean up all the effects of this script if the user passes "--clean".
if [ $1 = "--clean" ]
then
    rm -f Readme.txt patch.py feature.py
    rm -rf .git
    exit 0
fi

# Initialize a new repository.
# (This creates a `.git` directory in the current directory).
# This will not affect your JQR repo in any way!
# You can remove all effects of this script by running
# `rm -rf .git` (in the current directory!) afterwards.
git init

# Create a Readme with some contents.
echo This is a fake project to learn git. > Readme.txt

# TODO: Add `Readme.txt` to your new git repo and then make a commit
# with a descriptive message.

# TODO: Create a new branch called `bug-fix-1337` and check it out.

# Create `patch.py`.
echo This file will somehow patch a bug! > patch.py

# TODO: Add `patch.py` and make a commit on the new branch.

# TODO: Switch back to the main branch.

# Create `feature.py`.
echo This is a cool new feature! > feature.py

# TODO: Add `feature.py` and make a new commit on the main branch.

# TODO: Merge the `bug-fix-1337` branch into the main branch.
