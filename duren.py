import random
from itertools import product
import math
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style
from name_print import name

class Card:
    def __init__(self,rank,suit,value) -> None:
        self.rank = rank
        self.suit = suit

    def print_cards(deck):
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

    def take_cards_from_deck(self,deck):
        if len(deck) < 6:
            for i in range(6 - len(deck) ):
                card = random.choice(self.game_deck.deck)
                self.game_deck.deck.remove(card)
                self.deck.append(card)
        return self.player_deck

class Player :
    def __init__(self,player_deck, game_deck):
        self.game_deck = game_deck
        self.player_deck = player_deck


    def take_cards_from_deck(self):
        if len(self.player_deck) < 6:
            for i in range(6 - len(self.player_deck)):
                card = random.choice(self.game_deck)
                self.game_deck.remove(card)
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

        # cprint(Style.BRIGHT + f'{self.first_name}','red','on_light_blue')
        name(self.first_name)
        Card.print_cards(first_deck)

        name(self.second_name)
        Card.print_cards(second_deck)
        name('cards in deck -->'),name(len(game_deck))
        
        # cprint(f'\ncards in deck -->{len(game_deck)}','cyan','on_green')

        while len(first_deck)!=0  or len(second_deck) !=0 and len(game_deck) != 0:     
            command = input("\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            if command not in ["a", "d", "t",'e']:
                print('\nwrong command')

            elif command == 'a':
                try:
                    card = int(input(f'\nchoose card to attack(1,2,3..): '))
                    att_card = first_deck.pop(card-1)
                    att_cards =[]
                    att_cards.append(att_card)
                    print(f'\n{self.first_name}, attack -->'),Card.print_cards(att_cards)
                except IndexError:
                    print('card index out of range please write correct index of card! ')
                except ValueError:
                    print('card index out of range please write correct index of card!')
            # command = input("attack/defense/take-cards/end-choda: ")


            elif command == 'd':
                
                try:
                    card = int(input(f'\nchoose card to defense(1,2,3..): '))
                    def_card = second_deck.pop(card-1)
                    def_cards= []
                    def_cards.append(def_card)
                    # print(f'{self.second_name}, defense -->')
                    Card.print_cards(def_cards)
                    result = durak_ex.compare_cards(att_card,def_card)
                except IndexError:
                    print('card index out of range please write correct index of card!')
                except ValueError:
                    print('card index out of range please write correct index of card!')


                    
                while result != 2 and command != 't':
                    print('\nimposible')
                    second_deck.append(def_card)
                    Card.print_cards(second_deck)
                    try:
                        card = int(input(f'\nchoose card to defense(1,2,3..): '))
                        def_card = second_deck.pop(card-1)
                        result = durak_ex.compare_cards(att_card,def_card)
                        command = input("\nenter/take-cards to continue: ")
                    except ValueError:
                        print('card index out of range please write correct index of card!')


                if result  == 2:
                    print('\n',att_card, '<', def_card)
                    print('\n✔')
                

            if command == 't':
                try:
                    # cards = (att_card) or (att_card),(def_card)
                    buff = [(att_card),(def_card)]
                    # buff.append(cards)
                    for  i in buff:
                        second_deck.append(i)
                    print('\n')
                    Card.print_cards(first_deck)
                    print('\n')
                    Card.print_cards(second_deck)
                except UnboundLocalError: 
                    print('you cant do this')
                

            if command == 'e':
                # first_deck.remove(att_card)
                # second_deck.remove(def_card)
                # odboy.append(att_card,def_card)
                Player(first_deck,deck_instance.deck).take_cards_from_deck()
                Player(second_deck,deck_instance.deck).take_cards_from_deck()
                name(self.first_name)
                Card.print_cards(first_deck)
                name(self.second_name)
                Card.print_cards(second_deck)



            
odboy = []
deck_instance = Deck()
Durak(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
# Card(deck_instance.deck)