import global_functions as gf

users = []


def userSeqence():
    user = prepareUser()
    printStats(user)
    return user


class user():
    userName = None
    correctAmount = 0

    def __init__(self, name):
        self.userName = name

    def setCorrect(self, correctAmount):
        self.correctAmount = correctAmount


def leaderboard():
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


def checkUser(name):
    for user in users:
        if user.userName == name:
            return user
    if isinstance(checkName(name), (bool)) is True:
        # handle invalid name
        return None
    else:
        return addUser(name)


def addUser(name):
    users.append(user(name))
    return users[len(users) - 1]


def checkName(name):
    # this will return a false if the name is invalid
    if not name.isalpha() or name == "":
        return False
    return name


def prepareUser():
    # users.append(user("test"))
    print("What do you want me to call you?")
    print("(I'll use this the leaderboard)")
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


def addLeaderboard(user, correctAmount):
    user.setCorrect(correctAmount)


def printStats(user):
    print(f"Thanks for playing {user.userName}")
    print("")
    print("Leaderboard:")
    leaderboard()
    print("")
    print("Press enter to continue")
    input()
    gf.clearScreen()
