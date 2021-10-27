#
# File Recursion
#

import os 

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []

    if not os.path.isdir(path):
        if path.endswith(suffix):
            return [path]
        return []

    sub_paths = [ os.path.join(path, _sub_path) for _sub_path in os.listdir(path) ]
    for item in sub_paths:
        if os.path.isfile(item):
            if item.endswith(suffix):
                paths.append(item)
        else:
            paths += find_files(suffix, item)

    return paths


if __name__ == '__main__':
    path = 'testdir'
    suffix = '.c'

    paths = find_files(suffix, path)
    print(paths)