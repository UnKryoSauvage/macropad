print("")
print(" Loading...")
print("")

import os
os.system("color F0")
os.system("title MacroPad Console")
import threading
import tkinter as tk
from tkinter import filedialog
import mido
import pygame
import keyboard
import tkinter.ttk as ttk
pygame.init()
pygame.mixer.init()

print("")
print("--------------------------------------------------------------------------------------------------------------")
print("")

# Création des variables "son1, son2, son3...", "sound_file" et "noSoundAssignedPlaced"
son1 = ""
son2 = ""
son3 = ""
son4 = ""
son5 = ""
son6 = ""
son7 = ""
son8 = ""
son9 = ""
son10 = ""
son11 = ""
son12 = ""
son13 = ""
son14 = ""
son15 = ""
son16 = ""
sound_file = ""
noSoundAssignedPlaced = 0


# ------------------------------------------ Fonctions -------------------------------------------

def printOK(valx, valy):
    OK = tk.Label(fenetre, text="✅", fg='green', font=("30"))
    OK.place(x=valx, y=valy)

def onClose():
    fenetre.destroy()
    os.system("exit")



def fonctionAfficherPortsMIDI():
    positionPortsMIDI_y = 710
    positionPortsMIDI_x = 20

    for ports in mido.get_input_names():

        afficherPortsMIDI = tk.Label(fenetre, text=ports)
        afficherPortsMIDI.place(x=positionPortsMIDI_x, y=positionPortsMIDI_y)
        positionPortsMIDI_y += 20



def commandeBouton1():
    global son1

    son1 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son1 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 1st pad! Here's the path to the sound:")
        print(son1)
        print("")
        printOK(87, 120)

def commandeBouton2():
    global son2
    
    son2 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son2 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 2nd pad! Here's the path to the sound:")
        print(son2)
        print("")
        printOK(257, 120)

def commandeBouton3():
    global son3
    
    son3 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son3 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 3rd pad! Here's the path to the sound:")
        print(son3)
        print("")
        printOK(422, 120)

def commandeBouton4():
    global son4
    
    son4 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son4 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 4th pad! Here's the path to the sound:")
        print(son4)
        print("")
        printOK(593, 120)

def commandeBouton5():
    global son5
    
    son5 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son5 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 5th pad! Here's the path to the sound:")
        print(son5)
        print("")
        printOK(87, 278)

def commandeBouton6():
    global son6

    son6 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son6 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 6th pad! Here's the path to the sound:")
        print(son6)
        print("")
        printOK(257, 278)

def commandeBouton7():
    global son7
    
    son7 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son7 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 7th pad! Here's the path to the sound:")
        print(son7)
        print("")
        printOK(422, 278)


def commandeBouton8():
    global son8

    son8 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son8 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 8th pad! Here's the path to the sound:")
        print(son8)
        print("")
        printOK(593, 278)

def commandeBouton9():
    global son9
    
    son9 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son9 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 9th pad! Here's the path to the sound:")
        print(son9)
        print("")
        printOK(87, 438)

def commandeBouton10():
    global son10
    
    son10 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son10 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 10th pad! Here's the path to the sound:")
        print(son10)
        print("")
        printOK(257, 438)

def commandeBouton11():
    global son11
    
    son11 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son11 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 11th pad! Here's the path to the sound:")
        print(son11)
        print("")
        printOK(422, 438)

def commandeBouton12():
    global son12
    
    son12 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son12 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 12th pad! Here's the path to the sound:")
        print(son12)
        print("")
        printOK(593, 438)

def commandeBouton13():
    global son13
    
    son13 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son13 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 13rd pad! Here's the path to the sound:")
        print(son13)
        print("")
        printOK(87, 610)

def commandeBouton14():
    global son14
    
    son14 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son14 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 14th pad! Here's the path to the sound:")
        print(son14)
        print("")
        printOK(257, 610)

def commandeBouton15():
    global son15
    
    son15 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son15 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 15th pad! Here's the path to the sound:")
        print(son15)
        print("")
        printOK(422, 610)

def commandeBouton16():
    global son16
    
    son16 = filedialog.askopenfilename(title="Open", defaultextension=".wav", filetypes=[("Fichiers .wav", "*.wav")])
    if son16 == "":
        print("The user tried to link a sound to a pad, but finally didn't.")
        print("")
    else:
        print("Sound linked to the 16th pad! Here's the path to the sound:")
        print(son16)
        print("")
        printOK(593, 610)




def clearPadDeSonAssigne():
    global noSoundAssigned

    if noSoundAssignedPlaced == 1:
        noSoundAssigned.destroy()



def pasDeSonAssigne():
    noSoundAssigned = tk.Label(fenetre, text="Please assign a sound to the pad you've pressed.", fg='red', font=("Arial", "8", "bold"))
    print("The pressed pad doesn't seems to have any sound linked to it...")
    print("")

    noSoundAssigned.place(x=214, y=661)
    noSoundAssignedPlaced = 1

    croix = tk.Label(fenetre, text="x", fg='red', font=("Arial", "13", "bold"))
    croix.place(x=195, y=658)

    os.system("timeout 0 >nul")
    croix.place(x=0, y=100000)



