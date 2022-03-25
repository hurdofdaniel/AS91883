Debugging:

When you enter the wrong value on a question, ie 3 rather then c
The game crashes with the following error

Traceback (most recent call last):
  File "AS91883\main.py", line 20, in <module>
    run()
  File "AS91883\main.py", line 14, in run
    correctAnwsers = questions.list()
  File "AS91883\questions.py", line 60, in list
    isCorrect = questionRunner(question, idx)
  File "AS91883\questions.py", line 94, in questionRunner
    return questionRunner(question)
TypeError: questionRunner() missing 1 required positional argument: 'questionIdx'

When you type an invalid question the function gets reran
I didn't pass the correct arguments to the function thus causing the error

I changed line 94, I added questionIdx as a second argument
Old:
return questionRunner(question)
New:
return questionRunner(question, questionIdx)
