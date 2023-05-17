""" Recursively enumerate all directory contents """

import os

def recursive_enumerate(path, ignorer = None, include_dirs = False):
    """ Recursively enumerate items in a directory.

    You can optionally specify an Ignorer object to filter out
    directories and files.

    `include_dirs` can be either
    - False (only yield regular files)
    - "before" (yield directory paths before descending into them)
    - "after" (yield directory paths after descending into them) """

    include_dirs_options = {False, "before", "after"}
    if include_dirs not in include_dirs_options:
        error_message = "`include_dir` ({}) must be in {}"
        error_message = error_message.format(include_dirs,
                                             include_dirs_options)
        raise ValueError(error_message)

    # All items yielded are the `path` of some base case of this function.
    # Thus, they all go through this check.
    if ignorer is not None:
        if ignorer.check_ignore(path):
            return

    # Handle files.
    if not os.path.isdir(path):
        yield path

    # Handle directories.
    else:
        if include_dirs == "before":
            yield path

        for sub_item in os.listdir(path):
            full_sub_item_path = os.path.sep.join([path, sub_item])
            for sub_sub_item in recursive_enumerate(full_sub_item_path,
                                                    ignorer, include_dirs):
                yield sub_sub_item

        if include_dirs == "after":
            yield path


if __name__ == "__main__":
    import ignorer

    for path in recursive_enumerate("..", ignorer.Ignorer("template-ignore.txt")):
        print(path)
