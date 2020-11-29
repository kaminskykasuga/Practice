# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for a in secret_word:
        if a not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    s = ''
    for a in secret_word:
        if a in letters_guessed: s += a
        else: s += '_ '
    return s

def get_available_letters(letters_guessed):
    s = ''
    for a in string.ascii_lowercase:
        if a not in letters_guessed: s += a
    return s

def hangman(secret_word):
    warnings, guesses, letters_guessed = 3, 6, []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 3 warnings left.')
    while True:
        print('-------------')
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won! Your total score for this game is: ', guesses * len(set(secret_word)))
            break
        elif guesses < 1:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        print('You have', guesses, 'guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        a = input('Please guess a letter: ').lower()
        if a in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                      get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
                continue
        elif (a.isalpha() == False) or (len(a) != 1):
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                print("Oops! That is not a valid letter. You have no warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
                continue
        letters_guessed.append(a)
        if a in secret_word:
            print('Good guess: ',  get_guessed_word(secret_word, letters_guessed))
        elif a in 'aoiue':
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            guesses -= 2
        else:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            guesses -= 1



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    if len(my_word.replace(' ', '')) != len(other_word): return False
    for i in range(len(other_word)):
        if my_word.replace(' ', '')[i] != '_':
            if my_word.replace(' ', '')[i] != other_word[i]: return False
        elif other_word[i] in my_word: return False
    return True

def show_possible_matches(my_word):
    a = ''
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            a += i + ' '
    if a == '': a = 'No matches found'
    print(a)

def hangman_with_hints(secret_word):
    warnings, guesses, letters_guessed = 3, 6, []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have 3 warnings left.')
    while True:
        print('-------------')
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won! Your total score for this game is: ', guesses * len(set(secret_word)))
            break
        elif guesses < 1:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        print('You have', guesses, 'guesses left.')
        print('Available letters: ', get_available_letters(letters_guessed))
        a = input('Please guess a letter: ').lower()
        if a == '*':
            print('Possible word matches are:', end = ' ')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        if a in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print("Oops! You've already guessed that letter. You have", warnings, "warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ",
                      get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
                continue
        elif (a.isalpha() == False) or (len(a) != 1):
            if warnings > 0:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                continue
            else:
                print("Oops! That is not a valid letter. You have no warnings left: ",
                      get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
                continue
        letters_guessed.append(a)
        if a in secret_word:
            print('Good guess: ',  get_guessed_word(secret_word, letters_guessed))
        elif a in 'aoiue':
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            guesses -= 2
        else:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            guesses -= 1


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)