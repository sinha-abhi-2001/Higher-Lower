#importing required modules
from game_data import data
from art import logo, vs
from random import randint


#printing the game logo.
print(logo)


#defining required variables
is_game_over = False
curr_score = 0
a_index = 0
#creating a function name chose_person() that returns a random person from 
#game data.
def chose_person():
    return data[randint(0,len(data)-1)]["name"]

#definign initial persons
person_a = chose_person()
person_b = chose_person()


##run a while loop until user types a wrong answer
while not is_game_over:
    print(f"Compare A: {data[person_a]['name']}, a {data[person_a]['description']} from {data[person_a]['country']}")
    is_game_over = False
##inside the while loop if the user types corrects answer then again call chose_person