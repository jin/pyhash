#!/usr/bin/env python

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
    md5index = {}
    output = open(r'./output.txt', 'w')

    for root, dirs, files in os.walk(sys.argv[1]):
        for eachfile in files:
            filepath = os.path.join(root, eachfile)
            content = readfile(filepath)
            md5sum = md5function(content)
            md5index[filepath] = md5sum
            
    for entry in md5index:
        output.write(entry + "\t" + md5index[entry] + "\n")
                
    output.close()
    print "Success!" + "\n" "All filenames and their respective md5sums are indexed in output.txt"



if __name__ == "__main__":
    main()
