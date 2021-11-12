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

    # paths = find_files(suffix, path)
    # print(paths)
    # treee testdir
    # ├── subdir1
    # │   ├── a.c
    # │   └── a.h
    # ├── subdir2
    # ├── subdir3
    # │   └── subsubdir1
    # │       ├── b.c
    # │       └── b.h
    # ├── subdir4
    # ├── subdir5
    # │   ├── a.c
    # │   └── a.h
    # ├── t1.c
    # └── t1.h

    print(f"\nTest0: find_files('.c','testdir')")
    # ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']
    print(find_files('.c','testdir'))

    print(f"\nTest1: find_files('.c','testdir/subdir5/subsub51')")
    # ['testdir/subdir5/subsub51/a51.c']
    print(find_files('.c','testdir/subdir5/subsub51'))

    print(f"\nTest2: find_files('.c','testdir/subdir4')")
    # []
    print(find_files('.c','testdir/subdir4'))

    print(f"\nTest3: find_files('.c','testdir/subdir432')")
    # []
    print(find_files('.c','testdir/subdir432'))

    print(f"\nTest4: find_files('.c','testdir/subdir5/nodir')")
    # []
    print(find_files('.c','testdir/subdir5/nodir'))

    print(f"\nTest5: find_files('.c','testdir/subdir5')")
    # ['testdir/subdir5/a.c','testdir/subdir5/subsub51/a51.c']
    print(find_files('.c','testdir/subdir5'))