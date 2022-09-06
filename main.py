import random
def user_guess():
    guess = input("Enter number")
    return int(guess)

def guess(input):
    guess_right = False
    if input == "easy":
        guess_num = 10
        print(f"You have {guess_num} tries")
    elif input == "hard":
        guess_num = 5
        print(f"You have {guess_num} tries")
    else:
        print("Restart game")
        guess_right = True
    number = random.randint(1,100)

    while guess_right == False:
        num_guess = user_guess()
        if num_guess == number:
            guess_right = True
            print(f"you guessed correctly {number}")
        elif num_guess > number:
            print("Too high. Guess lower.")
            guess_num -= 1
            print(f"You have {guess_num} tries\n")
        else:
            print("Too low. Guess higher")
            guess_num -= 1
            print(f"You have {guess_num} tries\n")
        if guess_num == 0:
            print("You lose")
            break

print("Number guessing game.")
print("Choose a number between 1 and 100.")
unos = input("Choose a difficulty. Type 'easy' or 'hard': ")

guess(unos)