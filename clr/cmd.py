#!/usr/bin/env python
import argparse, serial

ser = serial.Serial('/dev/clr', 115200)


parser = argparse.ArgumentParser(description='Turn a light on.')

parser.add_argument("-m", "--mode", help='Effect when changing', default='0' )

parser.add_argument("-r", "--red", help='Red', 
        default='255' )

parser.add_argument("-g", "--green", help='Green', default='255')

parser.add_argument("-b", "--blue", help='Blue', default='255')

parser.add_argument("-d", "--delay", help='Delay', default='0')

args = parser.parse_args()

brk = "/"
cmd = args.mode + brk + args.red + brk + args.green + brk + args.blue + brk + args.delay + brk


if(ser.is_open == False):
    while(ser.is_open == False):
        if(ser.is_open == True):
            ser.write(cmd.encode())
            break
elif(ser.is_open == True):
    ser.write(cmd.encode())
