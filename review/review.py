""" A tool to help review trainees' JQR signature requests """

import sys
import os
import datetime

from find_signature_requests import find_requested_sections

def get_signers_config_option(option, required = True):
    """ Read an option from the signers_config.py file. """

    try:
        import signers_config
    except ModuleNotFoundError:
        raise ModuleNotFoundError("Please configure your signer's options "
                                  + "in `review/signers_config.py`")

    if not hasattr(signers_config, option):
        rtn = None
    else:
        rtn = getattr(signers_config, option)

    if rtn is None and required:
        raise ValueError("Please configure option `{}`".format(option),
                         + " in signers_config.py")

    return rtn


def find_section_path(trainee, section):
    """ Find the most specific path to this section.

    If the section has its own directory, this is the path to that
    directory. Otherwise, the section should have its own file, and this
    will return the path to that file. """

    for path in os.listdir(trainee):
        if path.startswith("{}_".format(section.split(".")[0])):
            section_dir = os.sep.join([trainee, path])
            break

    for path in os.listdir(section_dir):
        if path.startswith("{}_".format(section[:section.rindex(".")])):
            section_dir = os.sep.join([section_dir, path])

    rtn = None
    if section in os.listdir(section_dir):
        rtn = os.sep.join([section_dir, section])
    else:
        for filename in os.listdir(section_dir):
            if filename.startswith(section):
                rtn = os.sep.join([section_dir, filename])
                return rtn

    if rtn is None:
        raise ValueError("Could not find section path for", section)
    return rtn

def open_review_shell(path, trainee, section):
    """ Open an interactive shell in the section's directory. """

    default_bashrc = os.path.expanduser("~/.bashrc")
    temp_bashrc_filename = ".bashrc-temp"

    with open(default_bashrc, "r") as f:
        contents = f.read()

    with open(temp_bashrc_filename, "w") as f:
        f.write(contents)
        f.write("\nPS1=(reviewing {} {}) $PS1\n".format(trainee, section))

    orig_dir = os.getcwd()
    os.chdir(path)
    os.system("/bin/bash --init-file {}".format(temp_bashrc_filename))
    os.chdir(orig_dir)

    os.remove(temp_bashrc_filename)

def open_editor(path):
    """ Open up a file in an interactive editor.

    This requires an editor to be selected in signers_config.py. """

    editor = get_signers_config_option("editor")
    os.system("{} {}".format(editor, path))

def diff_files(path1, path2):
    """ Display a diff of 2 files. """

    os.system("vim -d {} {}".format(path1, path2))

def classify_files(files):
    """ Classify files (code/image/markdown/other) by extension.

    Returns a dictionary. """

    rtn = {"code_files": set(),
           "markdowns": set(),
           "images": set(),
           "other": set()}

    for filename in files:
        if filename.lower().endswith(".md"):
            rtn["markdowns"].add(filename)
        elif (filename.lower().endswith(".png") or
              filename.lower().endswith(".jpg")):
            rtn["images"].add(filename)
        elif (filename.lower().endswith(".py") or
              filename.lower().endswith(".c") or
              filename.lower().endswith(".h") or
              filename.lower().endswith("asm") or
              filename.lower() == "makefile"):
            rtn["code_files"].add(filename)
        else:
            rtn["other"].add(filename)

    return rtn

def copy_file(dst_filename, src_filename):
    """ Copy all contents from `src_filename` to `dst_filename`. """

    with open(dst_filename, "wb") as dst:
        with open(src_filename, "rb") as src:
            while True:
                chunk = src.read(1024)
                if not chunk:
                    break
                dst.write(chunk)

def copy_files(dst_dir, src_dir, filenames):
    """ Copy the given files from `src_dir` to `dst_dir`.

    This raises a ValueError if `dst_dir` does not exist.
    It also skips files that already exist in `dst_dir`. """
    if not os.path.isdir(dst_dir):
        msg = "Destination '{}' doesn't exist!".format(dst_dir)
        raise ValueError(msg)

    already_there = os.listdir(dst_dir)
    for filename in filenames:
        if filename not in already_there:
            copy_file(os.path.sep.join([dst_dir,
                                        filename]),
                      os.path.sep.join([src_dir,
                                        filename]))

def review_section(path, trainee, section):
    """ Review a specific section. """

    if os.path.isdir(path):
        files = os.listdir(path)
        groups = classify_files(files)

        # If `image_dir` has been configured, copy over all the image
        # files to a convenient directory.
        if groups["images"]:
            image_dir = get_signers_config_option("image_dir")
            if image_dir is not None:
                copy_files(image_dir, path, groups["images"])

        # If there's a single markdown all by itself, just open it.
        if (not groups["code_files"] and
            not groups["other"] and
            len(groups["markdowns"]) == 1):
            # Open up the markdown.
            (markdown_filename,) = groups["markdowns"]
            open_editor(os.path.sep.join([path, markdown_filename]))

        # Otherwise, pop open a shell.
        else:
            open_review_shell(path, trainee, section)

    # If the whole section is just a markdown file (i.e., without its
    # own directory), just open the markdown.
    else:
        open_editor(path)

def edit_readme_section(trainee, section, action):
    """ Edit the README line for a specific section.

    `action` can be "sign", "kickback", or "skip".
    This requires initials to be configured in signers_config.py """

    participle_dict = {"sign": "Signing",
                       "skip": "Skipping",
                       "kickback": "Kicking back"}
    print(participle_dict[action], section)

    if action == "skip":
        return

    initials_column_width = 10
    date_str = datetime.datetime.today().strftime("%d%b%Y").upper()
    readme_filename = "{}/README.md".format(trainee)

    with open(readme_filename, "r") as f:
        readme_lines = f.readlines()

    found_section = False
    with open(readme_filename, "w") as f:
        for line in readme_lines:
            if section in line.split():
                found_section = True

                pieces = line.split("|")
                assert len(pieces) == 6
                assert "?" in pieces[3]
                assert not pieces[4].strip()

                if action == "sign":
                    # Sign and date.
                    pieces[3] = " {}".format(get_signers_config_option("initials"))
                    pieces[3] += " " * (initials_column_width - len(pieces[3]))

                    pieces[4] = " {} ".format(date_str)

                elif action == "kickback":
                    # Get rid of the question mark.
                    pieces[3] = " " * initials_column_width
                else:
                    raise ValueError("action '{}' not understood".format(action))


                line = "|".join(pieces)

            f.write(line)

    if not found_section:
        raise ValueError("Could not find section '{}'".format(section))

def get_action_for_readme(trainee, section):
    """ Get the signer's requested action for the README. """

    action_dict = {"y": "sign", "k": "kickback", "": "skip"}

    verdict = None
    while verdict not in action_dict:
        if verdict is not None:
            print("Please enter y (sign), k (kick back), or nothing (skip)")

        verdict = input("Action for {} section {}? (y/k/) ".format(trainee,
                                                                   section))
        verdict = verdict.strip().lower()

    return action_dict[verdict]


if __name__ == "__main__":
    trainee = sys.argv[1]
    print("Reviewing {}".format(trainee))

    to_review = find_requested_sections("{}/README.md".format(trainee))

    for section in to_review:
        path = find_section_path(trainee, section)

        review_section(path, trainee, section)

        action = get_action_for_readme(trainee, section)
        edit_readme_section(trainee, section, action)

    print()
