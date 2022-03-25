import global_functions as gf


class question():
    question = ""
    options = []

    anwserIdx = 0

    def __init__(self, question, options, anwserIdx):
        self.question = question
        self.options = options
        self.anwserIdx = anwserIdx


# questions can be added inline
questions = []

# questions can be appended as following shows
# I will add questions using the following method
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


def list():
    correctAnwsers = 0
    for idx, question in enumerate(questions):
        isCorrect = questionRunner(question, idx)

        if isCorrect:
            correctAnwsers += 1
    return correctAnwsers


# the following string is used to make the questions tidier
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def questionRunner(question, questionIdx):
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


def anwserValidator(anwserKey, optionsAmount):
    if anwserKey.upper() not in alphabet[0:optionsAmount]:
        return False
    else:
        return anwserKey
