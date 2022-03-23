import global_functions as gf
import questions


def welcome():
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
    print("This is a quiz game")
    questionsAmount = len(questions.questions)
    print(f"There are {questionsAmount} questions,", end=' ')
    print("each with 4 possible anwsers")
    print("Are you ready to go? [Press enter to continue]")
    input()
    gf.clearScreen()
    return


def introSeqence():
    isContinue = welcome()
    if isContinue:
        instructions()
        return True
    else:
        return False
