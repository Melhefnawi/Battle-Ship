# ULTIMATE Battleships

Ultimate Battleships is a Python terminal game, which run on the mock terminal on Heroku

Users can try to beat the computer by finding all the computer's battleships before the computer finds theirs.
Each battleship occupies one square on the board.

###### Here is a live version of my project 

<img src="/images/photo/AMI responsive.JPG">

## How to play 

Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on WiKipedia.

In this version, the player enters their name and two boards are randomly generated.

The player can see Where their ships are, indicated by an @ sign but cannot see where the computer's ships are.

Guesses are collected in the two lists, that appears every new round of the game.

The Player and the computer then take it in turns to make guesses and try to sink each other's battleships.

The Winner is the player who sink all the their opponent's battleships first.

# Features

## Existing Features

- Random board generation 
   - ships are randomly placed on both the player and computer bords
   - The player cannot see where the computer's ships are.

   
   <img src="images/photo/Game boards.JPG">

   - Play against the computer
   - Accepts user input 
   - Maintains score



   <img src="images/photo/New round.JPG">

- Input validation and error-checking 
  - You cannot enter coordinates outside the size of the grid 
  - You must enter numbers
  - You cannot enter the same guess twice

  <img src="images/photo/Validate photo.JPG">

  - Data maintained in class instances

  ## Future Features

  - Allow player to select the board size and number of ships 
  - Allow player to position ships themselves
  - Have ship larger than 1x1

  ## Data Model 

  I decided to use a set of functions as my model. The game creates sets of functions; each function controls a certain task to perform.


    All the main variables have been created at the beginning of the game, which include the size of the boards, previous coordinates entered by each player and computer, number of ships, and score for both players.


    The game is composed of sets of functions, which help in creating the boards for both players and randomly set the location of ships. The game then starts to gather the inputs from both players, then compares the inputs with previous coordinates and the ship location to indicate if the ship was hit and a point is scored.

  ## Testing 

  I have manulally tested this project by doing the following 

  - Passed the code through a PEP8 linter and confirmed there are no problems
  - Given invalid inputs strings when number are expected out of bounds input, same input twice
  - Tested in my local terminal and Code institute Heroku terminal 

  ## Bugs 

  Solved Bugs 

  - When I wrote the project, I was getting undefined variable errors. I fixed this by adding all the variables that were required to be used outside the function.


  -  While trying to add a string instead of an integer, I was getting a value error. I fixed this by putting code between try and except blocks, which fixed the error by requiring inserting an integer instead of a string.

  ### Remaining Bugs 

  - No bugs remaining

  ## Validator Testing 

  - PEP8 
    - No errors were returned from PEP8online.com

    <img src="images/photo/PEP8 pyhton.JPG">

  # Deployment

  This project was deployed using Code Institute's mock terminal for Heroku.

  - Steps for deployment:
    - Fork or clone this repository 
    - Create a new Heroku app
    - Set the buildbacks to python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

  # Creadit 

    - Code institute for the deployment terminal
    - Wikipedia for the details of the Battleships





