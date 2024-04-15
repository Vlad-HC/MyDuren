import random
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style


def name(name):
        elm1 = ['red']
        elm2 = ['on_light_grey']
        text_color = random.choice(elm1)
        background_color = random.choice(elm2)
        print('\r')
        print('\r')
        cprint(Style.BRIGHT + ' ' + f'{name}'+ ' ',text_color,background_color)
        print('\r')
        
def print_card_middle(symbol, color):
    cprint(Style.BRIGHT + f'|  ', 'black', 'on_light_yellow',end='')
    cprint(Style.BRIGHT + symbol, color ,'on_light_yellow',end='')
    cprint(Style.BRIGHT + f'  |  ', 'black', 'on_light_yellow',end='')

def print_cool_suit(suit):
    if suit in ['♥','♦']:
        suitcolor = 'red'
        print('\r') 
        cprint(suit ,f'{suitcolor}')
    else:
        print('\r') 
        cprint(suit ,'light_grey')

