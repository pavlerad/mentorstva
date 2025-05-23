import random
import subprocess
import webbrowser
from win10toast import ToastNotifier
import threading
import time



#subprocess.Popen('"C:\Program Files\Google\Chrome\Application\chrome.exe"')

#webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('https://www.youtube.com/watch?v=gsZiaNeD-Ms')

#toaster = ToastNotifier()
#toaster.show_toast("Pavle", random.choice(messages), duration=5)
#time.sleep(3)

#messages = ['Zdravo', 'Hello', 'Hola', "Olá", 'Hallo', 'Bonjour', 'Здравствуйте']



def hello_world():
    while True:
        print("Hello world")
        time.sleep(1)


threadHello = threading.Thread(target = hello_world)
threadHello.start()


print("Urlam")

