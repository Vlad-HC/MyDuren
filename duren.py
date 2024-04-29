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
    
    def is_it_cool_suit(self,suit):
        if self.cool_suit == suit:
            return 0
        return 1


    def card_suit(card):
        for i in card:
            if i in ['♥', '♦', '♣', '♠']:
                suit = i
        return suit

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
        self.att_quantity = 0
        subcommand = str
        self.turn_cards = []
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


            if self.att_quantity % 2 == 1:
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
                        self.att_quantity += 1
                        att_card = self.get_player().attack(self.turn_cards) 

                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card! ','red')
                        self.att_quantity -= 1

                elif command == 'd':
                    if att_card == None:
                        cprint('You cant do this','red')
                        continue
                    try:
                        def_card = self.get_player_for_defense().defense(self.turn_cards)
                        result = self.result(att_card,def_card)
                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card!','red')
                        continue

                    while result != 2 and command != 't':
                        cprint('\nimposible',"red")
                        command = input("\nenter to continue/take-cards(t) : ")

                        if self.att_quantity % 2 == 1:
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
                        if att_card != None and att_card not in self.turn_cards:
                            self.turn_cards.append(att_card)
                        if def_card != None and def_card not in self.turn_cards: 
                            self.turn_cards.append(def_card)

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
                                subcommand_ = None   
                                att_card = self.get_player().throw_card(self.turn_cards)
                                possibility = None
                                while possibility != 0 and command != 'e':
                                    result = self.check_posibility_for_flip(att_card)
                                    if result == 0: possibility = 0 
                                           

                                    while possibility != 0 and subcommand != 'e':
                                        cprint('\nYou cant do this' ,'red')
                                        if self.att_quantity % 2 == 1 and att_card not in first_deck: first_deck.append(att_card)
                                        elif self.att_quantity % 2 != 1 and att_card not in second_deck: second_deck.append(att_card)
                                        subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nthrow more card <<c>>/end turn <<e>>: ")

                                        if subcommand != 'e': att_card = Player(first_deck, game_deck).throw_card(self.turn_cards)
                                        elif subcommand == 'e': 
                                            command = 'e'
                                            att_card = None

                                if result != 2 and command != 'e': 
                                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")

                                while subcommand_ not in ['d','t'] and command != 'e':
                                    cprint('\nwrong command','red')
                                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")
                                    continue

                                if subcommand_ == 'd':
                                    while result != 2 and command != 't': 
                                        print('\n')
                                        if self.att_quantity % 2 == 1:
                                            if def_card != None:second_deck.append(def_card)
                                            def_card = self.get_player_for_defense().defense(self.turn_cards)
                                        else:
                                            if def_card != None:first_deck.append(def_card)
                                            def_card = self.get_player_for_defense().defense(self.turn_cards)
                                        result = self.result(att_card,def_card)
                                            
                                        if result != 2:
                                            subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")
                                        while subcommand_ not in ['d','t']:
                                            cprint('\nwrong command','red')
                                            subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")

                                            
                                        if subcommand_ == 't':command = 't'


                                if subcommand_ == 't':
                                    command = 't'

                            except (IndexError,ValueError):
                                cprint('card index out of range please write correct index of card!','red')
                                continue


                        if att_card != None and att_card not in self.turn_cards: self.turn_cards.append(att_card)
                            
                        if def_card != None and def_card not in self.turn_cards: self.turn_cards.append(def_card)

                        if subcommand_ == 'e': command = 'e'
                        elif subcommand_ not in ['e','t']: cprint('\nwrong command','red')
                         
                if command == 't':
                    buff = []
                    if  att_card == None and subcommand!='e':
                        print('you cant do this')
                        continue
                    
                    att_card = None
                    result = None 
                    while subcommand != 'e':
                        subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nthrow more card <<c>>/end turn <<e>>: ")
                        if subcommand != 'e':
                            att_card = self.get_player().throw_card(self.turn_cards)
                            if att_card not in self.turn_cards:self.turn_cards.append(att_card)
                            result = self.check_posibility_for_flip(att_card)

                            if result != 0: 
                                ind = self.turn_cards.index(att_card)
                                self.turn_cards.pop(ind)
                                if self.att_quantity % 2 == 1 and att_card not in first_deck: first_deck.append(att_card)
                                elif self.att_quantity % 2 != 1 and att_card not in second_deck: second_deck.append(att_card)

                    # if att_card != None and subcommand == 'e':
                    #     for i in self.turn_cards:
                    #         buff.append(i)
                            # buff = [(self.turn_cards)]

                    if subcommand != None:
                        for n in self.turn_cards:
                            buff.append(n)
                    else:
                        buff = [(att_card),(def_card)]

                    for  i in buff:
                        if self.att_quantity % 2 == 1:
                            if i not in second_deck:
                                second_deck.append(i)
                        else: 
                            if i not in first_deck:
                                first_deck.append(i)

                    self.att_quantity += 1 
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
                        self.turn_cards = []































                        
            if self.choice == '1':#<--------------------------------------------------------------------------
                if self.att_quantity % 2 == 1 and att_card == None: command = 'a'
                if command == 'a':
                    try:
                        if att_card != None:
                            cprint('You cant do this' ,'red')
                            continue
                        self.att_quantity += 1
                        if self.att_quantity % 2 == 1: att_card = Player(first_deck,game_deck).attack(self.turn_cards)   
                        else:
                            time.sleep(1)
                            att_card = BotDanil(second_deck).bot_attack(att_card)
                            
                            

                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card! ','red')
                        self.att_quantity -= 1

                if self.att_quantity % 2 == 1 and att_card != None: command = 'd'
                if command == 'd':
                    if att_card == None:
                        cprint('You cant do this','red')
                        continue

                    try:
                        if self.att_quantity % 2 != 1:
                            def_card = BotDanil(second_deck).bot_defense(att_card)
                        else: def_card = Player(first_deck,game_deck).defense(att_card)
                            
                            
                        result = self.result(att_card,def_card)
                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card!','red')
                        continue


                    while result != 2 and command != 't':
                        cprint('\nimposible',"red")
                        if self.att_quantity % 2 != 1:
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
                        if self.att_quantity % 2 == 1:
                            if i not in second_deck:
                                second_deck.append(i)
                        else:
                            if i not in first_deck:
                                first_deck.append(i)
                    self.att_quantity += 1 
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
                        self.att_quantity % 2 == 1
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
        return deck_instance.compare_cards(att_card,def_card)

    def get_player(self):
        return Player(self.first_deck if self.att_quantity % 2 else self.second_deck, self.game_deck)
    
    def get_player_for_defense(self):
        return Player(self.second_deck if self.att_quantity % 2 else self.first_deck, self.game_deck)
    
    # def get_player_or_bot(self):
    #     if self.att_quantity % 2 == 1:return Player(self.first_deck,self.game_deck)
    #     else: BotDanil(self.second_deck)

    # def get_player_or_bot_defense(self):
    #     if self.att_quantity % 2 != 1:return Player(self.first_deck,self.game_deck)
    #     else: return BotDanil(self.second_deck)

    def check_posibility_for_flip(self, att_card):
        for i in self.turn_cards:
            result = deck_instance.compare_values_of_cards(att_card,i)
        return result
odboy = []
deck_instance = Deck()
Durak_instance = Durak(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
bot_instance = BotDanil(Durak_instance.second_deck)