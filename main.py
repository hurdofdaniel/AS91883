# I have broken up the main.py file into multiple files.
# This will make it easier to read and find bugs.
import intro
import questions
import userHandler


def run():
    '''
        This function initates the quiz
        This function does not require any parameters
    '''
    while True:
        isContinue = intro.introSeqence()
        if not isContinue:
            break
        user = userHandler.userSeqence()
        correctAnwsers = questions.list()
        userHandler.addLeaderboard(user, correctAnwsers)
        userHandler.printStats(user)


# make sure this is the main file
if __name__ == "__main__":
    run()
