#!/usr/bin/env python
import argparse, serial, time
 
ser = serial.Serial('/dev/clr', 115200)
print("Opening Port...")
time.sleep(3)



parser = argparse.ArgumentParser(description='Turn a light on.')

parser.add_argument("-m", "--mode", help='Effect when changing')

parser.add_argument("-r", "--red", default='/255/255/255/0/',
        help='RGB values (Default: /255/255/255/0 = white)')

parser.add_argument("-g", "--green", default='0', help='Green')

parser.add_argument("-b", "--blue", default='0', help='blue')

parser.add_argument("-d", "--delay", default='0', help='delay')

args = parser.parse_args()

brk = "/"
cmd = args.mode + brk + args.red + brk + args.green + brk + args.blue + brk + args.delay + brk

ser.write(cmd.encode())

print("done")
 



 








