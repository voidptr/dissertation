#!/usr/bin/python

###################
# Analyze
###################

# system includes
#import glob
import os
from optparse import OptionParser
import sys
import re

# Set up options
usage = """usage: %prog [options] infile.tex
"""

parser = OptionParser(usage)
parser.add_option("-v", "--verbose", action = "store_true", dest = "verbose",
                  default = False, help = "print extra messages to stdout")
parser.add_option("-d", "--debug_messages", action = "store_true", dest = "debug_messages",
                  default = False, help = "print debug messages to stdout")

## fetch the args
(options, args) = parser.parse_args()

## parameter errors
if len(args) < 1:
    parser.error("incorrect number of arguments")


infile = args[0]

fp = open(infile)

outline = [("", "", "")]

level = None
for line in fp:
    #print "hi"
    level = None
    prepend = ""
    if "\\subsubsection" in line:
        level = 2
    if "\\subsection" in line:
        level = 1
    if "\\section" in line:
        level = 0

    if level != None:
        m = re.search('{(.+?)}', line)
        if m:
            val = "".ljust(level * 2, " ")
            if level != None:
                prepend = "\n"

            outline.append( (val, prepend, m.group(1)) )
    elif "%=" in line:
        m = re.search('%=(.+?)$', line)
        if m:
            outline.append( (outline[-1][0], "", "  -"+m.group(1))) #

for bit in outline:
    print bit[1]+bit[0]+bit[2]
