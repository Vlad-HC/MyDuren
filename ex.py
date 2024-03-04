import random
import sys
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style








b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = [1, 2, 3, 5, 8, 15, 21, 34, 55, 89, 300,45,30]
c= []



def ooo():
    for i in range (len(a)):
        num = random.choice(a)
        a.remove(num)
        print(a)
        c.append(num)
        print(c)
        print('-----------------------')



# uu=8
# print(uu%8 == uu)
# print(ooo())


# def out_15(list):
#     result = []
#     for i in list:
#         if i % 15 != 0:
#             result.append(i)
#     return result


# print(out_15(a))

# num = 1
# result = num / 15
# odp = isinstance(result,(float))
# if odp == True:
#     a.pop(a.index(num))
#     print(a)





class Card:
    def __init__(self, suit, rank) -> None:
        self.rank = rank
        self.suit = suit

    def create_card():
        # Create six cards
        cards = [Card('♥', '10'), Card('♠', 'J'), Card('♦', '10'), Card('♣', '10'), Card('♥', '9'), Card('♠', '10')]

        # Print the cards in a row
        for card in cards:cprint(Style.BRIGHT + f' _____   ','black' ,'on_light_magenta',end='')
        print()

        for card in cards:
            if card.rank=='10':
                cprint(Style.BRIGHT + f'|   {card.rank}|  ', 'black' ,'on_light_magenta',end='')
            else:
                cprint(Style.BRIGHT + f'|    {card.rank}|  ', 'black' ,'on_light_magenta',end='')
        print()

        for card in cards:cprint(Style.BRIGHT + '|     |  ','black' ,'on_light_magenta', end='')
        print()

        for card in cards:
            if card.suit in ['♠','♣']:
                cprint(Style.BRIGHT + f'|  {card.suit}  |  ', 'black' ,'on_light_magenta',end='')
            if card.suit in ['♥','♦']:
                cprint(Style.BRIGHT + f'|  {card.suit}  |  ', 'red' ,'on_light_magenta',end='')
        print()

        for card in cards:cprint(Style.BRIGHT + '|     |  ','black' ,'on_light_magenta', end='')
        print()
        for card in cards:
            if card.rank == '10':
                cprint(Style.BRIGHT + f'|{card.rank}   |  ', 'black' ,'on_light_magenta',end='')
            else:
                cprint(Style.BRIGHT + f'|{card.rank}    |  ', 'black' ,'on_light_magenta',end='')
        print()

        for card in cards:cprint(Style.BRIGHT + ' ‾‾‾‾‾   ', 'black' ,'on_light_magenta',end='')


Card.create_card()










'''
 _____
|    J|
|     |
|  ♥  |
|     |
|J    |
 ¯¯¯¯¯

'''
