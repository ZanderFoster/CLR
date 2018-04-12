#!/usr/bin/env python
import serial, argparse, time

parser = argparse.ArgumentParser(description='Knock on the door')

parser.add_argument("-p", "--port", help='Port name')

parser.add_argument("-b", "--baud", help='Baud rate')

args = parser.parse_args()

ser = serial.Serial(args.port, args.baud)

while True:
    print("going to sleep")
    time.sleep(500)
