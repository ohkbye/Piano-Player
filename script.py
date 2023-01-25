from time import sleep
while True:
    try:
        speed = int(input("How fast do you want the song to be played (in ms): ")) / 1000
        break
    except:
        print("Please enter an integer")

from tkinter import Tk
import pyautogui
import keyboard
# Copy the sheet music into clipboard (ctrl + c)
music_sheet = Tk().clipboard_get()
print("Characters:", len(music_sheet))
chord_lock = False
chord = ""
def play_note(notes):
    global chord
    chord = ""
    sleep(speed/2)
    print(notes)
    pyautogui.write(notes)

   
print("Starting in 3 seconds...")
sleep(3)

for char in range(len(music_sheet)):
    if keyboard.is_pressed("ctrl"):
        exit()
    note = music_sheet[char]
    if note == " ":
        sleep(speed)
    else:
        if chord_lock == True:
            if music_sheet[char] != "]":
                chord = chord + note
            else:
                chord_lock = False
                play_note(chord)

        else:
            if music_sheet[char] == '[':
                chord_lock = True
            else:
                play_note(note)
