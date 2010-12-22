#!/usr/bin/env python

import sys
import hashlib
import os


def readfile(filename):             #define function to read a file
    f = open(filename)
    content = f.read()
    f.close()
    return content


def md5function(content):           #define function to generate md5 hash using hashlib module
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest() 


def main():                         #main function
    print "Running.."               #start the program
    md5index = {}                   #create an empty dictionary {key:value}
    output = open(r'./output.txt', 'w') #create a new output.txt to contain the generated md5 hashes

    for root, dirs, files in os.walk(sys.argv[1]):  #perform recursive file lookup
        for eachfile in files:                      #loop through the list of files
            filepath = os.path.join(root, eachfile) #join the root and the file name to form a filepath
            content = readfile(filepath)            #call the readfile function for filepath
            md5sum = md5function(content)           #call md5function to generate md5 hash
            md5index[filepath] = md5sum             #add a new entry into the md5index 
            
    for entry in md5index:          #for each entry in the md5index
        output.write(entry + "\t" + md5index[entry] + "\n") #write into the output.txt, with a tab spacing between filename and hash
                
    output.close()  #close the file
    print "Success!" + "\n" + "All filenames and their respective md5sums are indexed in output.txt"  #print success message when done



if __name__ == "__main__":
    main()
