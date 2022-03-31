import global_functions as gf

users = []


class user():
    '''
        This is the class of the user

        This class can have variables added to expand the game

        This function is self initialising
            it requires a variable for the name
    '''

    userName = None
    correctAmount = 0

    def __init__(self, name):
        self.userName = name

    def setCorrect(self, correctAmount):
        self.correctAmount = correctAmount


def leaderboard():
    '''
        This function prints out the leaderboard

        This function does not require any parameters
        This function does not return anything
    '''

    width = 1

    for user in users:
        if len(user.userName) > width:
            width = len(user.userName)

    print("+", end='')
    print("-" * (width + 4), end='')
    print("+")

    for user in users:
        print(f"|{user.userName}", end='')
        print(' ' * (width - len(user.userName)), end='')
        print(f" - {user.correctAmount}", end='')
        print("|")

    print("+", end='')
    print("-" * int(width + 4), end='')
    print("+")


def addLeaderboard(user, correctAmount):
    '''
        This function adds the score to the user
        This function is basic but it is for safety

        This function should not be called from this file

        This function requires parameters, the user instance and the score
        This function does not return anything
    '''

    user.setCorrect(correctAmount)


def addUser(name):
    '''
        This function adds the user to the array

        This should only be called by the check user function

        This function requires a parameter, the name
        This function returns the instance of the user
    '''

    users.append(user(name))
    return users[len(users) - 1]


def checkName(name):
    '''
        This function checks if the name is valid
        It checks if the name is alphabetical and not empty

        This function requires a parameter, the given name
        This function returns either a string or a boolean
    '''

    if not name.isalpha() or name == "":
        return False
    return name


def checkUser(name):
    '''
        This function checks if everything is valid

        This function requires a parameter, the name of the user
        This function will return either null or an instance of user
    '''

    for user in users:
        if user.userName == name:
            return user
    if checkName(name) is False:
        return None
    else:
        return addUser(name)


def prepareUser():
    '''
        This function asks user for the name and validates it

        This function does not require any parameters
        This function return an instance of the user class
    '''

    print("What do you want me to call you?")
    print("(I'll use this on the leaderboard)")

    name = input()

    gf.clearScreen()

    newUser = checkUser(name)

    if newUser is None:
        print("That's an invalid name!")
        print("Press enter and type in a valid name!")
        input()
        gf.clearScreen()
        return prepareUser()
    else:
        return newUser


def printStats(user):
    '''
        This function prints information to the user

        This function requires parameters, an instance of the user class
        This function does not return anything
    '''

    print(f"Thanks for playing {user.userName}")
    print("")
    print("Leaderboard:")
    leaderboard()
    print("")
    print("Press enter to continue")
    input()
    gf.clearScreen()


def userSeqence():
    '''
        This function runs all the functions in this file in correct order
        It will also handle the returns of the functions

        Use this to make it easier

        This function does not require any parameters
        This function returns an instance of the User class
    '''

    user = prepareUser()
    printStats(user)
    return user