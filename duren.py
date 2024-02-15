import random
from itertools import product
import math


class Card :
    def __init__(self) :
        pass
    
    def attack_card():
        ...
    
    def defense_card():
        ...



class Deck:
    deck: list[tuple[str,str,int]]
    
    def __init__(self):
        self.ranks_values = {
            '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }
        suits = ['♥', '♦️', '♣️', '♠️']
        ranks = list(self.ranks_values.keys())


        self.deck = [(rank, suit, self.ranks_values[rank]) for rank, suit in product(ranks, suits)]
        random.shuffle(self.deck)
        

    def compare_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2

        if suit1 == suit2:
            if value1 > value2 :
                return value1 - value2, '<-- різниця  карта n1 більше'
            if value2 > value1:
                return value2 - value1, '<-- різниця карта n2 більше'
        elif suit1 != suit2:
            return 'масті не співпадають'
            
        elif  value1 == 2 and value2 == 14:  # Якщо значення першої карти на 1 більше за значення другої
            return '1 карта більше'  # Перша карта перемагає
        else:
            return '2 карта більше'  # Друга карта перемагає
    def create_deck_for_player(self): # <-- create deck for player 
        player_deck = []
        for i in range(4):
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
    def __init__(self) -> None:
        pass



    def compare_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2

        if suit1 == suit2:
            if value1 > value2 :
                return value1 - value2, '<-- різниця  карта n1 більше'
            if value2 > value1:
                return value2 - value1, '<-- різниця карта n2 більше'
        elif suit1 != suit2:
            return 'масті не співпадають'
            
        elif  value1 == 2 and value2 == 14:  # Якщо значення першої карти на 1 більше за значення другої
            return '1 карта більше'  # Перша карта перемагає
        else:
            return '2 карта більше'  # Друга карта перемагає

# card1 = deck.deck[0]
# print('---------------------------------')
# print(card1)
# card2 = deck.deck[1]
# print(card2)
# result = deck.compare_cards(card1, card2)
# print(result)  # Виведе різницю значень карт 

# deck.create_decks() <-- stworue kolodu dla grawcia 
# print(deck.deck)
deck_instance = Deck()
for i in  range(10):
    Player('Vlad', deck_instance)
   
