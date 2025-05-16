def guessing_game():
    secret = 6
    guess = int(input("Enter a number between 1 and 9: "))
    
    if guess < secret:
        print("Your guess is almost there")
    elif guess > secret:
        print("Your guess is higher")
    else:
        print("Your Guess Is Correct!")