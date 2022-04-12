# :brain::brain: Mastermind :brain::brain:

Mastermind is a command-line game built using python and the Random Number Generator API (docs for API can be found here: <https://www.random.org/clients/http/api/>)

## Requirements

For optimal game play experience, Python version 3.9.1 or higher must be installed as well as pgAdmin 4 

## Installation 
##### (skip this step if you already have Python 3.9.1 or higher installed on your system)

You can find the steps to install Python on your system here: <https://www.python.org/downloads/>

## To Play:

1. Navigate to the folder that you would like to house all game files and clone this repository

```git
git clone https://github.com/JamesJohnson11/mastermind.git
```

2. Install requirements from requirements.txt file

```bash
ExampleName-MacBook-Air:~ username$ pip install -r requirements.txt
```

3. Once cloned, navigate to the folder on your system that contains the game files.

### Mac:
```bash
ExampleName-MacBook-Air:~ username$ cd Desktop
```
```bash
ExampleName-MacBook-Air:Desktop username$ cd folder_name
```

### PC:
```bash
C:\Users\username>cd Desktop
```
```bash
C:\Users\username\Desktop>cd folder_name
```

4. Run the game.py script using Python to initiate the start of the game

### Mac:
```bash
ExampleName-MacBook-Air:folder_name username$ python3 game.py
```

### PC:
```bash
C:\Users\username\Desktop\folder_name>py game.py
```
You will receive a prompt via the command-line that goes over the rules then asks you to enter your name
```bash
Enter player name: 
```

## Thought Process

I decided to use a class based object oriented approach to building out this game.  There are 3 classes: 
1. The Guess class - which validates player guesses through it's methods
2. The Player class - which initializes player attributes
3. The Game class - which contains the game logic 

There is a constants file that contains the bulk of the constants that are used throughout the game for things like api urls and user prompts. The app.py file contains API endpoints to communicate with the database. The db.py file sets up the database and helpers.py contains a function that checks the player guess against the answer. Finally, the models.py file contains the database schema that is used to build the player table in the database. This can be used to query all user scores.

## Rules:

1. At the start of the game the computer will randomly select a pattern of
numbers from a total of 8 different numbers (0-7). The amount of digits in the number will be based on the difficulty selection of the player.

    - Easy (E) --> 4 digits
    - Medium (M) --> 6 digits
    - Hard (H) --> 8 digits

2. The player will have 10 attempts to guess the number combinations.

3. At the end of each guess, the computer will provide one of the following responses
as feedback:
- The player guessed a correct number.

- The player guessed a correct number and its correct location.

- The player’s guess was incorrect.

*Note: The computer’s feedback will not reveal which number the player guessed
correctly)*

4. If the player is able to guess the random number in 10 guesses or less, they are declared the winner!

5. If the player is unable to guess the random number in 10 guesses, they lose the game.

6. Players can exit the game at any time by typing 'quit' or 'exit' as a response to any of the various prompts.

## License
[MIT](https://choosealicense.com/licenses/mit/)
