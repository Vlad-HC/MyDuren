from name_print import name,print_card_middle,print_cool_suit
from termcolor import colored, cprint
from colorama import Fore, Style
from playsound import playsound
from itertools import product
from Card import Card
import os, time
import random



class BotDanil:
    def __init__(self,player_deck:list) -> None:
        names = ['Danil','Filip','Bartosz','Dima','Monika','Kateryna']
        self.name = random.choice(names)
        self.player_deck = player_deck
    
    def bot_attack(self):
        att_card = None
        choice = deck_instance.min_card(self.player_deck)
        card = self.player_deck.index(choice)
        att_card = self.player_deck.pop(card)
        att_cards = [att_card]
        print('\n')
        playsound('sounds/cardsound.mp3')
        Card.print_cards(att_cards)
        time.sleep(1)
        return att_card
    
    def bot_defense(self,att_card):
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
            def_cards= [def_card]
        except UnboundLocalError: 
            rndcrd = random.choice(self.player_deck)
            def_card = rndcrd
            def_cards=[rndcrd]
        print('\n')
        playsound('sounds/cardsound.mp3')
        Card.print_cards(def_cards)
        time.sleep(1)
        return def_card
   


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
        self.cool_suit = random.choice(suits)

    def compare_cards(self, card1, card2):
        _, suit1, value1 = card1
        _, suit2, value2 = card2
        if suit1  == self.cool_suit and suit1!=suit2:
            return 1

        if suit2 == self.cool_suit and suit1!=suit2:
            return 2         

        if suit1== self.cool_suit and suit2 == self.cool_suit:
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
        
#some logic for bot

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


