#!/usr/bin/env python
#
#syntax: $python insertmd5sumhere file/location/to/check/*.*

import sys
import hashlib
import os

def readfile(filename):
    f = open(filename)
    content = f.read()
    f.close()
    return content


def md5function(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()


def main():
    print "Running.."
    presetmd5 = sys.argv[1]
    foundflag = 0
    md5index = {}
    if len(presetmd5) != 32:
        print "Please enter a valid 32 byte md5sum."
        sys.exit(0)

    for root, dirs, files in os.walk(sys.argv[2]):
        for eachfile in files:
            filepath = os.path.join(root, eachfile)
            content = readfile(filepath)
            md5sum = md5function(content)
            md5index[filepath] = md5sum
            
    for entry in md5index:
        if md5index[entry] == presetmd5:
            print "File found! :D" + "\n" + "The md5sum, " + presetmd5 + ", belongs to the file: " + entry
            foundflag = 1
        
    if foundflag != 1:
        print "No matches to your md5sum :("


if __name__ == "__main__":
    main()
