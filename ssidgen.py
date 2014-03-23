#!/usr/bin/env python

import sys
import argparse

print '+----------------------------------+'
print '|    ESSID Dictionary Generator    |'
print '+----------------------------------+'
print

parser = argparse.ArgumentParser()
parser.add_argument("-c","--company", help="The company name")
parser.add_argument("-f","--fai", help="A known FAI")
parser.add_argument("-o","--output", help="the output file")
args = parser.parse_args()

company = args.company
fai     = args.fai
output  = args.output

if fai and company:
    sys.exit("You cannot specifiy both -c and -f parameters")
