from modules.Card import Card
from modules.Deck import Deck
from playsound import playsound
import time
import random

class BotDanil:
    def __init__(self,player_deck:list) -> None:
        names = ['Danil','Filip','Bartosz','Dima','Monika','Kateryna']
        self.name = random.choice(names)
        self.player_deck = player_deck
    
    def bot_attack(self,turn_cards:list):
        att_card = None
        choice = deck_instance.min_card(self.player_deck)
        card = self.player_deck.index(choice)
        att_card = self.player_deck.pop(card)
        att_cards = [att_card]
        turn_cards.append(att_card)
        print('\n')
        playsound('sounds/cardsound.mp3')
        Card.print_cards(att_cards)
        time.sleep(1)
        return att_card
    
    def bot_defense(self,att_card,turn_cards:list):
        def_card = None
        choices = []
        card = None
        for i in range(0,len(self.player_deck)):
            result = deck_instance.compare_cards(self.player_deck[i],att_card)
            if result == 1:
                choice = self.player_deck[i]
                choices.append(choice)
                choice = deck_instance.min_card(choices)
        try:
            card = self.player_deck.index(choice)
            def_card = self.player_deck.pop(card)
            def_cards = [def_card]
        except UnboundLocalError: 
            rndcrd = random.choice(self.player_deck)
            def_card = rndcrd
            def_cards=[rndcrd]
        print('\n')
        playsound('sounds/cardsound.mp3')
        turn_cards.append(def_card)
        Card.print_cards(def_cards)
        time.sleep(1)
        return def_card
    
deck_instance = Deck()
