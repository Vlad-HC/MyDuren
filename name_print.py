import random
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style


def name(name):
        elm1 = ['red','black','green','yellow','blue','magenta','cyan','light_grey','light_red','light_green','light_yellow','light_blue','light_magenta','light_cyan']
        elm2 = ['on_yellow','on_blue','on_magenta','on_cyan','on_white','on_light_grey','on_light_red','on_light_green','on_light_yellow','on_light_blue','on_light_magenta','on_light_cyan']
        text_color = random.choice(elm1)
        background_color = random.choice(elm2)
        print('\r')
        print('\r')
        cprint(Style.BRIGHT + ' ' + f'{name}'+ ' ',text_color,background_color)
        print('\r')
        
def print_card_middle(symbol, color):
    cprint(Style.BRIGHT + f'|  ', 'black', 'on_light_magenta',end='')
    cprint(Style.BRIGHT + symbol, color ,'on_light_magenta',end='')
    cprint(Style.BRIGHT + f'  |  ', 'black', 'on_light_magenta',end='')

def print_cool_suit(suit):
    if suit in ['♥','♦️']:
        suitcolor = 'red'
        print('\r') 
        cprint(suit ,f'{suitcolor}')
    else:
        print('\r') 
        cprint(suit ,'black')

