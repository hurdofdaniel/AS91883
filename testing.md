# Testing

This file will contain how I tested my game

I'll write rough pseudocode to show what parts I'll test
The parts I'll test are only ones that require Input

Run:
  Intro:
    Welcome:
      Welcome accepts an input of q or Q
      This will be used to end the game
    Instructions

  User:
    PrepareUser:
      PrepareUser takes an input of the name
      This is checked, it should not allow numbers
    PrintStats

  Questions:
    QuestionRunner:
      QuestionRunner takes an Input
      This is checked to see if the input is within a range of letters
      It should allow "A", "B", "C" or "D" for 4 optioned Questions

  GlobalFunctions:
    ClearScreen


Date - Input - Expected Output - Actual Output - Action - Result
Welcome
30/03 - return - next step - next step - When return key is pressed i want the game to continue - The game continues
30/03 - q - End game - End game - When the q key is pressed i want the game to end - The game ends
30/03 - quit - next step - next step - When anything other than q is entered i want the game to continue - The game continues

PrepareUser
30/03 - Daniel - Welcome Daniel - Welcome Daniel - When a valid name is provided i want the game to continue - the game continues
30/03 - 123 - Thats an invalid name - Thats an invalid name - When an input consisting of anything but letters the game should warn and reask - the game warns and reasks

QuestionRunner - First question (Anwser is B, options are A, B, C, D)
30/03 - B - Correct - Correct - When i provide the correct anwser the game should tell me i got it correct - the game tells me i got it correct
30/03 - A - Not quite - Not quite - When i provide the incorrect anwser the game tells me that i got it wrong - The game tells me i got it wrong
30/03 - E - That is not vaild, enter A-D - That is not valid, enter A-D - when i provide an invalid anwser the game tells me what is valid - The game tells me how to anwser correctly
30/03 - 1 - That is not valid, enter A-D - That is not valid, enter A-D - when i provide an invalid anwser the game tells me what is valid - The game tells me how to anwser correctly

