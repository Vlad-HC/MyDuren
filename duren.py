import random
from itertools import product
import math
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style
from name_print import name

def print_card_middle(symbol, color):
    cprint(Style.BRIGHT + f'|  ', 'black', 'on_light_magenta',end='')
    cprint(Style.BRIGHT + symbol, color ,'on_light_magenta',end='')
    cprint(Style.BRIGHT + f'  |  ', 'black', 'on_light_magenta',end='')
        
        
        
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
            print_card_middle(card.suit, suit_color)
            # cprint(Style.BRIGHT + f'|  {card.suit}  |  ', suit_color ,'on_light_magenta',end='')
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
        cool_suit = random.choice(suits)

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

    def take_cards_from_deck(self,deck:list):
        if len(deck) < 6:
            for i in range(6 - len(deck) ):
                card = random.choice(self.game_deck.deck)
                self.game_deck.deck.remove(card)
                self.deck.append(card)
        return self.player_deck

class Player :
    def __init__(self,player_deck: list, game_deck: list):
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
        att_card = None
        Card.print_cards(self.player_deck)
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to attack(1,2,3..): '))
        att_card = self.player_deck.pop(card-1)
        att_cards =[att_card]
        Card.print_cards(att_cards)
        return att_card
    
    def defense(self):
        def_card = None
        Card.print_cards(self.player_deck)
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to defense(1,2,3..): '))
        def_card = self.player_deck.pop(card-1)
        def_cards= [def_card]
        Card.print_cards(def_cards)
        return def_card
    
    def result(att_card,def_card):
        result = None
        result = deck_instance.compare_cards(att_card,def_card)
        return result
    
class Durak:

    def __init__(self,first_deck: list, second_deck: list, game_deck: list ,deck_ex: Deck):
        self.game_deck = game_deck
        self.first_deck = first_deck
        self.second_deck = second_deck
        self.first_name = input(Fore.BLUE + 'write your name: ')
        self.second_name = input(Fore.BLUE + 'write your name: ')
        self.deck_ex = deck_ex
        self.players = [self.first_name, self.second_name]
        self.odboy = []
        att_quantity = []
        name(self.first_name)
        Card.print_cards(first_deck)

        name(self.second_name)
        Card.print_cards(second_deck)
        name('cards in deck -->'),name(len(game_deck))
        att_card = None
        def_card = None

        while len(first_deck)!=0  or len(second_deck) !=0 and len(game_deck) != 0:     
            command = input(Style.BRIGHT+ Fore.CYAN + "\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            if command not in ["a", "d", "t",'e']:
                cprint('\nwrong command','red')

            if command == 'a':
                try:
                    att_quantity.append(1)
                    if len(att_quantity)%2 == 1:    
                        att_card = Player(first_deck,game_deck).attack()
                    else:
                        att_card = Player(second_deck,game_deck).attack()

                except IndexError:
                    cprint('card index out of range please write correct index of card! ','red')
                    att_quantity.append(1)
                except ValueError:
                    cprint('card index out of range please write correct index of card!','red')
                    att_quantity.append(1)


            elif command == 'd':
                if att_card == None:
                    print('You cant do this')
                    continue

                try:
                    def_card = Player(second_deck, game_deck).defense()
                    result = self.result(att_card,def_card)
                except (IndexError,ValueError):
                    cprint('card index out of range please write correct index of card!','red')
                    continue

                    
                while result != 2 and command != 't':
                    cprint('\nimposible',"red")
                    second_deck.append(def_card)
                    Card.print_cards(second_deck)
                    try:
                        card = int(input(f'\nchoose card to defense(1,2,3..): '))
                        def_card = second_deck.pop(card-1)
                        result = deck_ex.compare_cards(att_card,def_card)
                        command = input("\nenter/take-cards to continue: ")
                    except ValueError:
                        cprint('card index out of range please write correct index of card!','red')
                        continue

                if result  == 2:
                    print('\n',att_card, '<', def_card)
                    cprint('  ✔  ','light_green','on_green')
                    att_card=None
                    def_card=None
                    

            if command == 't':
                
                if  att_card == None :
                    print('you cant do this')
                    continue
                if def_card == None:
                    if att_card != None:
                        buff = [(att_card)]
                else:
                    buff = [(att_card),(def_card)]
                for  i in buff:
                    if len(att_quantity)%2 == 1:
                        second_deck.append(i)
                    else:
                        first_deck.append(i)
                print('\n')
                Card.print_cards(first_deck)
                print('\n')
                Card.print_cards(second_deck)
                att_card = None
                def_card= None
    
            if command == 'e':
                if att_card != None:
                    cprint("You cant do this",'red')
                    continue
                else:
                    Player(first_deck,deck_instance.deck).take_cards_from_deck()
                    Player(second_deck,deck_instance.deck).take_cards_from_deck()
                    name(self.first_name)
                    Card.print_cards(first_deck)
                    name(self.second_name)
                    Card.print_cards(second_deck)
                    att_card = None
                    def_card = None
    @staticmethod
    def result(att_card,def_card):
        result = None
        result = deck_instance.compare_cards(att_card,def_card)
        return result

odboy = []
deck_instance = Deck()
Durak(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
