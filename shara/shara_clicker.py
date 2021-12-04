import pyautogui
import ctypes
import pynput
import sys
import time
import threading
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Controller
from tkinter import*
import tkinter as tk
from time import sleep
from threading import Thread, Event, RLock

#ctypes.windll.kernel32.SetConsoleTitleW("Autoclicker")

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
    print("\t Esc = Exit")
    print("\t F3 = Keyboard")
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
            time.sleep(0.1)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.press('w')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            time.sleep(0.5)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.release('w')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.press('d')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            time.sleep(0.1)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.release('d')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.press('s')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            time.sleep(0.5)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.release('s')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.press('a')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            time.sleep(0.1)
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            keyboard.release('a')
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
        else:
            sleep(delay)
    lis.stop()


if __name__ == "__main__":
    main()

