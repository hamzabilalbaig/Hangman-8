import random
import os
from words import word_list


def clear_terminal():
    """
    Clears the terminal and code sourced from:
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word():
    word = random.choice(word_list)
    return word.upper()


def welcome():
    clear_terminal()
    print("{:^70}".format(" WELCOME TO HANGMAN! "))
    print("\n" * 6)
    print("{:^70}".format(" 1: PLAY GAME "))
    print("{:^70}".format(" 2: HIGH SCORES "))
    print('\n' * 6)


def play(word):
    clear_terminal()
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print(show_hangman(attempts))
    print(completed_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter: " + guess)
            elif guess not in word:
                print("Sorry", guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is in the word.")
                guessed_letters.append(guess)
                list_words = list(completed_word)
                indices = [i for i, letter in enumerate(word)
                           if letter == guess]
                for index in indices:
                    list_words[index] = guess
                completed_word = "".join(list_words)
                if "_" not in completed_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed that word", guess)
            elif guess != word:
                print("Sorry," + guess + "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guess = True
                completed_word = word
        else:
            print("Guess is not valid, please try again.")
            print(show_hangman(attempts))
        print(completed_word)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word correctly! You Win!")
    else:
        print("Sorry, you died")
        print("the word was " + word + " better luck next time!")


def show_hangman(attempts):
    phases = [
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
        """
        ]
    return phases[attempts]


def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
