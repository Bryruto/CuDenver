#!/usr/bin/python3

import os
import stat
import sys

def myFind(directory, substring):
    directory = os.path.abspath(directory)
    matches = []
    total_size = 0

    #list directory and go down path total up bytes 
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        info = os.lstat(path)

        if substring in name:
            matches.append(path)

            if stat.S_ISREG(info.st_mode):
                print(f"{path}  {info.st_size:,} bytes")
                total_size += info.st_size
            else:
                print(path)

        if stat.S_ISDIR(info.st_mode):
            # search the subfolder using the same function.
            found, size = myFind(path, substring)
            matches.extend(found)
            total_size += size

    return matches, total_size

if __name__ =="__main__":
    files, total = myFind(sys.argv[1], sys.argv[2])
    print(f"\nTotal file size: {total:,} bytes")
