""" Manage the reference links in the JQR

Right now, the main purpose of this script is to verify that the embedded
links aren't dead.
"""

import os
import urllib.request
import http

from functools import total_ordering

@total_ordering
class Reference:
    def __init__(self, section, name, url):
        self.section = section
        self.name = name
        self.url = url

    def __str__(self):
        return "{}: [{}]({})".format(self.section, self.name, self.url)

    def __eq__(self, r):
        rtn = False
        if self.section == r.section:
            rtn = True
        return rtn

    def __lt__(self, r):
        rtn = False
        self_secs = [int(n) for n in self.section.split(".")]
        r_secs = [int(n) for n in r.section.split(".")]

        rtn = False
        for s_sec, r_sec in zip(self_secs, r_secs):
            if s_sec < r_sec:
                rtn = True
                break
            elif s_sec > r_sec:
                break

        return rtn

    def check(self, verbose = False):
        live = True
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            req = urllib.request.Request(self.url, headers = headers)
            response = urllib.request.urlopen(req, timeout = 2)
            assert isinstance(response, http.client.HTTPResponse)

        except urllib.error.URLError as e:
            r.error = e
            live = False
            print(e)

        except AssertionError:
            r.error = e
            print("Unexpected assert error:")
            print(e)
            live = False

        except Exception as e:
            r.error = e
            print("Unexpected error:")
            print(e)
            live = False

        return live

def parse_ref_line(line):
    if "[" not in line:
        return None

    p1, p2 = line.split("[")

    if "]" not in p2:
        print("Failed to find ']' in {}".format(line))
        return None

    ref_name, p3 = p2.split("]")

    if "(" not in p3:
        return None
    p4, p5 = p3.split("(")[:2]
    if ")" not in p5:
        return None

    ref_url, p6 = p5.split(")")

    # Find the section the reference is associated with, so we can sort
    # them nicely.
    a = p1.rindex("/")
    b = p1.rindex(".")
    ref_section = p1[a + 1: b]
    if not ref_section.count(".") == 2:
        # This must be markdown that isn't named with the section.
        # But, the section should be the directory name.
        dir_path = p1[:a]
        ref_section = dir_path[dir_path.rindex("/") + 1:]

    return Reference(ref_section, ref_name, ref_url)

def get_refs():
    ref_filename = "refs.txt"
    os.system('grep --include "*.md" -r -A 20 "\<Reference" .. > {}'.format(ref_filename))
    with open(ref_filename, "r") as f:
        lines = f.readlines()
    os.remove(ref_filename)

    refs = []
    for ref_line in lines:
        r = parse_ref_line(ref_line)
        if r is not None:
            refs.append(r)

    return sorted(refs)

if __name__ == "__main__":
    ref_list = get_refs()

    live = []
    broken = []
    for r in ref_list:
        if not r.check():
            print("broken: {}".format(r))
            broken.append(r)

        else:
            print("live: {}".format(r))
            live.append(r)

    with open("refs.md", "w") as f:
        f.write("# JQR Link Summary\n\n")

        f.write("## Live:\n\n")
        for r in live:
            f.write("{}\n\n".format(r))

        f.write("\n\n## Broken:\n")
        for r in broken:
            f.write("{}\n\n".format(r))
            f.write("- {}\n\n".format(r.error))
