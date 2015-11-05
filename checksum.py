__author__ = 'PCPC'

import hashlib
import os
import sys

def sha256(filename , digest):
    f = open(filename,'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    print( digest==sh.hexdigest())
    f.close()
    return


def main():
    print(sys.argv[1])
    sha256(sys.argv[1],sys.argv[2])

main()