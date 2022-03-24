The PseudoCode









Start While True Loop
Run the intro sequence and store the return as a variable called continue

Clear the screen
Print welcome
print press enter to continue
print type q to end

Get input
if input is q
  return false
clear the screen
return true

print this is a quiz game
get amount of questions
print there are x amount of questions
print each with 4 possible anwsers
print are you ready

clear the screen
return true if input prior was not q
return false if input prior was q

If the continue is false, end the program
Otherwise continue on

Run the user sequence and store the return as a variable called user

print what do you want me to call you
print ill use this for the leaderboard

get input

clear the screen

run check user and pass in the input

if the user exists return the user
if the user doesnt exist check the name and return user
if name is invalid return null

if the return is null
print thats an invalid name
print enter a valid name

clear the screen and rerun function

else if the name is valid

run printStats

print thanks for playing and the username

run the leaderboard function
print leaderboard table

Run the questions sequence and store the return as a variable called correctAnwsers

for all the questions in the questions list
run the questionRunner function store the return as variable

print question x of y
print question

for anwserChoices
print letter and choice

print type the letter that corresponds with the anwser

take input

check if the anwser is a valid anwser

if it is not
print that is not valid
print enter a letter between the a-d

clear the screen

rerun the function

check if the given anwser was correct
print correct
set correct to True

else
print not quite
print correct anwser is x
set correct to false

clear the screen
return if it was correct

if the anwser was corret add one to the total correct

return the total correct

Run the add leaderboard function and pass in the user and correctAnwsers variables

Run the printStats function and pass in the user variable

Goto start or while loop
