# HANGMAN

For my portfolio 3 project I have choosen the fun, well known game known as Hangman. I have displayed Hangman in a Python terminal game, which runs through the Code Institute terminal on Heroku.

Users will be greeted by the welcome screen, they can choose from 3 options. First option will start the game, from there the User will be prompt an 'Enter a username', after entering a username the User will be prompt with the image of code that shows the first stage of the hangman which will increase up to 6 more times for each incorrect guess along with the random word that has been chosen which will be displayed with a " _ " for each letter in that word. Everytime the User gets a guessed letter correct, the letter will appear in place of the " _ " until the User either gets the word correct or runs out of guesses. Once the User has run out of 'lives' The game will display the last stage of hangman which will show a stickman being 'hung' on a platform. When that shows the User will be able to either, play again, or save their Username and Score to the googlesheets.  The second option will display the Highscores leaderboard which will consists of the top 5 scores along with their Username, which can be updated from all Users that play the game just as long as they can beat any of their scores.

[Click here to go to the live version of my Project.](https://antonydavidtroy-hangman.herokuapp.com//)


## How to play

Hangman is traditionally a game that derives on the basic pen and paper that can be played with 2 players or more.
However, in this game, 1 player is only needed as the words are automatically randomized and the lives will automatically be deducted for any incorrecct guess. 
The User will enters their desired Username and the game will select a random word from a word folder that consists of 100's of words. The word to be guessed will be displayed as "_ _ _ _ _" and with an image of a hangman in different stages depending on the number of incorrect guesses.
When the User guesses a letter that is in the random word, the terminal will display the correct letter guessed on the line in the " _ _ _ _ _" in the position it would be in the word. 
This process will continue until they either run out of guesses and then will be 'hung' on a platform which will be shown on the terminal and a message letting the User know they have 'died' and have lost the game. The other option will be that the User continued guessing the correct letters and got the correct word before running out of lives.
When the User has either wins or loses, they will have the option to play again, save their score or go back to the welcome screen.