def ecouterConnexionMIDI():
    global padSounds, sound_file

    with mido.open_input("Arturia MiniLab mkII 1", backend='mido.backends.rtmidi') as port:

        try:

            while True:

                # Attendre un message MIDI
                msg = port.receive()

                # Vérifier si le message est du type "note_on" (appui sur un pad)
                if msg.type == 'note_on':
                    pad_number = msg.note
                    print("Pad pressed! Pad number: " + str(pad_number))
                        
                    # Vérifier si le numéro de pad est présent dans le dictionnaire des sons
                    if pad_number == 36:
                        if son1:
                             sound_file = son1
                        else:
                            pasDeSonAssigne()
                            return msg

                    if pad_number == 37:
                        if son2:
                           sound_file = son2
                        else:
                            pasDeSonAssigne()
                            return msg

                    if pad_number == 38:
                        if son3:
                            sound_file = son3
                        else:
                             pasDeSonAssigne()
                    if pad_number == 39:
                        if son4:
                            sound_file = son4
                        else:
                            pasDeSonAssigne()
                    if pad_number == 40:
                        if son5:
                            sound_file = son5
                        else:
                            pasDeSonAssigne()
                    if pad_number == 41:
                        if son6:
                            sound_file = son6
                        else:
                            pasDeSonAssigne()
                    if pad_number == 42:
                        if son7:
                            sound_file = son7
                        else:
                            pasDeSonAssigne()
                    if pad_number == 43:
                        if son8:
                            sound_file = son8
                        else:
                            pasDeSonAssigne()
                    if pad_number == 44:
                        if son9:
                            sound_file = son9
                        else:
                            pasDeSonAssigne()
                    if pad_number == 45:
                        if son10:
                            sound_file = son10
                        else:
                            pasDeSonAssigne()
                    if pad_number == 46:
                        if son11:
                            sound_file = son11
                        else:
                            pasDeSonAssigne()
                    if pad_number == 47:
                        if son12:
                            sound_file = son12
                        else:
                            pasDeSonAssigne()
                    if pad_number == 48:
                        if son13:
                            sound_file = son13
                        else:
                            pasDeSonAssigne()
                    if pad_number == 49:
                        if son14:
                            sound_file = son14
                        else:
                            pasDeSonAssigne()
                    if pad_number == 50:
                        if son15:
                            sound_file = son15
                        else:
                            pasDeSonAssigne()
                    if pad_number == 51:
                        if son16:
                            sound_file = son16
                        else:
                            pasDeSonAssigne()

                    # Charger et jouer le fichier audio s'il existe
                    if sound_file:
                        sound = pygame.mixer.Sound(sound_file)
                        sound.play()
                        print("Sound played.")
                        print("")
                            
        except KeyboardInterrupt:
            pass



def attendreUneSeconde():

    os.system("timeout 1 >nul")

# -------------------------------------------- Code ----------------------------------------------

# Créer une fenêtre et faire ses réglages
fenetre = tk.Tk()
fenetre.geometry("710x800")
fenetre.title("MacroPad for Arturia MiniLab MKII")
fenetre.iconbitmap("files\\icon.ico")
fenetre.resizable(False, False)
fenetre.protocol("WM_DELETE_WINDOW", onClose)
fenetre.config(bg="white")

# Importer le layer
layer = tk.PhotoImage(file="files/layer.png")
afficherLayer = tk.Label(fenetre, image=layer)
afficherLayer.place(x=0, y=0)

# Afficher les ports MIDI
fonctionAfficherPortsMIDI()

# Créer et afficher des boutons
bouton1 = tk.Button(fenetre, text="Add a sound", command=commandeBouton1)
bouton1.place(x=63, y=78)

bouton2 = tk.Button(fenetre, text="Add a sound", command=commandeBouton2)
bouton2.place(x=233, y=78)

bouton3 = tk.Button(fenetre, text="Add a sound", command=commandeBouton3)
bouton3.place(x=397, y=78)

bouton4 = tk.Button(fenetre, text="Add a sound", command=commandeBouton4)
bouton4.place(x=567, y=78)

bouton5 = tk.Button(fenetre, text="Add a sound", command=commandeBouton5)
bouton5.place(x=63, y=240)

bouton6 = tk.Button(fenetre, text="Add a sound", command=commandeBouton6)
bouton6.place(x=233, y=240)

bouton7 = tk.Button(fenetre, text="Add a sound", command=commandeBouton7)
bouton7.place(x=397, y=240)

bouton8 = tk.Button(fenetre, text="Add a sound", command=commandeBouton8)
bouton8.place(x=567, y=240)

bouton9 = tk.Button(fenetre, text="Add a sound", command=commandeBouton9)
bouton9.place(x=63, y=402)

bouton10 = tk.Button(fenetre, text="Add a sound", command=commandeBouton10)
bouton10.place(x=233, y=402)

bouton11 = tk.Button(fenetre, text="Add a sound", command=commandeBouton11)
bouton11.place(x=397, y=402)

bouton12 = tk.Button(fenetre, text="Add a sound", command=commandeBouton12)
bouton12.place(x=567, y=402)

bouton13 = tk.Button(fenetre, text="Add a sound", command=commandeBouton13)
bouton13.place(x=63, y=570)

bouton14 = tk.Button(fenetre, text="Add a sound", command=commandeBouton14)
bouton14.place(x=233, y=570)

bouton15 = tk.Button(fenetre, text="Add a sound", command=commandeBouton15)
bouton15.place(x=397, y=570)

bouton16 = tk.Button(fenetre, text="Add a sound", command=commandeBouton16)
bouton16.place(x=567, y=570)

threadConnexionsMIDI = threading.Thread(target=ecouterConnexionMIDI)
threadConnexionsMIDI.start()

# -------------------------------------- Fin du programme ----------------------------------------

fenetre.mainloop()