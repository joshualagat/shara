import pyautogui
import pynput
import sys
import time
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Controller
from tkinter import*
import tkinter as tk

# Shara_Clicker V 0.2 Beta 
# By Joshua Solon

#  ======== settings ========
delay = 0.10  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
keyboard = Controller()
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("Shara Clicker by Joshua Lagat")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Esc")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()

def run():
    lis = Listener(on_press=on_press)
    lis.start()

    on_press()
    while running:
        if not pause:
            time.sleep(1.5)
            keyboard.press('w')
            time.sleep(2)
            keyboard.release('w')
            keyboard.press('d')
            time.sleep(1.5)
            keyboard.release('d')
            keyboard.press('s')
            time.sleep(2)
            keyboard.release('s')
            keyboard.press('a')
            time.sleep(1.5)
            keyboard.release('a')
    lis.stop()


if __name__ == "__main__":
    main()

