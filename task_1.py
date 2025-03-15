import random
words = [
    "adventure", "beautiful", "computer", "discovery", "elephant",
    "furniture", "grateful", "happiness", "internet", "judgment",
    "knowledge", "language", "mountain", "nostalgia", "obstacle",
    "persistence", "quintessential", "resilient", "structure", "transcend",
    "universal", "vibrant", "whimsical", "xylophone", "yesterday",
    "zealous", "ambitious", "butterfly", "courage", "diligent",
    "eloquent", "fascinate", "genius", "harmonize", "inspire",
    "jovial", "luminous", "meticulous", "nurture", "optimistic",
    "playful", "radiant", "symphony", "tranquility", "unite",
    "victorious", "wonderful", "xenon", "youthful", "zestful"
]
word = random.choice(words)
list_word = []
new_list = []
def word_list(word):
    for letter in word:
        list_word.append(letter)
        new_list.append(letter)
    return list_word,new_list
word_list(word)
b = -1
c = 0
for i in range(0,2):
    a =random.randrange(0,len(word))
    if a ==b :
        if c ==2 :
            c += 1
    else :
        b = a
        if len(word) == 3:
           new_list[a] ="_"
           break
        else :
           new_list[a] ="_"
           i +=1
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]
def Hangman_game(word, list_word, new_list):
    print("Welcome to Hangman Game")
    print("You have 6 lives")
    print("Good luck!")
    guessed_letters = set()
    tries = 6
    print(display_hangman(tries))
    print("your word is :")
    for letter in new_list:
     print(letter,end=" ")
    lives = 6
    while lives > 0:
        print(f"\nGuessed letters: {', '.join(sorted(guessed_letters))}")
        guess = input("\nGuess a letter: ").lower()
        if guess == "":
            print("Please enter a letter")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
            for i in range(len(word)):
                if list_word[i] == guess: 
                    new_list[i] = guess
            for letter in new_list:
                print(letter,end=" ")
            if "_" not in new_list:
                return "\nYou won!"
        else:
            lives -= 1
            tries -= 1
            guessed_letters.add(guess)
            print(display_hangman(tries))
            print("Incorrect! You have", lives, "lives left")
    return "You lose! The word was : " + word
print(Hangman_game(word,list_word,new_list))