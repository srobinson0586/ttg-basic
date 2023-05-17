""" Automatically generate a JQR README file

This script enumerates all the contents of .. and then takes the header
from each README file and treats it as the line-item description.

Then it formats the line items with their descriptions into a big table
that could be used in the README markdown.

It's intended to be useful even if you're not using it actually to generate
a README file.
1. It will warn you if there's a missing line-item in a section (e.g.,
   if there are section 1.2.3 and 1.2.5 but no 1.2.4).

2. You can have it generate a table and then copy and paste a part of that
   table into the actual README file.
"""

import os

def get_section_description_from_markdown(filename):
    """ Get the line-item description from a markdown file.

    This is the contents of the first line, after the initial "# ". """

    with open(filename, "r") as f:
        first_line = f.readline().strip()
        description = first_line.removeprefix("# ")

    return description

def get_subsection_markdowns(directory):
    """ Collect all item markdowns for a JQR subsection. """
    items = []
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path) and item.count(".") == 2:
            md_path = os.path.join(path, item + ".md")
            assert os.path.exists(md_path)
            items.append(md_path)
        if item.count(".") == 3 and item.endswith(".md"):
            items.append(path)
    return items

def get_section_tuple(filename):
    """ Get a tuple of the section numbers from `filename`. """
    base_filename = os.path.basename(filename)
    return tuple(int(x) for x in base_filename.split(".")[:-1])

def format_table_line(section, description, initials, date, fillchar = " "):
    section_width = 8
    description_width = 80
    initials_width = 7
    date_width = 11

    fields = [section, description, initials, date]
    field_widths = [section_width, description_width, initials_width,
                    date_width]

    fields = [fillchar + (f + fillchar).ljust(f_w - 1, fillchar)
              for f, f_w in zip(fields, field_widths)]

    sep = "|"
    line = sep.join(fields)
    line = sep + line + sep + "\n"
    return line

def get_section_idx_and_name(dirname):
    i = 0
    while dirname[i].isdigit():
        i += 1

    if i:
        section_idx = int(dirname[:i])
        section_name = dirname[i:]
        section_name = section_name.replace("-", " ")
        section_name = section_name.strip()
        section_name = section_name.title()
        rtn = (section_idx, section_name)
    else:
        rtn = (None, None)
    return rtn


class Section:
    level_map = ["section", "subsection", "item"]

    def __init__(self, name, idx, path, level):
        self.name = name
        self.idx = idx
        self.path = path
        self.level = level

    def __str__(self):
        return f"{self.level_map[self.level]} {self.name} @ {self.path} ({self.idx})"

    def __lt__(self, other):
        assert self.level == other.level
        return self.idx < other.idx

    def get_contents(self):
        if self.level == 0 and self.idx > 5:
            self.contents = []
            print("Skipping", self)
            return

        if self.level == 0:
            # Collect all the subsections in our directory.
            self.contents = find_sections(self.path, self.level + 1)

        elif self.level == 1:
            # Collect all the items that live under our directory.
            md_paths = get_subsection_markdowns(self.path)
            self.contents = []
            for md_path in md_paths:
                item_tuple = get_section_tuple(md_path)
                item_name = ".".join([str(x) for x in item_tuple])
                s = Section(item_name, item_tuple[2], md_path, self.level + 1)
                self.contents.append(s)

            self.contents.sort()

        elif self.level == 2:
            # Get the description from the markdown file.
            self.description = get_section_description_from_markdown(self.path)

        if self.level < 2:
            if not self.contents:
                print("\tEmpty section:", self)

            indices = [s.idx for s in self.contents]
            for i in range(min(indices), max(indices) + 1):
                if i not in indices:
                    print(f"\tMaybe missing item {i} under {self}?")

            for s in self.contents:
                s.get_contents()

    def generate_readme_text(self):
        if self.level == 0:
            text = f"## {self.idx}: {self.name}\n"
            text += format_table_line("Sec.", "Requirement", "Init.", "Date")
            text += format_table_line("", "", "", "", fillchar = "-")

            for s in self.contents:
                text += s.generate_readme_text()

        elif self.level == 1:
            text = f"| {self.name}\n"
            for s in self.contents:
                text += s.generate_readme_text()

        elif self.level == 2:
            text = format_table_line(self.name, self.description, "", "")

        return text

def find_sections(directory, level):
    sections = []
    for path in os.listdir(directory):
        idx, name = get_section_idx_and_name(path)
        if idx is not None:
            section_path = os.path.join(directory, path)
            s = Section(name, idx, section_path, level)
            sections.append(s)

    return sorted(sections)


if __name__ == "__main__":
    sections = find_sections("..", 0)

    readme_table = ""

    for s in sections:
        s.get_contents()
        readme_table += s.generate_readme_text() + "\n"

    with open("readme-template.md", "r") as src:
        template = src.read()

    readme_contents = template.replace("SIGTABLE", readme_table)

    with open("README.md~", "w") as dst:
        dst.write(readme_contents)
