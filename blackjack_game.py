import random
from os import system as sys
from art import logo

def cards_value(cards_list: list, cards_values: dict):
    """Function returns total value of all cards."""

    value = 0
    for card in cards_list:
        value += cards_values[card]

    return value

def game_result(player_cards: list, computer_cards: list, cards_values: dict):
    """Function compares player and computer cards values and determines the game result."""

    computer_cards_value = cards_value(computer_cards, cards_values)
    player_cards_value = cards_value(player_cards, cards_values)

    print(f"Computer cards are: {computer_cards}, and their value is: {computer_cards_value}.")
    print(f"Your cards are: {player_cards}, and their value is: {player_cards_value}.")

    if computer_cards_value == player_cards_value:
        print("DRAW.")
    
    elif computer_cards_value == 21:
        print("You LOSE!")

    elif player_cards_value == 21:
        print("You WIN!")

    elif player_cards_value > 21:
        if "A" not in player_cards:
            print("You LOSE! Your cards total value is over 21.")

        elif "A" in player_cards and player_cards_value - 10 > 21:
            print("You LOSE! Your cards total value is over 21.")
    
    elif computer_cards_value > 21:
        print("You WIN! Computer cards total value is over 21.")

    elif computer_cards_value > player_cards_value:
        print(f"You LOSE! Your cards total value is {player_cards_value}, and computers cards total vaue is {computer_cards_value}.")
    
    else:
        print(f"You Win! Your cards total value is {player_cards_value}, and computers cards total vaue is {computer_cards_value}.")



def blackjack_game():
    """Function starts Blackjack game."""

    cards_symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    cards_values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }

    computer_cards = []
    player_cards = []
    game_continues = True

    for _ in range(2):
        computer_cards.append(random.choice(cards_symbols))
        player_cards.append(random.choice(cards_symbols))
    
    computer_cards_value = cards_value(computer_cards, cards_values)
    player_cards_value = cards_value(player_cards, cards_values)
    sys("cls")
    print(logo)
    print("Welcome to Blackjack Game!\n")
    print(f"Computer first card is: {computer_cards[0]}.")
    
    while game_continues:

        if computer_cards_value == 21 or player_cards_value == 21:
            print("Game over!")
            game_continues = False
        
        elif player_cards_value > 21:
            if "A" not in player_cards:
                print("Game over!")
                game_continues = False

            elif "A" in player_cards and player_cards_value - 10 > 21:
                print("Game over!")
                game_continues = False
        
        else:
            print(f"Your cards are: {player_cards}, and their value is: {player_cards_value}.")
            decision = input("Do u wamnt to get another card? Type \"y\" for yes or \"n\" for no. ")

            if decision == "y":
                player_cards.append(random.choice(cards_symbols))
                player_cards_value = cards_value(player_cards, cards_values)

            elif decision == "n":
                game_continues = False
        
        sys("cls")
    
    while computer_cards_value < 17:
        computer_cards.append(random.choice(cards_symbols))
        computer_cards_value = cards_value(computer_cards, cards_values)

    game_result(player_cards, computer_cards, cards_values)

    next_game = input("Do You want to play another game of Blackjack?\nIf yes type \"y\", if no type \"n\". ")
    if next_game == "y":
        blackjack_game()

if __name__ == "__main__":
    blackjack_game()