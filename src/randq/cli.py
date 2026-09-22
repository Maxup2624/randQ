import random

from randq.data import questions
from randq.data import name_list
from randq.selector import rand_draw

def main():
    rng = random.Random()
    while True:
        chosen_name, chosen_question = rand_draw(name_list, questions, rng)
        print(f"{chosen_name}, please answer: {chosen_question}")

        user_choice = input("Enter 'Y' to continue, or any other key to quit: ")

        if user_choice.upper() != 'Y':
            break
