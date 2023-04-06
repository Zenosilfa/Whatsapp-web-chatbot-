import pyautogui as pt 
from time import sleep
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import random



sleep(3)

position1 = pt.locateOnScreen("smileys.PNG", confidence=.6)
x = position1[0]
y = position1[1]

#gets message
def gets_message():
    global x, y

    position = pt.locateOnScreen("smileys.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x+70,y-60, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message

#posts
def post_response(message):
    global x,y
    keyboard = Controller()
    position = pt.locateOnScreen("smileys.PNG", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y +20, duration=.5)
    pt.click()
    keyboard.type(message)
    pt.typewrite("\n", interval=.05)






#Processes response
def process_response(message):
    random_no = random.randrange(3)
    if "R" in str(message).lower():
        return "sormak istediğin şeyi anlayamadım konunun dışında sorma"
    
    else:
        if random_no == 0:
            return "tekrar bekleriz"
        elif random_no == 1:
            return "anlamadım henüz bu kelimeleri öğrenemedim."
        else:
            return "anlamadım henüz bu kelimeleri öğrenemedim."

#Check for new messages
def check_for_new_messages():
    pt.moveTo(x+40,y-39, duration=.5)

    while True:
        #continuously checks green dots and new messages
        try:
            position = pt.locateOnScreen("green_circle.PNG", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new messages")
        if pt.pixelMatchesColor(int(x+40), int(y-39),(255,255,255), tolerance = 10):
            print("is_white")
            process_message = process_response(gets_message())
            post_response(process_message)
            
        else:
            print("no new messages")
    

    


