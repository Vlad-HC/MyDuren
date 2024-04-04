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


deck= [('8', '♦️', 8), ('8', '♣️', 8), ('6', '♠️', 6), ('6', '♠️', 6), ('6', '♠️', 6), ('6', '♠️', 6)]
class Card:
    def __init__(self,rank,suit,value) -> None:
        self.rank = rank
        self.suit = suit

    def create_card():
        # Create six cards
        cards = [Card(rank, suit, value) for rank, suit, value in deck]
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
            suit_color= 'black'
            if card.suit in ['♥','♦️']:
                suit_color = 'red'
            cprint(Style.BRIGHT + f'|  {card.suit}  |  ', suit_color ,'on_light_magenta',end='')
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
l = 0
# inp = int(input())
# if inp == 1:
#     l = l+1
#     l= l+1
# print(l)
ranks = {
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
min_rank = min(ranks.values())
max_rank = max(ranks.values())
desired_value = 10  # Значення, яке ви шукаєте

for key, value in ranks.items():
    if value == desired_value:
        print("Ключ для значення", desired_value, ":", key)

# Отримуємо відповідні ключі для мінімального та максимального значення
# min_key = [key for key, value in ranks.items() if value == min_rank][0]
# max_key = [key for key, value in ranks.items() if value == max_rank][0]

print(desired_value)
print(ranks.items())




'''
 _____
|    J|
|     |
|  ♥  |
|     |
|J    |
 ¯¯¯¯¯

'''
