from  termcolor import colored, cprint
from colorama import init, Fore, Back, Style
from name_print import name,print_card_middle,print_cool_suit

class Card:
    def __init__(self,rank,suit,value) -> None:
        self.rank = rank
        self.suit = suit

    def print_cards(deck):
        # Create six cards
        cards = [Card(rank, suit, value) for rank, suit, value in deck]
        # Print the cards in a row
        for card in cards:cprint(Style.BRIGHT + f' _____   ','black' ,'on_light_yellow',end='')
        print()

        for card in cards:
            if card.rank=='10':
                cprint(Style.BRIGHT + f'|   {card.rank}|  ', 'black' ,'on_light_yellow',end='')
            else:
                cprint(Style.BRIGHT + f'|    {card.rank}|  ', 'black' ,'on_light_yellow',end='')
        print()

        for card in cards:cprint(Style.BRIGHT + '|     |  ','black' ,'on_light_yellow', end='')
        print()

        for card in cards:
            suit_color= 'black'
            if card.suit in ['♥','♦']:
                suit_color = 'red'
            print_card_middle(card.suit, suit_color)
        print()

        for card in cards:cprint(Style.BRIGHT + '|     |  ','black' ,'on_light_yellow', end='')
        print() 
        for card in cards:
            if card.rank == '10':
                cprint(Style.BRIGHT + f'|{card.rank}   |  ', 'black' ,'on_light_yellow',end='')
            else:
                cprint(Style.BRIGHT + f'|{card.rank}    |  ', 'black' ,'on_light_yellow',end='')
        print()

        for card in cards:cprint(Style.BRIGHT + ' ‾‾‾‾‾   ', 'black' ,'on_light_yellow',end='')
