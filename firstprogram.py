guesses = 5
import random as r
print("Hello there? Would you like to guess my number? y/n")
play = input()
if play == "y" :
    print("Good good, My number is between 1 and 10, You have 5 guesses.")
    number = r.randint(1,10)
    while guesses != 0 :
        
        guess = input()
        if guess == number :
            print("Congratulations! You managed to guess my number")
            break
        else :
            guesses -= 1
            if guesses == 0 :
                print("Oh dear, you have run out of guesses. Goodbye")
            else :
                print("Oh dear, that was incorrect. You have " + str(guesses) + " remaining")        

elif play == "n" :
    print("Goodbye.")