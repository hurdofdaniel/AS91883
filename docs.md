# Documentation

This file provides documentation on how to use my game

Directory Tree:

|- Main.py
|
|- Intro.py
|
|- UserHandler.py
|
|- Questions.py
|
|- Global_Functions.py

Main.py is used as the runner file
This is the file to run to play the game, it consists of one function run()
This function does not return, nor require parameters

Intro.py
This is the file that welcomes the user to the game, it consists multiples functions
Welcome(), this function welcomes the user and gives a chance to close the game
Instructions(), this function gives the user instructions on what the game is
IntroSequence(), this function handles the other 2 functions
  Use IntroSequence() to start the game when calling from other files

UserHandler.py
This is the file used to get the user
