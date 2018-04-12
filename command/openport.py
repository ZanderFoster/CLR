#!/usr/bin/env python
import serial
# importing required modules
import argparse
 
# create a parser object
parser = argparse.ArgumentParser(description = "Computer Light Reaction || Made By: Zander Foster")
 
  parser.add_argument("-r", "--read", type = str, nargs = 1,
                        metavar = "file_name", default = None,
                        help = "Opens and reads the specified text file.")





# parse the arguments from standard input
args = parser.parse_args()

print(args.mode)
print(args.rgb)














