from  termcolor import colored, cprint
from colorama import init, Fore, Back, Style
from modules.name_print import name,print_card_middle,print_cool_suit
from modules.Deck import deck_instance
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
            print_card_middle(card.suit, suit_color, 1)
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


    def print_deck(lastcard):
        # card = Card(lastcard[0], lastcard[1], lastcard[2])
        if len(deck_instance.deck) > 1:
            cprint(Style.BRIGHT + f' _____  ','black' ,'on_light_yellow',end='')
            print()
            cprint(Style.BRIGHT + f'|╔ ╥ ╗|_____  ','black' ,'on_light_yellow',end='')
            print()
            if int(deck_instance.rank_of_last_card) == 10:
                cprint(Style.BRIGHT + f'|║   ║|   {deck_instance.rank_of_last_card}| ','black' ,'on_light_yellow',end='')
                print()
            else:
                cprint(Style.BRIGHT + f'|║   ║|    {deck_instance.rank_of_last_card}| ','black' ,'on_light_yellow',end='')
                print()
            suit_color= 'black'
            if deck_instance.cool_suit in ['♥','♦']:
                suit_color = 'red'
            print_card_middle(deck_instance.cool_suit, suit_color, 2)
            print()

            cprint(Style.BRIGHT + f'|║   ║|     | ','black' ,'on_light_yellow',end='')
            print()

            cprint(Style.BRIGHT + f'|╚ ╨ ╜|‾‾‾‾‾  ','black' ,'on_light_yellow',end='')
            print()

            cprint(Style.BRIGHT + f' ‾‾‾‾‾  ','black' ,'on_light_yellow',end='')
            print()

        elif len(deck_instance.deck) == 1:
            cprint(Style.BRIGHT + f' ____________ ','black' ,'on_light_yellow',end='')
            print()

            if deck_instance.rank_of_last_card == 10:cprint(Style.BRIGHT + f'|          {deck_instance.rank_of_last_card}| ','black' ,'on_light_yellow',end='')
            else:cprint(Style.BRIGHT + f'|           {deck_instance.rank_of_last_card}| ','black' ,'on_light_yellow',end='')
            print()

            print_card_middle(deck_instance.cool_suit)
            print()

            if deck_instance.rank_of_last_card == 10:cprint(Style.BRIGHT + f'|{deck_instance.rank_of_last_card}          |','black' ,'on_light_yellow',end='')
            else:cprint(Style.BRIGHT + f'|{deck_instance.rank_of_last_card}           |','black' ,'on_light_yellow',end='')
            print()
            cprint(Style.BRIGHT + f' ‾‾‾‾‾‾‾‾‾‾‾‾ ','black' ,'on_light_yellow',end='')
            print()
        elif len(deck_instance.deck) == 0:
            pass

"""         

 _____
|╔ ╥ ╗|_______
|║   ║|       | 
|║ ╬ ║|♥      |
|║   ║|     10|  
|╚ ╨ ╜|‾‾‾‾‾‾‾
 ‾‾‾‾‾
 ____________
|          10| 
|     ♥      |
|10          |  
 ‾‾‾‾‾‾‾‾‾‾‾‾ 
"""