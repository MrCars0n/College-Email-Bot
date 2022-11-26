from emailBotLists import emails, names
import pyautogui
import time
import keyboard

# Wait 5 seconds to open gmail page
time.sleep(5)

# Holding space bar is kill switch, but wait to kill until body paragraph to avoid formatting issues

for x in range(1716):
    # If space bar is being held, kill loop
    if keyboard.is_pressed('space') != True:
        # Click the Compose new email button (change coordinates based on MousePosition.py
        pyautogui.click(263, 349)

        # Write Recipient
        time.sleep(.5)
        pyautogui.write(emails[x])
        pyautogui.press('tab')
        pyautogui.press('tab')

        # Write Subject
        time.sleep(.5)
        pyautogui.write('Attending ')
        pyautogui.write(names[x])
        pyautogui.write(' for the Fall Semester')
        pyautogui.press('tab')

        # Write Body
        time.sleep(.5)
        pyautogui.write('Hi Admissions,')
        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(.1)
        pyautogui.write('My name is <INSERT_NAME> and I am a senior at <INSERT_HIGH_SCHOOL_NAME> High School in <INSERT_STATE>. I am looking into applying to ')
        pyautogui.write(names[x])
        pyautogui.write(' for the fall semester. I toured your campus a month or two ago and it just feels like the perfect fit for me.')
        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(.1)
        pyautogui.write('I\'m sure you get a lot of these requests, but I was wondering if there is any chance I could receive a sticker, flag, pennant, shirt (size <INSERT_SIZE>) or anything you guys are able to send my way. I would love to show some school pride as soon as possible!')
        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(.1)
        pyautogui.write('If you can provide me with anything, please send it my way at my address <INSERT_MAILING_ADDRESS>.')
        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(.1)
        pyautogui.write('I am looking forward to possibly joining in the fall and progressing my collegiate career!')
        pyautogui.press('enter')
        pyautogui.press('enter')

        pyautogui.write('Thanks!')
        pyautogui.press('enter')
        pyautogui.press('enter')

        pyautogui.write('<INSERT_NAME>')

        # Send email only if space bar is not being held
        if keyboard.is_pressed('space') != True:
            pyautogui.hotkey('ctrl', 'enter')
    else:
        break
