import random
def hangman():
    word=random.choice(["affection","appreciation","relationship","devotion","cherishing","infatuation","attachment","passion","friendship"])
    valid='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    while len(word)>0:
        main=""
        miss=0

        for letter in word:
            if letter in guessmade:
                main =main + letter
            else:
                main = main + "_" + " "
        if main == word :
            print(main)
            print("You win !!!")
            break

        print("Guess the word ...",main)
        guess=input()

        if guess in valid:
            guessmade = guessmade + guess
        else:
            print("Enter valid character...")
            guess=input()
        if guess not in word:
            turns = turns-1
            if turns==9:
                print("9 turns left")
                print("  --------  ")
            if turns==8:
                print("8 turns left")
                print("  --------  ")
                print("     O       ")
            if turns==7:
                print("7 turns left")
                print("  --------  ")
                print("     O       ")
                print("     |       ")
            if turns==6:
                print("6 turns left")
                print("  --------  ")
                print("     O       ")
                print("     |       ")
                print("    /        ")
            if turns==5:
                print("5 turns left")
                print("  --------  ")
                print("     O       ")
                print("     |       ")
                print("    / \      ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O       ")
                print("     |       ")
                print("    / \      ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /     ")
                print("     |       ")
                print("    / \      ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|    ")
                print("     |       ")
                print("    / \      ")
            if turns == 1:
                print("1 turn left")
                print("!!! last breaths counting , Take care !!!! ")
                print("  --------  ")
                print("   \ O _|/  ")
                print("     |       ")
                print("    / \      ")
            if turns == 0:
                print("YOU LOOSE !!!!")
                print("  --------  ")
                print("     O_|     ")
                print("    /|\      ")
                print("    / \      ")
                break


name=input("Enter your name ...")
print("Welcome ",name.title() +" !!!!")
print("-----------------------------------")
print("Try to guess the name in less than 10 attempts ...")
hangman()
print()
