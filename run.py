import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print("Welcome to Hangman!")
    print(show_hangman(attempts))
    print(completed_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.fromalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter:" + guess + ".")
            elif guess not in word:
                print("Sorry", guess, "is not the correct word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Well done!", guess, "is the correct word.")
                guessed_letters.append(guess)
                list_words = list(completed_word)
                indices = [i for i, letter in enumerate(word)if letter == guess]
                for index in indices:
                    list_words[index] = guess
                completed_word = "".join(list_words)
                if "_" not in completed_word:
                    guessed = True
        elif len(guess) == len(word) and guess.fromalpha():
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
        print("the word was" + word + "better luck next time!")


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
