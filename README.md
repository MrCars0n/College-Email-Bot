# College-Email-Bot
Python bot that emails colleges for merchandise using pyautogui

NOTE 1: Bot written for gmail. Some shortcuts may differ with other platforms

NOTE 2: Space bar has been designated as kill switch. Hold down the space bar while the bot is typing in the body paragraph to prevent the email from sending and exiting loop

Setup steps:
1) Install "pyautogui" and "keyboard" librarires
2) Run MousePosition.py. Hover mouse over email "Compose" button in email platform. Take note of coordinates
3) Replace coordinates in MousePosition.py for pyautogui.click(x, y)
4) Fill in relevant information in sections designated with <>
