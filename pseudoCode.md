The PseudoCode

Start While True Loop
Run the intro sequence 
  store the return as a variable called continue

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

Run the user sequence 
  store the return as a variable called user

  print what do you want me to call you
  print ill use this for the leaderboard

  get input

  clear the screen

  run check user and pass in the input
  
    loop over all users, if the given name is a user 
      return the user

    run a check name function
      if the name is not alphabetical or the input was empty
        return false
      otherwise return the name

    if the return from check name is false
      print thats an invalid name
      print enter a valid name
      and the function will get rerun
      return none
    else
      add the user and return the new user

  run printStats

  print thanks for playing "username"

  run the leaderboard function
    print leaderboard table

Run the questions sequence 
  store the return as a variable called correctAnwsers

  for all the questions in the questions list
    run the questionRunner function 
      store the return as variable

      print question x of y
      print question

      for anwserChoices
        print letter and choice

        print type the letter that corresponds with the anwser

        take input

        run the anwser validator 
          pass the input and amount of anwser options

          if thet anwser is not in a list of the avaliable options
            return false
          otherwise return the input

        if it is false
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

      if the anwser was correct add one to the total correct

    return the total correct

Run the add leaderboard function 
  pass in the user and correctAnwsers variables

Run the printStats function
  pass in the user variable

Goto start of while loop
