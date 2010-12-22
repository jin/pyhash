#!/usr/bin/env python
#
#syntax: $python insertmd5sumhere file/location/to/check/

import sys
import hashlib
import os

def readfile(filename):         #define function to read a file
    f = open(filename)
    content = f.read()
    f.close()
    return content


def md5function(content):       #define function to generate md5 hash using hashlib module
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()


def main():                     #main function
    print "Running.."           #start the program
    presetmd5 = sys.argv[1]     #get the md5 hash that the user wants to compare with
    foundflag = 0               #a flag to signal whether a match has been found. 0 = not found
    md5index = {}               #create an empty dictionary {key:value}
    if len(presetmd5) != 32:    #check if md5sum user provided is of correct length
        print "Please enter a valid 32 byte md5sum."    #error message
        sys.exit(0)                                     #exit from program

    for root, dirs, files in os.walk(sys.argv[2]):      #perform recursive file lookup
        for eachfile in files:                          #loop through the list of files
            filepath = os.path.join(root, eachfile)     #join the root and the file name to form a filepath
            content = readfile(filepath)                #call the readfile function for filepath
            md5sum = md5function(content)               #call md5function to generate md5hash
            md5index[filepath] = md5sum                 #add a new entry into md5index
            
    for entry in md5index:                              #for each entry in md5index
        if md5index[entry] == presetmd5:                #compare with the user provided md5 hash
            print "File found! :D" + "\n" + "The md5sum, " + presetmd5 + ", belongs to the file: " + entry  #if found, print success message
            foundflag = 1   #set foundflag to 1
        
    if foundflag != 1: #if after searching and the foundflag remains as 0
        print "No matches to your md5sum :("    #print failure message


if __name__ == "__main__":
    main()
