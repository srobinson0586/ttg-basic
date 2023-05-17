""" Strip solution lines out of JQR template files

When run as a script with 1 filename argument, it displays the file
contents with the material to be excised in red. With 2 arguments, it
actually performs the excise and copy from the first file to the second. """

import os
import sys

comment_dict = {".py": "#",
                ".c": "//",
                ".h": "//",
                ".cpp": "//",
                ".asm": ";",
                ".nasm": ";",
                ".sh": "#",
                "txt": "#",
                ".md": "$$",
                ".json": "#",
                ".gitignore": "#"}

raw_extensions = {".png", ".pdf",
                  ".exe", ".pdb",
                  ".sln", ".vcxproj"}

def print_red(line):
    """ Print `line` in red """
    print("\033[91m{}\033[00m".format(line), end="")


def excise_text_file(src, dst, comment_mark, debug = False):
    """ Excise solutions out of a text file

    The comment symbol is determined from the file extension and
    `comment_dict`.
    """

    excise_start = "excise-start"
    excise_end = "excise-end"
    copying = True

    for line_num_minus_one, line in enumerate(src):
        if excise_start in line[line.find(comment_mark):]:
            if copying:
                copying = False
            else:
                msg = "Hit excise-start while not copying in {}, line {}!"
                msg = msg.format(src.name, line_num_minus_one + 1)
                raise ValueError(msg)

        if copying:
            dst.write(line)
            if debug:
                print(line, end="")

        elif debug:
            print_red(line)

        if excise_end in line[line.find(comment_mark):]:
            if not copying:
                copying = True
            else:
                msg = "Hit excise-end while copying in {}, line {}!"
                msg = msg.format(src.name, line_num_minus_one + 1)
                raise ValueError(msg)

def excise_raw_file(src, dst):
    """ Excise solutions out of a raw data file

    This will probably always be just a copy. """
    dst.write(src.read())

def excise(src_filename, dst_filename, debug = False):
    """ Copy over a file, excising solutions as appropriate

    If the file is a text file, we hand it to `excise_text_file`.
    If it contains raw binary data, we hand it to `excise_raw_file`. """
    text = None

    # Look for known raw file extensions. These files need no excising.
    for extension in raw_extensions:
        if src_filename.lower().endswith(extension):
            text = False
            break

    # Look for standard text file extensions.
    for extension, comment_mark in comment_dict.items():
        if src_filename.endswith(extension):
            text = True
            break

    # Handle file names with no period.
    short_filename = src_filename.split(os.sep)[-1]
    if "." not in short_filename:
        if short_filename.lower() == "makefile":
            text = True
            comment_mark = "#"

        else:
            # This is hopefully an ELF file.
            with open(src_filename, "rb") as f:
                magic = f.read(4)
            if magic == b"\x7fELF":
                text = False
                #msg = "Plain file {} that's not a Makfile or an ELF file!"
                #msg = msg.format(src_filename)
                #raise ValueError(msg)

    if text is None:
        # We didn't know how to handle this file. We'll read the contents to
        # check for non-ASCII characters.
        #raise ValueError("Unknown file extension: {}".format(src_filename))
        with open(src_filename, "rb") as f:
            contents = f.read()
        try:
            contents.decode("utf-8")
            text = True
            comment_marker = "#"
        except UnicodeError:
            text = False
        print("Exciser doesn't know how to handle", src_filename)
        print("Interpreting it as " + ("text." if text else "raw."))

    # Determine the mode to use when we open the files.
    if text:
        mode_suffix = ""
    else:
        mode_suffix = "b"

    # Open the files and perform the excision.
    with open(src_filename, "r" + mode_suffix) as src:
        with open(dst_filename, "w" + mode_suffix) as dst:
            if text:
                excise_text_file(src, dst, comment_mark, debug)
            else:
                excise_raw_file(src, dst)

if __name__ == "__main__":
    src_filename = sys.argv[1]
    if len(sys.argv) == 3:
        dst_filename = sys.argv[2]
        debug = False
    else:
        dst_filename = "/dev/null"
        debug = True
    excise(src_filename, dst_filename, debug)
