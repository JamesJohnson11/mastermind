### DATABASE API CONSTANTS ###
DB_API_URL = "http://localhost:5000/player-scores"
HIGH_SCORE_ENDPOINT_URL = "http://localhost:5000/high-scores"


### MISC CONSTANTS ###
GAME_INSTRUCTIONS = "\nHi {}! The name of the game is 'Mastermind'!\n\nRules:\n1. You will have 10 chances to guess a random four digit number.\n2. Each digit within the four digit number will be an integer from 0-7.\n3. Duplicate digits are allowed.\n4. If you are able to guess the number in 10 guesses or less, you are a Mastermind and you have won the game! If not, you LOSE!!!\n5. Exit the game at any time by typing 'quit' or 'exit' as a response to any of the various prompts.\n"
VALID_DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7"]
GAME_ENDING = "\nSee you soon! Goodbye...\n"


### USER INPUT PROMPT CONSTANTS ###
GUESS_PROMPT = "\nGuess a {} digit number: "
DIFFICULTY_SELECTION_PROMPT= "Select difficulty [E/M/H]: "
PLAY_AGAIN_PROMPT = "Would you like to play again (Y/N)? : "



### EXCEPTION CONSTANTS ###
VALID_DIGITS_EXCEPTION = "\nOnly numbers 0-7 are allowed. Try again...\n"
GUESS_LENGTH_EXCEPTION = "\nGuess must be {} digits long. Try again...\n"
INVALID_DIFFICULTY_INPUT = "Invalid input. Try again..."


### WIN/LOSS CONSTANTS ###
WINNER_MSG = "\nCongratulations, it took you {} tries to become a Mastermind! You win!!!\n"
MAX_ATTEMPTS = 10
OUT_OF_GUESSES_MSG = "\nSorry {}, you're all out of guesses... YOU LOSE!\n"


### FEEDBACK CONSTANTS ###
DIGITS_ONLY = "Correct Digits Only: {}"
POSITON_AND_DIGITS = "Correct Digits & Position: {}"
REMAINING_GUESSES = "\n{} guesses left...\n"
PREVIOUS_GUESSES = "\nPrevious Guesses: "
DUPLICATE_GUESS_MSG = "\nYou've already guessed this number. Please try another number...\n"


