#!/usr/bin/python

import sys
import getopt

def auntyUncle(inputNumber):
    '''
        Prints aunty if the inputNumber is divisible by 3 otherwise prints uncle

            Parameters:
                    inputNumber (int): A decimal integer
    '''
    if int(inputNumber) % 3 == 0:
        print "aunty"
    else:
        print "uncle"


#Do a basic sanity check to make sure an argument is supplied and it is made up of digits
if len(sys.argv) == 2 and sys.argv[1].isdigit():
    auntyUncle(sys.argv[1])

else:
    print "You must supply an argument that consists only of digits"
