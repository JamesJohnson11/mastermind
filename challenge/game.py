from os import name
import requests
from flask import request
from constants import *
from helpers import *
from db import db



class Player:
    def __init__(self):
        self.name = input("Enter a player name: ")
        self.guesses = 10
        self.previous_guesses = {}
        self.initial_score = 100000


class Guess:
    def __init__(self, level):
        self.feedback = ""
        self.guess = input(GUESS_PROMPT.format(level)).upper()


    def validate_guess(self, level):
        '''Checks guess against valid digits and difficulty level to ensure onliy valid digits 
            are accepted and the correct number of digits are in player guess'''

        if "EXIT" in self.guess or "QUIT" in self.guess:

            print(GAME_ENDING)
            quit()

        valid_digits = VALID_DIGITS

        if any(character not in valid_digits for character in self.guess):
            print(VALID_DIGITS_EXCEPTION)
            return False
            

        elif len(self.guess) != int(level):
            print(GUESS_LENGTH_EXCEPTION.format(level))
            return False

        return True


    def get_guess_feedback(self, random_number):
        

        correct_digit_and_position = 0
        correct_digit_only = 0

        for i in range(len(self.guess)):
            if self.guess[i] == random_number[i]:
                correct_digit_and_position += 1
    
        correct_digit_only += common_digit_count(self.guess, random_number) - correct_digit_and_position
        feedback = POSITON_AND_DIGITS.format(correct_digit_and_position) + " " + DIGITS_ONLY.format(correct_digit_only)
        
        return feedback


class Game:
    def __init__(self):
        self.player = Player()
    
    
    def get_game_instructions():
        return GAME_INSTRUCTIONS


    def select_difficulty():
        '''Returns the number of digits allowed for each guess based on the difficulty level selected by player'''

        while True:
            difficulty = input(DIFFICULTY_SELECTION_PROMPT).upper()
            if "EXIT" in difficulty or "QUIT" in difficulty:
                print(GAME_ENDING)
                quit()
            elif difficulty == 'E':
                level = '4'
            elif difficulty == 'M':
                level = '5'
            elif difficulty == 'H':
                level = '6'
            else:
                print(INVALID_DIFFICULTY_INPUT)
                continue
            break
        
        return level

    def generate_random_number(level):
        '''Generates and returns random number from api based on difficulty level chosen by player'''

        api_url = RAND_NUM_API_URL.format(level)
        response = requests.get(api_url).text.replace("\n", "")

        #print(response) - FOR DEMO
        return response


    def play_game(self):
        '''Game logic'''
        
        player = self.player
        Game.get_game_instructions().format(player.name)
        level = Game.select_difficulty()
        random_num = Game.generate_random_number(level)
        player_guesses_left = player.guesses
        score = player.initial_score


        while player_guesses_left > 0:
            player_guess = Guess(level)
            valid_guess = player_guess.validate_guess(level)

            if player_guess.guess in player.previous_guesses:
                print(DUPLICATE_GUESS_MSG)
        
            elif valid_guess == False:
                continue

            elif player_guess.guess == random_num:
                player_guesses_left -= 1
                score *= player_guesses_left
                print(WINNER_MSG.format(MAX_ATTEMPTS-player_guesses_left))
                print("Your final score is {}\n".format(score))
                    
                try:
                    response = response = requests.post(
                                                url=DB_API_URL,
                                                json={"name": player.name, "score":score}
                                            )
                    response.raise_for_status()
                
                except requests.exceptions.HTTPError as err:
                    print(f"Oh no! We couldn't save your score :(", err, "\n")

                

                Game.play_again()



            else:
                player.previous_guesses[player_guess.guess] = player_guess.get_guess_feedback(random_num)
                player_guesses_left -= 1
                print(PREVIOUS_GUESSES)
                for key, value in player.previous_guesses.items():
                    print(key + " | " + value)
                print(REMAINING_GUESSES.format(player_guesses_left))


        print(OUT_OF_GUESSES_MSG.format(player.name))
        Game.play_again()


    def play_again():
        '''Prompts player to play game again or ends game based on player input'''

        play_again = input(PLAY_AGAIN_PROMPT).upper()

        if play_again == 'Y':
            new_game = Game()
            new_game.play_game()
            

        print(GAME_ENDING)
        quit()


new_game = Game()
new_game.play_game()
