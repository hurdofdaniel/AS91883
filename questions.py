import global_functions as gf


class question():
    '''
        This is the class for questions

        This is a self initialising class,
            pass in the question string
            pass in an array of anwser options
            pass in an int that corresponds to the anwser index

        This class can be expanded in the future to add new feautures
    '''

    question = ""
    options = []

    anwserIdx = 0

    def __init__(self, question, options, anwserIdx):
        self.question = question
        self.options = options
        self.anwserIdx = anwserIdx


questions = []

# questions can be appended as following shows
questions.append(question("What region are the Moeraki Boulders located", [
        "Canterbury",
        "Otago",
        "Taranaki",
        "Wellington"
        ], 1))

questions.append(question("What city is The Sky Tower located", [
        "Christchurch",
        "Wellington",
        "Auckland",
        "Dunedin"
        ], 2))

questions.append(question("What city is The Beehive located", [
        "Wellington",
        "Nelson",
        "Timaru",
        "Hamilton"
        ], 0))

questions.append(question("What region is Mount Cook located", [
        "Southland",
        "Gisborne",
        "Northland",
        "Canterbury"
        ], 3))

questions.append(question("Where is the Giant Bottle located", [
        "Paeroa",
        "Oamaru",
        "Wanaka",
        "Akaroa"
        ], 0))

# the following string is used to make the questions tidier
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def anwserValidator(anwserKey, optionsAmount):
    '''
        This function checks if the input is valid

        This function requires parameters,
            the input
            the amount of possible anwsers

        This function will return either a string or a boolean
    '''

    if anwserKey.upper() not in alphabet[0:optionsAmount] or anwserKey == "":
        return False
    else:
        return anwserKey


def questionRunner(question, questionIdx):
    '''
        This function asks the questions

        This function requires parameters,
            the question class instance
            the question index

        This function returns a boolean
    '''

    print(f"Question {questionIdx + 1}/{len(questions)}")
    print(question.question)
    print("")
    print("Options:")

    for idx, option in enumerate(question.options):
        print(f"{alphabet[idx]}: {option}")

    print("")
    print("Type the letter that corresponds with the anwser!")

    anwser = input()

    isValid = anwserValidator(anwser, len(question.options))

    print("")

    if isValid is False:
        print("That is not valid!")
        validOptions = f"{alphabet[0]}-{alphabet[len(question.options)-1]}"
        print(f'''Provide an options between {validOptions}''')
        print("Press enter to try again!")
        input()
        gf.clearScreen()
        return questionRunner(question, questionIdx)

    correct = None

    if anwser.upper() == alphabet[question.anwserIdx]:
        print("Correct")
        correct = True
        print("Press enter to continue")
        input()
    else:
        print("Not quite")
        correct = False
        print(f"The anwser was {alphabet[question.anwserIdx]}")
        print("Press enter to continue")
        input()

    gf.clearScreen()
    return correct


def list():
    '''
        This function handles running all the questions

        It will store the amount of correct anwsers

        This function does not require any parameters
        This function will return an int
    '''

    correctAnwsers = 0
    for idx, question in enumerate(questions):
        isCorrect = questionRunner(question, idx)

        if isCorrect:
            correctAnwsers += 1
    return correctAnwsers
