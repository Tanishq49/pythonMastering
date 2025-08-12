import random
from colorama import Fore,Style,init

init(autoreset=True)
#Making a snake water and gun game in python
#This is just like rock paper and scissor

rules = """
Rules of Snake-Water-Gun game:
| Player 1 | Player 2 | Winner   |
|----------|----------|----------|
| Snake    | Water    | Snake    |
| Water    | Gun      | Water    |
| Gun      | Snake    | Gun      |
| Same     | Same     | Draw     |

"""
while True:
    print(rules)
    userInput = input(f"{Fore.YELLOW}Choose One(snake,water or gun):")
    bot_choice = ['snake','water','gun']
    bot_input = random.choice(bot_choice)
    user_winner = f"{Fore.GREEN}You are the winner"
    bot_winner = f"{Fore.MAGENTA}Bot is the winner"
    botInput = f"The choice of the bot was {Fore.BLUE}{bot_input}"
    if userInput == "snake" and bot_input == "water":
        print(user_winner)
        p
    elif userInput == "water" and bot_input == "snake":
        print(bot_winner)
        print(botInput)
    elif userInput == 'water' and bot_input == "gun":
        print(user_winner)
        print(botInput)
    elif userInput == 'gun' and bot_input == 'water':
        print(bot_winner)
        print(botInput)
    elif userInput == 'gun' and bot_input == 'snake':
        print(user_winner)
        print(botInput)
    elif userInput == 'snake' and bot_input == 'gun':
        print(bot_winner)
        print(botInput)
    elif userInput == bot_input:
        print("The game draws")
    else:
        print("Invalid Input,Please enter a valid command..")
    
