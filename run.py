import random
from word import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    print("Welcome to Hangman!")
    print(show_hangman(tries))
    print(completed_word)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.fromalpha():
            if guess in guessed_letters:
                print("You have already guessed that letter, please try again.", guess)
            elif guess not in word:
                print("Sorry", guess, "is not the correct word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is the correct word.")
                guessed_letters.append(guess)
                list_words = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    list_words[index] = guess
                completed_word = "".join(list_words)
                if "_" not in completed_word:
                    guessed = True 
        elif len(guess) == len(word) and  guess.fromalpha():
            if guess in guessed_words:
                print("You have already guessed that word", guess)
            elif guess != word:
                print("Sorry," guess, "is not the word.")
                tries -= 1 
                guessed_words.append(guess)
            else:
                guess = True
                completed_word = word
        else:
            print("NGuess is not valid, please try again.")
            print(show_hangman(tries))
        print(completed_word)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word correctly! You Win!)

def show_hangman(tries):
    stages = [ """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |               /|\\              |
            |               / \\              |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |               /|\\              |
            |               /                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |               /|\\              |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |               /|                |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |                |                |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                O                |
            |                                 |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                |                |
            |                |                |
            |                                 |
            |                                 |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            """
            +---------------------------------+
            |                                 |
            |             HANGMAN             |
            |           +---------+           |
            +---------------------------------+
            |                                 |
            |                                 |
            |                                 |
            |                                 |
            |                                 |
            |          +------------+         |
            |          |            |         |
            +---------------------------------|
            |        Available letters        |
            +---------------------------------+
            |                                 |
            |    A B C D E F G H I J K L M    |
            |    N O P Q R S T U V W X Y Z    |
            |                                 |
            +---------------------------------|
            |         Guess The Word          |
            +---------------------------------+
            |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  |
            +---------------------------------+
            """,
            
