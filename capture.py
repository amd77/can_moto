#!/usr/bin/env python3

import serial
import sys
import time

s = serial.Serial("/dev/ttyUSB0", 115200)
f = open(sys.argv[1], "w") if len(sys.argv) > 1 else sys.stdout
t0 = time.time()
while True:
    msg = s.readline().decode("cp437")
    if "CAN Receiver" in msg:
        continue
    f.write(msg)
    f.flush()
