import pyperclip, pyttsx3, time,keyboard

#Starts erngine,defines space
#sapi5 works on windows, change to "nsss" for unix
engine = pyttsx3.init(driverName='sapi5')
rate = 275
engine.setProperty('rate', rate) 
welcome = "Hello! Rate set to " +str(rate)

engine.say(welcome)
engine.runAndWait()

#Takes whatever is in clipboard
#if different, read!
#breaks if KEY is pressed
time.sleep(3)
while True:
    if keyboard.is_pressed('ctrl+alt+space'):
        oldtext = ""
        text = pyperclip.paste()
        while text != oldtext:
            #if new text is copied,continue reading
            engine.say(text)
            engine.runAndWait()
            oldtext = text
            text = pyperclip.paste()
    

    elif keyboard.is_pressed('ctrl+alt+.'):
        #speed up
        rate += 10 
        engine.setProperty('rate', rate)
        increase = "Speed set to " + str(rate)
        engine.say(increase)
        engine.runAndWait()

    elif keyboard.is_pressed('ctrl+alt+comma'):

        #slow down
        rate -= 10
        engine.setProperty('rate', rate)
        decrease = "Speed set to " + str(rate)
        engine.say(decrease)
        engine.runAndWait()

    elif keyboard.is_pressed('ctrl+alt+q'):
        #quits program
        engine.say("Goodbye")
        engine.runAndWait()
        exit()
