#!/usr/bin/env python

#import colorsys
import math
import time
import sys
import os

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0) # tested on pHAT/HAT with rotation 0, 90, 180 & 270
unicorn.brightness(0.5)
u_width,u_height=unicorn.get_shape()

#90, 120, 150, 180, 210, 240

brightness = [90, 90, 90, 120, 150, 180, 210, 240]
#sleep_interval = [0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01, 0.01, 0.01]
sleep_interval = [0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01, 0]
#sleep_interval = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
#sleep_interval = [0.05, 0.05, 0.04, 0.04, 0.1, 0.1, 0.1, 0.1, 0.1]



max_voltage = 990
min_voltage = 800
interval = (max_voltage - min_voltage) / u_width
#print(float(sys.argv[1]))
displayed_width = int((float(sys.argv[1]) - min_voltage) / interval) + 1
if displayed_width > u_width:
    displayed_width = u_width

if displayed_width < 0:
    displayed_width = 1
#displayed_width = 8
#print (displayed_width)
valid_colors = ["red", "green", "blue", "yellow", "cyan", "purple", "white"]
color_vals = {"red": [1, 0, 0],
              "green": [0, 1, 0],
              "blue": [0, 0, 1],
              "yellow": [1, 1, 0],
              "cyan": [0, 1, 1],
              "purple": [1, 0, 1],
              "white": [1, 1, 1]}

#print(os.environ["p_color"])
#print("displayed_width %d" % displayed_width)
try:
    os.environ["p_color"]
    p_color = os.environ["p_color"]
except KeyError:
    p_color = "red"

if p_color not in valid_colors:
    print(p_color + ": p_color not valid, using default red")
    p_color = "red"
#os._exit(0)

def get_color2(level):
    if level < 1 or level > 8:
        print("level invalid %d" % level)
        level = 8

    level = level - 1
    r, g, b = color_vals[p_color];
    return r * brightness[level], g * brightness[level], b * brightness[level]

def show_level(level):
    if level == 0:
        unicorn.clear()
        unicorn.show()
        return
    for i in range(level):
        r, g, b = get_color2(i+1)
        for y in range(u_height):
            unicorn.set_pixel(i, y, r, g, b)

    for i in range(level, 9):
        for y in range(u_height):
            unicorn.set_pixel(i, y, 0, 0, 0)

    unicorn.show()


for level in range(displayed_width + 1):
    show_level(level)
    time.sleep(sleep_interval[level])

for level in reversed(range(displayed_width + 1)):
    show_level(level)
    time.sleep(sleep_interval[level])

