import random

def guessthenumber():
    
    number = random.randint(1, 100)
    attempt = 0
    max_attempt = 7
    
    print ("Welcome to Guess the Nummber Game!")
    print ("I have chose a number from 1 - 100")
    print(f"You have {max_attempt} attempts to complete the game")
    
    while attempt < max_attempt:
        
        try:
            
            guess = int(input("Enter a number from 1-100: "))
            attempt += 1
            
            if guess > number:
                print(f"Lower than {guess}")
        
            elif guess < number:
                print (f"Higher than {guess}")
        
            else:
                print (f"Congratsulations! You have completed the game with just {attempt} attempts!")
                break
        except ValueError:
            print ("Please enter a valid number")
        
        if attempt == max_attempt and guess != number:
            print(f"Sorry, you've used all {max_attempt} attempts. The correct number was {number}.")
            
guessthenumber()