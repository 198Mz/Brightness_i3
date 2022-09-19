#!/usr/bin/env python3

import subprocess
import sys

def set_brightness(screen, value):
    subprocess.call(["xrandr", "--output", screen, "--brightness", value])

if __name__ == "__main__":
    value = sys.argv[1]
    result = subprocess.run(["xrandr", "--listmonitors"], stdout=subprocess.PIPE)
    screens = result.stdout.decode("utf8").split(" ")
    screenOne = screens[-6].replace("\n", "")
    screenTwo = screens[-1].replace("\n", "")

    screens = []
    screens.append(screenOne)
    screens.append(screenTwo)

    for i in screens:
        set_brightness(i, value)