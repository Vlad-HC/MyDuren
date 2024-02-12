import random
from itertools import product

class Deck:
    def __init__(self):
        self.ranks_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
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

    def create_decks():
        ...


class Card :
    def __init__(self) -> None:
        pass
    
    def attack_card():
        ...
    
    def defense_card():
        ...


class Player :
    def __init__(self) -> None:
        pass

    def attack():
        ...

    def defense():
        ...    

    def take_cards():
        ...
        
    def take_cards_from_deck():
        ...
            

deck = Deck()
card1 = deck.deck[0]
print('---------------------------------')
print(card1)
card2 = deck.deck[1]
print(card2)
result = deck.compare_cards(card1, card2)
print(result)  # Виведе різницю значень карт 
