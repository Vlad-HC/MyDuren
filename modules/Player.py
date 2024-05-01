from modules.name_print import name,print_card_middle,print_cool_suit
from modules.Deck import Deck 
from modules.Card import Card
from playsound import playsound
from termcolor import colored, cprint
from colorama import Fore, Style
import random

class Player :
    def __init__(self,player_deck: list, game_deck: list):
        self.game_deck = game_deck
        self.player_deck = player_deck
        


    def take_cards_from_deck(self):
        if len(self.player_deck) < 6 and len(self.game_deck) != 0:
            ln = len(self.player_deck)
            for _ in range(6-ln):
                playsound('sounds/card_fr_deck.mp3')
            for i in range(6 - len(self.player_deck)):
                card = random.choice(self.game_deck)
                self.game_deck.remove(card)
                self.player_deck.append(card)
            return self.player_deck
            
        
    
    def throw_card(self,turn_cards:list):
        Card.print_cards(self.player_deck)
        att_card = None
        while att_card == None:
            try:
                card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to attack(1,2,3..): '))
                att_card = self.player_deck.pop(card-1)
            except (IndexError, ValueError):
                cprint('card index out of range please write correct index of card! ','red')
                continue
        att_cards =[att_card]
        result = None
        for i in turn_cards:
            result = deck_instance.compare_values_of_cards(att_card,i)
            if result == 0:
                break
        if result == 0 or len(turn_cards) == 0:
            turn_cards.append(att_card)
        playsound('sounds/cardsound.mp3')
        Card.print_cards(att_cards)
        return att_card
        
                        
    def attack(self,turn_cards:list):
        att_card = None
        Card.print_cards(self.player_deck)
        
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to attack(1,2,3..): '))
        
        att_card = self.player_deck.pop(card-1)
        att_cards =[att_card]
        playsound('sounds/cardsound.mp3')
        turn_cards.append(att_card)
        Card.print_cards(att_cards)
        return att_card
    
    def defense(self,turn_cards:list):
        def_card = None
        Card.print_cards(self.player_deck)
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to defense(1,2,3..): '))
        def_card = self.player_deck.pop(card-1)
        def_cards= [def_card]
        playsound('sounds/cardsound.mp3')
        turn_cards.append(def_card)
        Card.print_cards(def_cards)
        return def_card
    
    def result(att_card,def_card):
        return deck_instance.compare_cards(att_card,def_card)
    
deck_instance = Deck()
