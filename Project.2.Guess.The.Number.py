# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random,simplegui
range_max=100
n_guess=7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,n_guess,attempts,range_max
    secret_number=random.randrange(0,range_max)
    
    attempts=0

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number,n_guess,range_max
    range_max=100
    n_guess=7
    print "Setting Range to [0,100), Starting New Game..."
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number,n_guess,range_max
    range_max=1000
    n_guess=10
    print "Setting Range to [0,1000), Starting New Game..."
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    # Convert to Integer.
    global n_guess,attempts
    attempts += 1
    guess=int(guess)
    print "Guess was",guess
    
    #compate guess to secret_number
    if secret_number == guess:
        print "Correct! You Win! Starting New Game..."
        new_game()
    elif secret_number > guess:
        print "Higher"
    elif secret_number < guess:
        print "Lower"
    #check to see guesses remaining
    if n_guess==attempts:
        print "Out Of Attempts! You Lose! Starting New Game..."
        new_game()
    elif n_guess>attempts:
        print "You have",n_guess-attempts, "guesses remaining, guess again."
# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200) ####### remember to create the frame ######

#Add input Field To take in guess:
frame.add_input("Make A Guess, Hit Enter",input_guess,200)
#New Game Button
frame.add_button("New Game", new_game)
#Range 0-100 Button
frame.add_button("Range is [0,100)", range100)
#Range 0-1000 button
frame.add_button("Range is [0,1000)", range1000)
# register event handlers for control elements and start frame
frame.start()

# call new_game

new_game()


# always remember to check your completed program against the grading rubric
