#!/usr/bin/env python3

import time

import os
size = os.get_terminal_size()
lines, columns = size.lines-2, size.columns-1
col = 50

lineas = [
    "0.1 123 5 0 1 2 3 4",
    "1.15 321 8 1 2 1 2 1 2 1 2",
    "5.2 123 5 0 1 2 3 4",
]


CSI = "\33["
CLEAR = CSI + "2J"
HOME = CSI + "0;0H"


def gotoxy(x, y):
    return CSI + f"{x+1};{y+1}H"


class Pantalla:
    def __init__(self):
        self.keys = []
        self.buffer = {}
        self.cambios = {}
        self.count = {}
        self.last = {}

    def add(self, t, k, v):
        if k in self.keys:
            if self.buffer[k] != v:
                self.buffer[k] = v
                self.cambios[k] += 1
            self.count[k] += 1
        else:
            self.keys.append(k)
            self.keys.sort()
            self.buffer[k] = v
            self.cambios[k] = 0
            self.count[k] = 1
        self.last[k] = t

    def print(self):
        print(CLEAR, HOME, end="")
        for i, k in enumerate(self.keys):
            print(
                gotoxy(i % lines, (i//lines)*col) +
                "[{:03X}]".format(k),
                "{:24s}".format(self.buffer[k]),
                "({:.3f})".format(self.last[k]),
                "{:3d}".format(self.count[k]),
                "{:3d}".format(self.cambios[k]),
            )
        print(gotoxy(lines, 0), end="")


if __name__ == "__main__":
    import sys

    f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    p = Pantalla()
    t0 = None
    for linea in f.readlines():
        t, id, data = linea.strip().split(" ", 2)
        t, id, data = float(t), int(id, 16), " ".join("{:02X}".format(int(x, 16)) for x in data.split(" "))
        if not t0:
            t0 = time.time() - t
        dt = t - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)
        p.add(t, id, data)
        p.print()
