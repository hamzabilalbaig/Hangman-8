<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/Responsive_screen.jpg">

[View the live project here.](https://antonydavidtroy-hangman.herokuapp.com/)

# HANGMAN

For my portfolio 3 project I have choosen the fun, well known game known as Hangman. I have displayed Hangman in a Python terminal game, which runs through the Code Institute terminal on Heroku.

Users will be greeted by the welcome screen, they can choose from 3 options. First option will start the game, from there the User will be prompt an 'Enter a username', after entering a username the User will be prompt with the image of code that shows the first stage of the hangman which will increase up to 6 more times for each incorrect guess along with the random word that has been chosen which will be displayed with a " _ " for each letter in that word. Everytime the User gets a guessed letter correct, the letter will appear in place of the " _ " until the User either gets the word correct or runs out of guesses. Once the User has run out of 'lives' The game will display the last stage of hangman which will show a stickman being 'hung' on a platform. When that shows the User will be able to either, play again, or save their Username and Score to the googlesheets.  The second option will display the Highscores leaderboard which will consists of the top 5 scores along with their Username, which can be updated from all Users that play the game just as long as they can beat any of their scores.

## Table of Contents

1.[**How To Play**](#how-to-play)

2. [**User Experience(UX)**](#user-experience(ux))
     - [**Flowchart**](#flowchart)

2. [**Existing Features**](#existing-features)
      - [**Welcome Screen**](#welcome-screen)
      - [**Highscores Screen**](#highscores-screen)
      - [**Username Screen**](#username-screen)
      - [**Guessing Screen**](#guessing-screen)
      - [**Incorrect Letter Screen**](#incorrect-letter-screen)
      - [**Correct Letter Screen**](#correct-letter-screen)
      - [**Invalid Guess**](#invalid-guess)
      - [**Repeated Guess**](#repeated-guess)
      - [**Display of Hangman**](#display-of-hangman)
      - [**Win Screen**](#win-screen)
      - [**Lose Screen**](#lose-screen)
      - [**Features Left To Implement**](#features-left-to-implement)
      
3. [**Technology Used**](#technology-used)
    - [**Languages Used**](#languages-used)
    - [**Frameworks, Libraries & Programs Used**](#frameworks,-libraries-&-programs-used)
 
4. [**Testing**](#testing)
      - [**Validator Testing**](#validator-testing)
      - [**Testing User Stories from User Experience (UX) Section**](#testing-user-stories-from-user-experience-(UX)-section)
      - [**Further Testing**](#further-testing)
      - [**Issues**](#issues)
5. [**Deployment**](#deployment)
       
## How to play

Hangman is traditionally a game that derives on the basic pen and paper that can be played with 2 players or more.
However, in this game, 1 player is only needed as the words are automatically randomized and the lives will automatically be deducted for any incorrecct guess. 
The User will enters their desired Username and the game will select a random word from a word folder that consists of 100's of words. The word to be guessed will be displayed as "_ _ _ _ _" and with an image of a hangman in different stages depending on the number of incorrect guesses.
When the User guesses a letter that is in the random word, the terminal will display the correct letter guessed on the line in the " _ _ _ _ _" in the position it would be in the word. 
This process will continue until they either run out of guesses and then will be 'hung' on a platform which will be shown on the terminal and a message letting the User know they have 'died' and have lost the game. The other option will be that the User continued guessing the correct letters and got the correct word before running out of lives.
When the User has either wins or loses, they will have the option to play again, save their score or go back to the welcome screen.

## User Experience(UX)

 - First Time User Goals. 
   1. As a First Time Visitor, I want to easily navigate through the game with simple inputs.
   2. As a First Time Visitor, I want to be able to have fun, enjoy the game and feel nostalgic when playing.
   3. As a First Time Visitor, I want to be able to attempt to be any Highscores.
   4. As a First Time Visitor, I want to be able to make sure I dont get any repeated words.
 
 - Returning Visitor Goals.
   1. As a Returning Visitor, I want to be able to check and see the updated Highscores and be able to try to beat any again.
   2. As a Returning Visitor, I want the navigation to be the same as it was the first time to keep it familiar.
   3. As a Returning Visitor, I want the be able to guess different words that I haven't guessed before.
   4. As a Returning Visitor, I want to be able to play with a friend to see who gets a higher score.
     
 - Frequent User Goals.
   1. As a Frequent User, I want to be able to notice different words still being guessed.
   2. As a Frequent User, I want the navigation to be the same throughout.



#### Flowchart
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/Hangman.jpeg">
 
## Existing Features

#### Welcome Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_welcome_screen.jpg">
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_invalid_option_welcome_screen.jpg">
 - The welcome screen shows a small title at the top to show the User what game the User will be playing with a menu bar that is central in the screen.
 - The welcome screen shows a simple screen with 3 option to either play the game, check the highscores or exit the high scores.
 - The welcome screen asks the User for an input, if the User enters an invalid option, the game will let the User know that their options are either 1, 2 or 3.

#### Highscores Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_highscores.jpg">
 - The Highscores screen will display the scores and the usernames of any of the players that have the top 5 scores and will continue to update through a googlesheet.
 - In the Highscores screen, the highscores are equally spaced between so easily read with an option at the bottom of the screen to let the User know what to input to go back to the Welcome screen.

#### Username Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_username_screen.jpg">
 - The Username screen displays the image of the final stage of the hangman to let the User have an idea of what the game is displayed like.
 - The User is asked to input a Username so that the game can keep track of the score.
 - If the User puts anything else but letters in, the game will display a text to the User, letting them know they can only user letters.

#### Guessing Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_guess_screen.jpg">
 - The Guessing screen displays the hangman title, the first stage of the hangman game and also the alphabet to show the Users what they can use as a guess.
 - underneath the hangman display, the User is asked to input a guess of a letter or word.

#### Incorrect Letter Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_incorrect_guess.jpg">
 - when the Users guess is valid but is not in the word, they are greeted with text stating that their guess was not in the word, therefore being incorrect they User will lose a life/guess and will display the next stage of hangman.
 - When the Users guess is valid but incorrect, it will also change the same letter in the hangman display that the User has guessed with a " * " to let the users see what they have guessed throughout the game. 

#### Correct Letter Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_correct_guess.jpg">
 - When the Users guess is valid and also correct, they are greeted with text praising them and stating that their guess is in the word. 
 - When the Users guess is valid and correct, it will also change the same letter in the hangman display that the User has guessed with a " * " to let the users see what they have guessed throughout the game. 

#### Invalid Guess
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_invalid_guess.jpg">
 - When the Users guess is invalid, they are are greeted with text stating that their guess is not valid(not a letter).

#### Repeated Guess
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_repeated_guess.jpg">
 - As the game plays often the User may accidentally guess a letter that they have already guessed, even though we changed the letters in the available letters box to a " * " to let the User know they have already guessed that letter, it is still likely to happen. So to help the User when this happens, we display a text to let the User know that they have already guessed that letter.

#### Display of Hangman
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_display_progess.jpg">
 - From the image above, The User will be able to see their progress of not only the hangman stages but also the letters that they have used previously in the current game.
 - As the game goes on, with each guess the User decides to user, the letters in the letters box will be changed to a " * " to show that they have guessed that particular letter.
 - With each incorrect letter or guess, they hangman display will go to the next 'stage' of the display until the User gets the word or runs out of guessed, which will the show either a congratulations screen or an unfortunate lose screen.

#### Win Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_win_screen.jpg">
 - The win screen is display once the User have guessed the word correctly, once this happens the user will be greeted with a congratulations text and will ask the User to input a "Y" or "N" to either play again or exit the game, either options will store their username along with their score to a googlesheet document.

#### Lose Screen
<img src="https://github.com/AntonyDavidTroy/Hangman/blob/main/readme_images/hangman_lose_screen.jpg">
- The lose screen is displayed when the User has finally used up all of their guessed and lets them know that they have lost the game.
- When this screen shows, it displays the last stage of the hangman (a stick figure being 'hung') showing that they have died.
- Underneath the hangman display, will be the Users word with their correct guesses filled in. On a new line it greets the User to an unfortunate message letting the User know they have did not get the word and have 'died', it also display what the word was and a encouraging text to persuade the User to play again.

#### Features Left To Implement
- Possibly could add a two player game so that 2 players could have the same word and take it in turn to guess the word, but will have their own hangman display to their Username.
- Possibly could add an option where the User could input words into the game when playing multiple player modes.
- Possibly different levels to the game, e.g easy = up to 4 letter words, normal = 5 - 6 letter words or hard = 7+ letter words.
- Possibly reset the Highscores every month to let new and frequent Users be more inclined to play.


## Technology Used

##### Languages Used
 - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 
#### Frameworks, Libraries & Programs Used

- [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
- [Lucidchart](https://www.lucidchart.com/)
    - Lucidchart is used to create and store flowcharts.
- [Heroku](https://www.heroku.com) 
    - Heroku is used to build, run and scale applications in a similar manner across most languages.
- [Google Sheets](https://docs.google.com/spreadsheets/u/0/)
    - Google Sheets is an online spreadsheet app that lets you create and format spreadsheets that you can use work along side websites and programs, you can also use them to work with other people.

## Testing

#### Validator Testing
 - PEP8 Python Validator 
       - No errors were returned when passing through PEP8 - [Website here](http://pep8online.com/)
 - Checked highscores would update if I changed them in the googlesheets doc.
 - Checked that when I get a score of 2 that it would update automatically in the googlesheets doc.
 - Tested the code in the Code Institute Heroku terminal and also the terminal inside of Gitpod.
 - Checked that symbols, numbers or empty spaces will come up as invalid guesses when guessing the word.

#### Testing User Stories from User Experience (UX) Section
 - 

#### Further Testing

 - First Time User Goals. 
   - As a First Time Visitor, I want to easily navigate through the game with simple inputs.
         1. From start to finish you are easily navigating your way through the game with such simple inpus of a single letter.
   - As a First Time Visitor, I want to be able to have fun, enjoy the game and feel nostalgic when playing.
         1. When the User is playing the game, the User will notice the game is designed and played in the same way when it was orginally created. Only difference is that the it's automatically updating for the User.
   - As a First Time Visitor, I want to be able to attempt to beat any Highscores.
         1. Once the User has seen that the current highscores are low, they'll be encourage to beat it, if the highscore is reset on a regular basis(monthly for example). The User will want to be first on the highscore or beat the few that could possibly on there.
   - As a First Time Visitor, I want to be able to make sure I dont get any repeated words.
         1. There are 100's of words in the game so when the User keeps playing again or resetting the browser page, it is very unlikely that they'll get the same word twice, by the time a word is repeated the User will most likely have forgotten it as there are too many to remember, also have to take in consideration what letters the User would have guessed the games before and their current game as their gameplay could result differently.
 
 - Returning Visitor Goals.
   - As a Returning Visitor, I want to be able to check and see the updated Highscores and be able to try to beat any again.
         1. As a Returning Visitor, the User will be able to easily check and see the updated scores through the Highcores. The User will then be able to decide whether they would like to attempt to beat any scores on there.
   - As a Returning Visitor, I want the navigation to be the same as it was the first time to keep it familiar.
         1. As a Returning Visitor, the User, will be able to notice that the Display and the mechanics of the game are unchanged.
   - As a Returning Visitor, I want the be able to guess different words that I haven't guessed before.
         1. As a Returning Visitor,  The User will have 100's of words that are randomized so that the User will most likely not get the same word for a very long time.
   - As a Returning Visitor, I want to be able to play with a friend to see who gets a higher score.
         1. As a Returning Visitor, the User will be able to check the Highscore to see if their or their friends are on the Highscore, then decide to attempt to beat it.
     
 - Frequent User Goals.
   - As a Frequent User, I want to be able to notice different words still being guessed.
         1. As a Frequent User, the User will be able to still play the game and not being repeated words for a very long time, due to being too many to remember, different letters could be guessed in an order that was different to when the User first played that word.
   - As a Frequent User, I want the navigation to be the same throughout.
         1. As a Frequent User, the User will see the consistency of style and navigation and mechanics of the game to keep familarized with the game.
#### Issues
 - After Deployment and the basic Python coding for the game, I kept getting a new word added onto the current word that had to be guessed when I guessed a letter incorrect.
 - The second issue I had with this was that I could not figure out when I guessed the whole word it kept coming up as an invalid guess.(e.g guessing apple for _apple).
 - I struggled figuring out a function that would delete or replace the letter in the Available letters box when guessed.

## Deployment

- Heroku

   - Fork or clone this repository.
   - Goto the Heroku Dashboard.
   - Click New.
   - Select to create a new app.
   - Set the buildbacks to Python and NodeJs in that order.
   - Link the Heroku app to the repository.
   - Click on Deploy.

#### Credits 

 - Watched a few videos on how to implement desired functions on www.youtube.co.uk/
 - My Mentor for continuous helpful feedback, ideas and help when strugglng with parts of my code.
 - Slack community for information and also the few that helped me with the install of gspread errors that I kept getting. 
