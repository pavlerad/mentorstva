import subprocess
import webbrowser
import time
import random
import threading
from win10toast import ToastNotifier

subprocess.Popen(['C:/Program Files/Google/Chrome/Application/chrome.exe'])
webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('https://www.youtube.com/')

messages = ['Zdravo', 'Hola', 'Hallo', 'Hello', 'Ola', 'Ciao']
toaster = ToastNotifier()


def display_message():
    while True:
        toaster.show_toast('Poruka:', random.choice(messages), duration=5)
        time.sleep(3)
threadMessage = threading.Thread(target = display_message())
threadMessage.start()






