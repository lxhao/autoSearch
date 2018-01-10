#!/bin/bash
adb shell screencap -p /sdcard/problem.png
adb pull /sdcard/problem.png .
