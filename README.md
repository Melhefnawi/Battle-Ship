# ULTIMATE Battleships

Ultimate Battleships is a Python terminal game, which run on the mock terminal on Heroku

Users can try to beat the computer by finding all the computer's battleships before the computer finds theirs.
Each battleship occupies one square on the board.

###### Here is a live version of my project 

## add a photo here for ami 

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

   ## add photo here for the board generation 

   - Play against the computer
   - Accepts user input 
   - Maintains score

   ## add another photo to show the above 

- Input validation and error-checking 
  - You cannot enter coordinates outside the size of the grid 
  - You must enter numbers
  - You cannot enter the same guess twice

  ## add photo here to show above 

  - Data maintained in class instances

  ## Future Features

  - Allow player to select the board size and number of ships 
  - Allow player to position ships themselves
  - Have ship larger than 1x1

  ## Data Model 

  I decided to use a sets of functions as my model. The game creates sets functions, each function control a certain task to perform

  All the main varialbles have been created at the beginning of the game which include the size of the boards, previous coordinate entered by each player and computer, number of ships, and score for both players

  The game composed of sets of fuction, which help in creating the boards for both player, and randomly set the location of ships then game start to gather the input from both player, then compare the input with pervious coordinate and the ship location, to indicate if the ship was hit and a point is scored

  ## Testing 

  I have manulally tested this project by doing the following 

  - Passed the code through a PEP8 linter and confirmed there are no problems
  - Given invalid inputs strings when number are expected out of bounds input, same input twice
  - Tested in my local terminal and Code institute Heroku terminal 

  ## Bugs 

  Solved Bugs 

  - When I wrote the project i was getting undefined variable errors, i fixed this by adding to all the variables that required to be used outside the function

  - While trying to add string instead of integer, i was getting a value error, i fixed this by putting code between try and except block fixed the error by requiring inserting a integer instead of string.

  ### Remaining Bugs 

  - No bugs remaining

  ## Validator Testing 

  - PEP8 
    - No errors were returned from PEP8online.com

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





