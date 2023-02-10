import random

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower())
word_bank = ["flesh", "mean", "trouble", "offer", "sheet", "live", "oatmeal", "duck", "shame", "vague", "relieved", "race", "fold", "smiling", "wound", "ring", "plantation", "wish", "cool", "stem", "increase", "invent", "class", "subtract", "giddy", "jump", "dreary", "instruct", "old", "communicate", "maddening", "reply", "courageous", "functional", "obscene", "sulky", "arrest", "yawn", "flawless", "gorgeous", "attraction", "imaginary", "report", "acid", "callous", "check", "time", "van", "science", "near", "far-flung", "vacation", "dangerous", "steel", "profuse", "charge", "mind", "next", "tooth", "radiate", "preserve", "thrill", "nod", "need", "detect", "calculator", "cap", "crate", "lewd", "fixed", "parsimonious", "incredible", "vessel", "year", "internal", "necessary", "pin", "mend", "mix", "reading", "lace", "pies", "lush", "earthy", "ruin", "self", "abject", "boy", "avoid", "garrulous", "waiting", "afterthought", "memory", "twig", "crib", "slippery", "rose", "wise", "appliance", "applaud"]

def get_word():
    mode = input("Would you like a random word or your own? (r for random/c for custom)").lower()
    if mode not in 'rc':
        print("Invalid option")
        return get_word()

    if mode == 'r':
        return random.choice(word_bank)

    else:
        return input("Input your word here: ").lower()


def display_word(word, guessed, lives):
    new_word = ""
    for letter in word:
        if letter == ' ':
            new_word += letter
        elif letter not in guessed:
            new_word += '_'
        else:
            new_word += letter

    print(f"Lives remaining: {lives}\nWord: {new_word}\nLetters remaining: {[let for let in ALPHABET if let not in guessed]}")

def get_guess(guessed):
    guess = input("Guess a letter:").lower()
    if guess in guessed:
        print(f"You alreay guessed {guess}")
        return get_guess(guessed)
    if guess == ' ':
        print("Can't guess ' '")
        return get_guess(guessed)

    return guess

def check_guess(word, guess, lives):
    if guess in word:
        print("You got a letter!")
        return (True, lives)
    
    print("Sorry! That letter is not in the word")
    return (False, lives - 1)

def check_win(word, guessed):
    for letter in word.replace(' ', ''):
        if letter not in guessed:
            return False
    return True

def get_play_again():
    response = input("Play again? (y/n)").lower()

    if response not in "yn":
        print("Invalid input")
        return get_play_again()
    
    if response == 'y': return True
    return False

def main():
    word = get_word()
    guessed = []
    lives = 7

    while lives >= 0:
        guess = get_guess(guessed)
        guessed.append(guess)
        correct, lives = check_guess(word, guess, lives)

        display_word(word, guessed, lives)
        if check_win(word, guessed): break

    if lives >= 0:
        print("You won!")
    else:
        print(f"You lost! The word was {word}")
    
    if get_play_again(): main()

if __name__ == "__main__": main()
