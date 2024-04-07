from name_print_w10 import name,print_card_middle,print_cool_suit

class Card:
    def __init__(self,rank,suit,value) -> None:
        self.rank = rank
        self.suit = suit

    def print_cards(deck):
        # Create six cards
        cards = [Card(rank, suit, value) for rank, suit, value in deck]
        # Print the cards in a row
        for card in cards:print(f' _____   ',end='')
        print()

        for card in cards:
            if card.rank=='10':
                print(f'|   {card.rank}|  ',end='')
            else:
                print(f'|    {card.rank}|  ',end='')
        print()

        for card in cards:print('|     |  ', end='')
        print()

        for card in cards:
            print_card_middle(card.suit)
        print()

        for card in cards:print('|     |  ', end='')
        print() 
        for card in cards:
            if card.rank == '10':
                print(f'|{card.rank}   |  ',end='')
            else:
                print(f'|{card.rank}    |  ',end='')
        print()

        for card in cards:print(' ‾‾‾‾‾   ',end='')
