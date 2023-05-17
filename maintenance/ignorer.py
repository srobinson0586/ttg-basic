""" Filter out files based on their name """

import re
import os

class Ignorer:
    """ A class to simulate gitignore functionality """

    def __init__(self, filename, verbose = False):
        """ Initialize an Ignorer from a file. """

        self.verbose = verbose

        with open(filename, "r") as f:
            self.regexs = list()
            for line in f:
                if line and not line.startswith("#"):
                    line = line.strip()
                    # We want `*` to represent arbitrary text, but in Python
                    # RE format, `*` represents arbitrary repitition of the
                    # previous expression.
                    pattern = line.replace("*", ".*")
                    # `$` forces the pattern to match against the end of a word;
                    # otherwise there can be arbitrary characters after the match
                    # and it will still succeed.
                    pattern += "$"
                    self.regexs.append(re.compile(pattern))

    def check_ignore(self, path):
        """ Determine if `path` matches a pattern from the ignore file

        Returns True if the path should be ignored, False otherwise. """
        matched = False
        for regex in self.regexs:
            short_name = path.split(os.sep)[-1]
            # Check against the full path we were given and the short name.
            if (regex.match(path) is not None or
                regex.match(short_name) is not None):
                matched = True
                if self.verbose:
                    print("Ignoring", path)
                break

        return matched
