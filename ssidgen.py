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
parser.add_argument("-l","--length", help="use this option in combination with --fai", default=2)
args = parser.parse_args()

company = args.company
fai     = args.fai
output  = args.output
length  = args.length

if fai and company:
    sys.exit("You cannot specifiy both -c and -f parameters")
elif not fai and not company:
    parser.print_help()
    sys.exit()

def bruteforcize(string):
    return [string, string.upper(), string[0].upper()+string[1:]]

dictionnary = open(output + '.txt' if output else 'ssid.txt', "w")


if fai:
    for i in range(pow(2,8*int(length))):
        dictionnary.write(fai + '_%04x\n' % i)
        dictionnary.write(fai + '_%04X\n' % i)
        dictionnary.write(fai + '-%04x\n' % i)
        dictionnary.write(fai + '-%04X\n' % i)

if company:
    prefix = 'wifi'
    map(lambda x: dictionnary.write(x+"\n"),[ "%s%s%s" % (x,y,z) for x in bruteforcize(prefix) for y in ["-","_"] for z in bruteforcize(company)])
    map(lambda x: dictionnary.write(x+"\n"),[ "%s%s%s" % (z,y,x) for x in bruteforcize(prefix) for y in ["-","_"] for z in bruteforcize(company)])

dictionnary.close
print 'An SSID list for '+ (company if company else fai) + ' was generated in ' + (output if output else 'ssid.txt')
