import pyautogui
import time
time.sleep(4)
count=0
while count<=1000:                                   #enter no. of counts you want to send
    pyautogui.typewrite("")                   #write your message here
    pyautogui.press("enter")
    count=count+1
    