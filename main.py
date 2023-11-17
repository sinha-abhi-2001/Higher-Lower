#importing required modules
from game_data import data
from art import logo, vs
from random import randint
import os



#defining required variables
is_game_over = False
score = 0

#creating a function name chose_person() that returns a random person from 
#game data
def chose_person():
    person = data[randint(0,len(data)-1)]
    return person

#definign initial persons
person_a = chose_person()
person_b = chose_person()
while person_a == person_b:
    person_a = chose_person()
##run a while loop until user types a wrong answer
while not is_game_over:
    #printing the game logo.
    print(logo)
    if score > 0:
        print(f"You are right! You'r current score is {score}")
    ##printing the two person.s details
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Againts B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

    ##checking which person has more follower and storing it in a variable
    if person_a['follower_count'] > person_b['follower_count']:
        answer = "A"
    else:
        answer = "B"
    ##store user's input
    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    if answer == user_choice:
        score += 1
        person_a = person_b
        ##inside the while loop if the user types corrects answer then again call chose_person
        person_b = chose_person()
        while person_a == person_b:
            person_a = chose_person()
    else:
        is_game_over = True
        print(f"Sorry that's wrong, Final score: {score}")
    os.system('cls')