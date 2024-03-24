import re
import subprocess
import sys
import time
import random
import threading

def clean_response(response):
    cleaned_response = re.sub(r"^[^\w]+", "", response)
    cleaned_response = cleaned_response.capitalize()
    return cleaned_response

def ensure_coherent_ending(response, min_length=30):
    if len(response) < min_length:
        response += '...'
    return response

def speak(text):
    subprocess.Popen(["say", text])

typing_animation_running = False

def typing_animation():
    global typing_animation_running
    dot_sequence = [".", "..", "...", "   "]
    index = 0
    while typing_animation_running:
        sys.stdout.write('\rTim: ' + dot_sequence[index % len(dot_sequence)])
        sys.stdout.flush()
        index += 1
        time.sleep(0.5)
    sys.stdout.write('\r' + ' ' * (len('Tim: ') + 3) + '\r')  # Clear the line after stopping
    sys.stdout.flush()

def start_typing_animation():
    global typing_animation_running
    typing_animation_running = True
    animation_thread = threading.Thread(target=typing_animation)
    animation_thread.start()
    return animation_thread

def stop_typing_animation(animation_thread):
    global typing_animation_running
    typing_animation_running = False
    animation_thread.join()

def print_response(response):
    print("Tim:", response)