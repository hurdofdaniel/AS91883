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
        is_continue = intro.introSeqence()
        if not is_continue:
            break
        user = userHandler.userSeqence()
        correct_anwsers = questions.list()
        userHandler.addLeaderboard(user, correct_anwsers)
        userHandler.printStats(user)


# make sure this is the main file
if __name__ == "__main__":
    run()
