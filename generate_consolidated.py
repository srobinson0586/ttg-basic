#!/usr/bin/python3
import sys
import os
import shutil
import datetime

if (len(sys.argv) > 1):
    print("python3 generate_consolidated.py")
    print("----------------------------")
    print("Generates a single Markdown file representing the JQR repo.")
    print("Inlcudes:")
    print("- Markdown Files")
    print("- Python Files (*.py)")
    print("- C Files (*.c, *.h)")
    print("- C++ Files (*.cpp)")
    print("- Assembly Files (*.asm, *.nasm)")
    print("- Makefiles (Makefile)")
    print("- Text Files (*.txt)")
    exit()

def file_contents(path):
    #print(path)
    with open(path, "r") as f:
        contents = f.read()
    return contents

def add_directory_to_md(path, mdf):
    files = os.listdir(path)

    files.sort()

    ### Copy over all the markdown files first.
    for name in files:
        if ".md" in name:
            full_path = path + "/" + name
            if mdf.tell() > 0:
                mdf.write("\n\n\n")
            mdf.write("# " + full_path + "\n\n")
            mdf.write(file_contents(full_path))

    ### Copy over other files that we care about.
    for name in files:
        if name in ignore:
            continue
        
        full_path = path + "/" + name
        for ex in extensions:
            if name.endswith(ex):
                mdf.write("\n\n\n# " + full_path + "\n\n")
                mdf.write("```" + extensions[ex] + "\n")
                mdf.write(file_contents(full_path))
                mdf.write("\n```\n")
                continue
            
        if ".PNG" in name:
            shutil.copyfile(full_path, target_dir + "/" + name)

    ### Descend into all directories that we care about.
    dirs = [d for d in files if os.path.isdir(path + os.path.sep + d)]
    for sub_dir in dirs:
        if not sub_dir in ignore:
            add_directory_to_md(path + "/" + sub_dir, mdf)

if __name__ == "__main__":
    ### Compute the name of the directory we'll put the consolidated file in.
    target_dir = "consolidated"
    
    ### Compute the name of the consolidated file.
    md_filename = "basic-jqr-consolidated-" + str(datetime.date.today()) + ".md"
    md_path_rel = target_dir + os.path.sep + md_filename

    print("Consolidating JQR into:   {}".format(md_path_rel))
    
    extensions = {".h": "c", ".c": "c", ".cpp": "cpp",
                  ".asm": "assembly", ".nasm": "assembly",
                  ".txt": "text", ".py": "python", "Makefile": "make"}
    
    this_file_name_abs = __file__
    this_file_name_rel = this_file_name_abs[this_file_name_abs.rindex(os.path.sep) + 1:]
    
    ignore = {".git", "XtraComps", "styles", "__pycache__", target_dir,
              "words.txt", this_file_name_rel}

    ### Create the target directory, if it doesn't already exist.
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    ### Generate the consolidated file.
    with open(md_path_rel, "w") as mdf:
        add_directory_to_md(".", mdf)

    print("Done!")
