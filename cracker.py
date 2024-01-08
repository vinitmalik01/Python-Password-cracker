import pyautogui
import time
time.sleep(4)
with open('passw.txt', 'r') as file:
    
    for line in file:
       
        pyautogui.write(line)
        pyautogui.press("enter")
        time.sleep(3)