class Player :
    def __init__(self,player_deck: list, game_deck: list):
        self.game_deck = game_deck
        self.player_deck = player_deck
        


    def take_cards_from_deck(self):
        if len(self.player_deck) < 6 and len(self.game_deck) != 0:
            for i in range(6 - len(self.player_deck)):
                card = random.choice(self.game_deck)
                self.game_deck.remove(card)
                ln = len(self.player_deck)
                self.player_deck.append(card)
                
                for i in range(6-ln):
                    playsound('sounds/card_fr_deck.mp3')
            return self.player_deck
        
    
    def throw_card(self):
        att_card = None
        Card.print_cards(self.player_deck)
        while att_card == None:
            try:
                card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to attack(1,2,3..): '))
                att_card = self.player_deck.pop(card-1)
            except (IndexError, ValueError):
                cprint('card index out of range please write correct index of card! ','red')
                continue
        att_cards =[att_card]
        playsound('sounds/cardsound.mp3')
        Card.print_cards(att_cards)
        return att_card
        
                        
    def attack(self):
        att_card = None
        Card.print_cards(self.player_deck)
        
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to attack(1,2,3..): '))
        
        att_card = self.player_deck.pop(card-1)
        att_cards =[att_card]
        playsound('sounds/cardsound.mp3')
        Card.print_cards(att_cards)
        return att_card
    
    def defense(self):
        def_card = None
        Card.print_cards(self.player_deck)
        card = int(input(Style.BRIGHT+ Fore.GREEN + f'\nchoose card to defense(1,2,3..): '))
        def_card = self.player_deck.pop(card-1)
        def_cards= [def_card]
        playsound('sounds/cardsound.mp3')
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
        os.system("cls")
        self.choice = input(Fore.BLUE + '\n1 - play with bot or 2 - play with friend :')
        self.first_name = input(Fore.BLUE + 'write your name: ')
        if self.choice == '1':
            self.second_name = BotDanil(second_deck).name
        else:
            self.second_name = input(Fore.BLUE + 'write your name: ')

        self.deck_ex = deck_ex
        self.players = [self.first_name, self.second_name]
        att_quantity = 0
        subcommand = str
        turn_cards = []
        name(self.first_name)
        Card.print_cards(first_deck)

        if self.choice == '1':
            name(self.second_name)
            name(f'cards in opponent deck --> {len(second_deck)}')
        else:
            name(self.second_name)
            Card.print_cards(second_deck)
        name(f'cards in game deck --> {len(game_deck)}')
        print_cool_suit(deck_instance.cool_suit)
        att_card = None
        def_card = None

        
        while (len(first_deck)!=0  and len(second_deck)!=0) or len(game_deck) != 0:


            if att_quantity % 2 == 1:
                cprint(f'\n{self.second_name} turn', 'light_green')    
                command = input(Style.BRIGHT+ Fore.CYAN + "\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            else:
                cprint(f'\n{self.first_name} turn', 'light_green')    
                command = input(Style.BRIGHT+ Fore.CYAN + "\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            if command not in ["a", "d", "t",'e','q',')']:
                cprint('\nwrong command','red')
                
            if self.choice == '2':#<--------------------------------------------------------------
                if command == 'a':
                    try:
                        if att_card != None:
                            cprint('You cant do this' ,'red')
                            continue
                        att_quantity = att_quantity + 1
                        if att_quantity % 2 == 1: att_card = Player(first_deck,game_deck).attack() 
                        else: att_card = Player(second_deck,game_deck).attack()

                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card! ','red')
                        att_quantity = att_quantity + 1

                elif command == 'd':
                    if att_card == None:
                        cprint('You cant do this','red')
                        continue
                    try:
                        if att_quantity % 2 == 1: def_card = Player(second_deck, game_deck).defense()
                        else: def_card = Player(first_deck, game_deck).defense()

                        result = self.result(att_card,def_card)
                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card!','red')
                        continue

                    while result != 2 and command != 't':
                        cprint('\nimposible',"red")
                        command = input("\nenter to continue/take-cards(t) : ")
                        if att_quantity % 2 == 1:
                            if def_card not in second_deck:second_deck.append(def_card)
                            Card.print_cards(second_deck)
                        else:
                            if def_card not in first_deck:first_deck.append(def_card)
                            Card.print_cards(first_deck)
                        if command!='t':
                            try:
                                card = int(input(f'\nchoose card to defense(1,2,3..): '))
                                def_card = second_deck.pop(card-1)
                                result = deck_ex.compare_cards(att_card,def_card)
                            except ValueError:
                                cprint('card index out of range please write correct index of card!','red')
                                continue

                    while result  == 2 and command != 'e' and command != 't':
                        print('\n')
                        cprint('  ✔  ','light_green','on_green')
                        odboy.append(att_card)
                        odboy.append(def_card)
                        if att_card != None and att_card not in turn_cards:
                            turn_cards.append(att_card)
                        if def_card != None and def_card not in turn_cards: 
                            turn_cards.append(def_card)

                        att_card = None
                        def_card = None
                        result = None
                        subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nthrow more card <<c>>/end turn <<e>>: ")
                        while subcommand not in ['e','c']:
                            cprint('\nwrong command','red')
                            subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nthrow more card <<c>>/end turn <<e>>: ")
                            continue
                        if subcommand == 'c': 
                            try:
                                if att_quantity % 2 == 1:  att_card = Player(first_deck, game_deck).throw_card()
                                else: att_card = Player(first_deck, game_deck).throw_card()
                                possibility = None
                                while possibility != 0:
                                    for i in turn_cards:
                                        result = deck_instance.compare_values_of_cards(att_card,i)
                                        if result == 0: possibility = 0 
                                           

                                    while possibility != 0 and subcommand != 'e':
                                        cprint('\nYou cant do this' ,'red')
                                        if att_quantity % 2 == 1 and att_card not in first_deck: first_deck.append(att_card)
                                        elif att_quantity % 2 != 1 and att_card not in second_deck: second_deck.append(att_card)
                                        subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nthrow more card <<c>>/end turn <<e>>: ")
                                        if subcommand != 'e': att_card = Player(first_deck, game_deck).throw_card()

                                if result != 2:    
                                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")

                                while subcommand_ not in ['d','t']:
                                    cprint('\nwrong command','red')
                                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")
                                    continue

                                if subcommand_ == 'd':
                                    while result != 2 and command != 't': 
                                        print('\n')
                                        if att_quantity % 2 == 1:
                                            if def_card != None:second_deck.append(def_card)
                                            def_card = Player(second_deck, game_deck).defense()
                                        else:
                                            if def_card != None:first_deck.append(def_card)
                                            def_card = Player(first_deck, game_deck).defense()
                                        if result != 2:
                                            subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")
                                        while subcommand_ not in ['d','t']:
                                            cprint('\nwrong command','red')
                                            subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")

                                            
                                        if subcommand_ == 't':command = 't'

                                        result = self.result(att_card,def_card)

                                if subcommand_ == 't':
                                    command = 't'

                            except (IndexError,ValueError):
                                cprint('card index out of range please write correct index of card!','red')
                                continue


                        if att_card != None and att_card not in turn_cards: turn_cards.append(att_card)
                            
                        if def_card != None and def_card not in turn_cards: turn_cards.append(def_card)

                        elif subcommand == 'e': command = 'e'
                        else: cprint('\nwrong command','red')
                        
                if command == 't':
                    buff = []
                    if  att_card == None :
                        print('you cant do this')
                        continue

                    if def_card == None:
                        if att_card != None and subcommand not in ['e','c']:
                            buff = [(att_card)]
                    else:
                        buff = [(att_card),(def_card)]

                    if subcommand != None:
                        for n in turn_cards:
                            buff.append(n)

                    for  i in buff:
                        if att_quantity % 2 == 1:
                            second_deck.append(i)

                        else: first_deck.append(i)

                    att_quantity = att_quantity + 1 
                    att_card = None
                    def_card= None
                    command = 'e'

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
                        print_cool_suit(deck_instance.cool_suit)
                        att_card = None
                        def_card = None































                        
            if self.choice == '1':#<--------------------------------------------------------------------------
                if att_quantity % 2 == 1 and att_card == None: command = 'a'
                if command == 'a':
                    try:
                        if att_card != None:
                            cprint('You cant do this' ,'red')
                            continue
                        att_quantity = att_quantity + 1
                        if att_quantity % 2 == 1: att_card = Player(first_deck,game_deck).attack()   
                        else:
                            time.sleep(1)
                            att_card = BotDanil(second_deck).bot_attack()

                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card! ','red')
                        att_quantity = att_quantity + 1

                if att_quantity % 2 == 1 and att_card != None: command = 'd'
                if command == 'd':
                    if att_card == None:
                        cprint('You cant do this','red')
                        continue

                    try:
                        if att_quantity % 2 == 1:
                            time.sleep(1)
                            def_card = BotDanil(second_deck).bot_defense(att_card)
                            
                        else: def_card = Player(first_deck, game_deck).defense()
                            
                        result = self.result(att_card,def_card)
                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card!','red')
                        continue


                    while result != 2 and command != 't':
                        cprint('\nimposible',"red")
                        if att_quantity % 2 != 1:
                            command = input("\nenter to continue/take-cards(t) : ")

                            if def_card not in first_deck:
                                first_deck.append(def_card)
                        else : command = 't'

                        if command!='t':
                            try:
                                
                                Card.print_cards(first_deck)
                                card = int(input(f'\nchoose card to defense(1,2,3..): '))
                                def_card = first_deck.pop(card-1)
                                result = deck_ex.compare_cards(att_card,def_card)
                            except ValueError:
                                cprint('card index out of range please write correct index of card!','red')
                                continue

                    if result  == 2:
                        print('\n')
                        cprint('  ✔  ','light_green','on_green')
                        odboy.append(att_card)
                        odboy.append(def_card)
                        att_card=None
                        def_card=None
                        command = 'e'
                        
                if command == 't':
                    
                    if  att_card == None :
                        print('you cant do this')
                        continue
                    if def_card == None:
                        if att_card != None:
                            buff = [(att_card)]
                    elif (def_card not in second_deck) or (def_card not  in first_deck):
                        buff = [(att_card),(def_card)]
                    elif def_card in first_deck:
                        buff = [(att_card)]
                        
                    else:
                        buff = [(att_card)]
                    
                    for  i in buff:
                        if att_quantity % 2 == 1:
                            if i not in second_deck:
                                second_deck.append(i)
                        else:
                            if i not in first_deck:
                                first_deck.append(i)
                    att_quantity = att_quantity + 1 
                    att_card = None
                    def_card= None
                    command = 'e'

                if command == 'e':
                    if att_card != None:
                        cprint("You cant do this",'red')
                        continue
                    else:
                        time.sleep(1)
                        os.system("cls")
                        Player(first_deck,deck_instance.deck).take_cards_from_deck()
                        Player(second_deck,deck_instance.deck).take_cards_from_deck()
                        name(self.first_name)
                        Card.print_cards(first_deck)
                        time.sleep(1)
                        name(self.second_name)
                        name(f'cards in opponent deck --> {len(second_deck)}')
                        name(f'cards in game deck --> {len(game_deck)}')
                        print_cool_suit(deck_instance.cool_suit)
                        att_card = None
                        def_card = None
                        att_quantity % 2 == 1
            if command == 'q':
                print('GG')
                os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                quit()                
            if command == ')':
                os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                name(':3 Never Gonna Give You Up :3')
        if len(first_deck) == 0:
            name(f'\nwinner -------> {self.first_name}')
        elif len(second_deck) == 0:
            name(f'\nwinner -------> {self.second_name}')
    @staticmethod
    def result(att_card,def_card):
        result = None
        result = deck_instance.compare_cards(att_card,def_card)
        return result

odboy = []
deck_instance = Deck()
Durak_instance = Durak(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
bot_instance = BotDanil(Durak_instance.second_deck)