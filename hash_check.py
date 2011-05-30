#!/usr/bin/env python
#coding=utf-8
import sys, hashlib
def usage():
    print """
    usage: hash_check.py <file> <hash type> <original_hash> \n\n

    1 = MD5 \n
    2 = SHA1 \n\

    """

def get_hash(file, type):
    print type
    file = open(file,"rb")

    if type == "md5":
        h = hashlib.md5()
        h.update(file.read())
        hash = h.hexdigest()
        file.close()
        return hash


    if type == "sha1":
        h = hashlib.sha1()
        h.update(file.read())
        hash = h.hexdigest()
        file.close()
        return hash


def main():
    if len(sys.argv) < 3:
        usage()
    else:

        global hash
        file = sys.argv[1]
        type = sys.argv[2]
        ohash = sys.argv[3]

        if type == "1":
            hash = get_hash(file,"md5")
        elif type == "2":
            hash = get_hash(file,"sha1")
        else:
            print "Invalid hash type"

        if ohash == hash:
            print "\n\n\n"
            print "Original:", ohash , "\n"
            print "Digest:  ", hash, "\n"
            print "*~" * 5
            print "* Valid *"
            print "*~" * 5
        else:
            print "\n\n\n"
            print "Original:", ohash , "\n"
            print "Digest:  ", hash, "\n"
            print "¿" * 5
            print "invalid"
            print "¿" * 5


if __name__ == "__main__":
    main()


