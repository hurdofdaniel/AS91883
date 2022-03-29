import global_functions as gf
import questions


def welcome():
    '''
        This function welcomes the user to the game
        It should be the first function ran

        This function does not require any parameters
        This function returns a boolean
    '''

    gf.clearScreen()
    print("Welcome to the game!")
    print("Press enter to continue")
    print("Type Q to end")
    continueInput = input()
    if continueInput.upper() == "Q":
        return False
    gf.clearScreen()
    return True


def instructions():
    '''
        This function provides instructions for the user
        This should be the second function ran but not needed

        This function does not require any parameters
        This function returns null
    '''

    print("This is a quiz game")
    questionsAmount = len(questions.questions)
    print(f"There are {questionsAmount} questions,", end=' ')
    print("each with 4 possible anwsers")
    print("Are you ready to go? [Press enter to continue]")
    input()
    gf.clearScreen()
    return


def introSeqence():
    '''
        This function runs all the functions in correct order
        It will also handle the returns of the functions

        Use this to make it easier

        This function does not require any parameters
        This function returns a boolean
    '''

    isContinue = welcome()
    if isContinue:
        instructions()
        return True
    else:
        return False
