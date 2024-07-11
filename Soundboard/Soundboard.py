import pygame
import os


# Clears console
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


# This function is just a really long-winded way of adding a forward slash if it isn't present as when copying the
# folder location Windows doesn't add the forward slash which can cause errors.
def folder_location_formatting():
  counter = 0  # Since we only need to check the last character This variable exists as a check that you are only
  # looking at the last character in the line.
  
  file = open('FolderLocation.txt', 'r')
  for num in reversed(file.readline()):  # The reversed() function makes life easier as it goes from back to front.
    if counter == 0:
      if num == "\\":
        counter = counter + 1
      else:
        file.close()
        file = open('FolderLocation.txt', 'a')
        file.write("\\")
        file.close()
        file = open('FolderLocation.txt', 'r')
        counter = counter + 1
  file.close()


# This function just sets the folder location so the user can set their own one.
def set_folder_location():
  folder_location = input("Enter folder location where the audio files are stored "
                          "(remove the quotation marks if present) or type 'cancel' to keep current one: ")
  
  if folder_location.lower() != 'cancel':
    file = open('FolderLocation.txt', 'w')
    file.write(folder_location)
    file.close()
    input('Folder location set to ' + folder_location + '. Press enter to return file selection. ')
    cls()
  else:
    input("Canceled action. Press enter to return file selection. ")
    cls()


# Plays the audio file that is requested or sends request to change the folder location.
def audio_player():
  # Initialize the mixer module
  pygame.mixer.init()
  
  # Requests file you want to play or allows you to change where to search for the file.
  selection = input("Enter name of file you want to play or type 'enter folder location': ")
  
  if selection.lower() == 'enter folder location':
    set_folder_location()
  else:
    folder_location_formatting()
    
    try:
      # Opens file where the file path to folder with audio file is located.
      file = open("FolderLocation.txt", "r")
      filepath = file.readline() + selection  # Mushes the audio file name and file path into one variable.
      file.close()
      
      pygame.mixer.music.load(filepath)  # Loads the audio file. Errors occur here if the user has done something wrong.
      pygame.mixer.music.play()  # Plays audio file
      print("Playing sound.\n")
      while pygame.mixer.music.get_busy():  # Ensures the audio file keeps playing until it is finished.
        continue
      cls()
    except pygame.error:  # Catches any errors normally due to user misuse
      input("Something went wrong trying to play this file. \n"
            "Check the set file location contains the file or file your trying to play is in the correct format.")
      cls()


cls()

while True:
  audio_player()
