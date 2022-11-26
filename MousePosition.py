import pyautogui
import time

# Delay start to postion mouse
time.sleep(.5)

# Repeat mouse coordinates to account for movement
for x in range(50):
    # Print current coordinates of mouse position
    print(pyautogui.position())
