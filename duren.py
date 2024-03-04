import random
from itertools import product
import math
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style


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

class Deck:
    deck: list[tuple[str,str,int]]
    
    def __init__(self):
        self.ranks_values = {
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        suits = ['♥', '♦️', '♣️', '♠️']
        ranks = list(self.ranks_values)

        self.deck = [(rank, suit, self.ranks_values[rank]) for rank, suit in product(ranks, suits)]
        random.shuffle(self.deck)

    def compare_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2

        if suit1 == suit2:
            if value1 > value2:
                return 1
            if value2 > value1:
                return 2
        
        return 0
        
            
    def create_deck_for_player(self): # <-- create deck for player 
        player_deck = []
        for i in range(6):
            random_card = random.choice(self.deck)
            self.deck.remove(random_card)
            player_deck.append(random_card)
        return player_deck


class Player :
    def __init__(self,name: str, game_deck):
        self.name = name 
        self.game_deck = game_deck
        self.player_deck = game_deck.create_deck_for_player()


    def take_cards_from_deck(self):
        if len(self.player_deck) < 6:
            for i in range(6 - len(self.player_deck) ):
                card = random.choice(self.game_deck.deck)
                self.game_deck.deck.remove(card)
                self.player_deck.append(card)
        return self.player_deck
    

    def attack(self):
        ...

    def defense():
        ...    

    def take_cards_hnvc():
        ...
        

class Durak:

    def __init__(self,first_deck: list, second_deck: list, game_deck: list ,durak_ex):
        self.game_deck = game_deck
        self.first_deck = first_deck
        self.second_deck = second_deck
        self.first_name = input('write your name: ')
        self.second_name = input('write your name: ')
        self.durak_ex = durak_ex
        self.players = [self.first_name, self.second_name]
        self.odboy = []


        print(f'{self.first_name} --> chodit {first_deck}')
        print(f'{self.second_name} -->{second_deck}')
        print('cards in deck -->', len(game_deck))

        while len(first_deck)!=0  or len(second_deck) !=0 and len(game_deck) != 0:     
            command = input("attack/defense/take-cards/end-choda: ")
            if command not in ["a", "d", "t"]:
                print('wrong command')

            elif command == 'a':
                try:
                    card = int(input(f'choose card to attack(0,1,2...): '))
                    att_card = first_deck.pop(card-1)
                    print(f'{self.first_name}, attack -->',att_card)
                except IndexError:
                    print('card index out of range please write correct index of card! ')
            
            # command = input("attack/defense/take-cards/end-choda: ")


            elif command == 'd':

                try:
                    
                    card = int(input(f'choose card to defense(0,1,2...): '))
                    def_card = second_deck.pop(card-1)
                    print(f'{self.second_name}, defense -->',def_card)
                    result = durak_ex.compare_cards(att_card,def_card)
                except IndexError:
                    print('card index out of range please write correct index of card! ')

                    while result not in [0,1,2]:
                        ...
                while result != 2 and command != 't':
                    print('imposible to bito')
                    second_deck.append(def_card)
                    print(second_deck)
                        
                    card = int(input(f'choose card to defense(0,1,2...): '))
                    def_card = second_deck.pop(card-1)
                    result = durak_ex.compare_cards(att_card,def_card)
                    command = input("attack/defense/take-cards/end-choda: ")


                if result  == 2:
                    print(att_card, '<', def_card)
                    print('✔')
                

            if command == 't':
                try:
                    cards = att_card or def_card or att_card,def_card
                    buff = []
                    buff.append(cards)
                    for  i in buff:
                        second_deck.append(i)
                    print(second_deck)
                except UnboundLocalError: 
                    print('you cant do this')
                

            if command == 'end-choda':
                ...

            

# deck_instance = Deck()
# Durak(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
Card('♥','7')