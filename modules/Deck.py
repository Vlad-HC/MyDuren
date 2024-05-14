import random
from itertools import product
class Deck:
    deck: list[tuple[str,str,int]]
    
    def __init__(self):
        self.ranks_values = {
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        suits = ['♥', '♦', '♣', '♠']
        ranks = list(self.ranks_values)

        self.deck = [(rank, suit, self.ranks_values[rank]) for rank, suit in product(ranks, suits)]
        random.shuffle(self.deck)
        self.last_card = self.deck[-1]
        self.rank_of_last_card = self.last_card[0]
        self.cool_suit = self.last_card[1]

    def compare_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2
        if suit1  == self.cool_suit and suit1!=suit2:
            return 1

        if suit2 == self.cool_suit and suit1!=suit2:
            return 2         

        if suit1 == self.cool_suit and suit2 == self.cool_suit:
            if value1 > value2:
                return 1
            if value2 > value1:
                return 2
            else:
                return 0    
        if suit1 == suit2:
            if value1 > value2:
                return 1
            if value2 > value1:
                return 2
        
        return 0
    

    def compare_values_of_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2
        if value1 < value2:
            return 1
        if value2 < value1:
            return 2
        if value1 == value2:
            return 0
        

    def min_card(self,player_deck:list):
        choice = player_deck[0]
        for i in range(0,len(player_deck)):
            result = deck_instance.compare_values_of_cards(player_deck[i], choice)
            if result == 1:
                choice = player_deck[i]       
        return choice


    def create_deck_for_player(self): # <-- create deck for player 
        player_deck = []
        for i in range(6):
            random_card = random.choice(self.deck)
            self.deck.remove(random_card)
            player_deck.append(random_card)
        return player_deck
    
    def is_it_cool_suit(self,suit):
        if self.cool_suit == suit:
            return 0
        return 1


    def card_suit(card):
        for i in card:
            if i in ['♥', '♦', '♣', '♠']:
                suit = i
        return suit
    
deck_instance = Deck()


