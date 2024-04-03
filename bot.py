import random

class BotDanil:
    def __init__(self,player_deck:list) -> None:
        names = ['Danyl','Filip','Bartosz','Dima','Monika','Kateryna']
        self.name = random.choice(names)
        self.player_deck = player_deck
    
    def bot_attack(self):
        att_card = None
        att_card = random.choice(self.player_deck)
        att_cards = [att_card]
        Card.print_cards(att_cards)
        return att_card
    
    def bot_defense(self):
        def_card = None
        def_card = random.choice(self.player_deck)
        def_cards= [def_card]
        Card.print_cards(def_cards)
        return def_card