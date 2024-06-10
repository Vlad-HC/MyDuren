from modules.name_print import name,print_card_middle,print_cool_suit
from termcolor import colored, cprint
from colorama import Fore, Style
from playsound import playsound
from modules.Card import Card
from modules.Deck import Deck,deck_instance
from modules.Player import Player
from modules.Bot import BotDanil
import os, time

   
class Duren:

    def __init__(self,first_deck: list, second_deck: list, game_deck: list ,deck_ex: Deck):
        self.game_deck = game_deck
        self.first_deck = first_deck
        self.second_deck = second_deck
        self.odboy = []
        os.system("cls")
        self.last_card = deck_instance.last_card
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

        if self.choice == '1':
            name(self.first_name)
            Card.print_cards(first_deck)
            name(self.second_name)
            name(f'cards in opponent deck --> {len(second_deck)}')
            print_cool_suit(deck_instance.cool_suit)
        else:
            self.information()
        att_card = None
        def_card = None
        
        while (len(first_deck)!=0  and len(second_deck)!=0) or len(game_deck) != 0:


            if self.att_quantity % 2 == 1:
                cprint(f'\n{self.second_name} turn', 'light_green')    
                command = input(Style.BRIGHT+ Fore.CYAN + "\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            else:
                cprint(f'\n{self.first_name} turn', 'light_green')    
                command = input(Style.BRIGHT+ Fore.CYAN + "\nattack(a)/defense(d)/take-cards(t)/end_of_turn(e): ")
            if command not in ["a", "d", "t",'e','q',')','s']:
                cprint('\nwrong command','red')
                
            if self.choice == '2':#<--------------------------------------------------------------
                
                if command == 's':
                    self.att_quantity += 1
                    cprint('deck sorted', 'green')
                    print('\n')
                    self.get_player().player_deck = self.sort_deck()
                    os.system('cls')
                    self.information()
                    self.att_quantity -= 1
                    

                if command == 'a':
                    try:
                        if att_card != None:
                            cprint('You cant do this' ,'red')
                            continue
                        att_card = self.turn_attack()
                    except (IndexError,ValueError):
                        cprint('card index out of range please write correct index of card! ','red')

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
                        ind = self.turn_cards.index(def_card)
                        self.turn_cards.pop(ind)
                        if self.att_quantity % 2 == 1:
                            if def_card not in second_deck:second_deck.append(def_card)
                        else:
                            if def_card not in first_deck:first_deck.append(def_card)
                            
                        if command != 't':
                            try:
                                if self.att_quantity % 2 == 1:
                                    Card.print_cards(second_deck)
                                else:
                                    Card.print_cards(first_deck)
                                card = int(input(f'\nchoose card to defense(1,2,3..): '))
                                def_card = second_deck.pop(card-1)
                                result = deck_ex.compare_cards(att_card,def_card)
                                self.turn_cards.append(def_card)
                            except ValueError:
                                cprint('card index out of range please write correct index of card!','red')
                                continue

                    while result  == 2 and command != 'e' and command != 't':
                        self.correct_card()
                        

                        att_card = None
                        def_card = None
                        result = None
                        subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nflip more card <<c>>/end turn <<e>>: ")

                        while subcommand not in ['e','c']:
                            cprint('\nwrong command','red')
                            subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nflip more card <<c>>/end turn <<e>>: ")
                            continue
                        

                        if subcommand == 'c': 
                            try:
                                
                                self.turn_flip_card(command)
                            except (IndexError,ValueError):
                                cprint('card index out of range please write correct index of card!','red')
                                continue


                        if att_card != None and att_card not in self.turn_cards: self.turn_cards.append(att_card)
                            
                        if def_card != None and def_card not in self.turn_cards: self.turn_cards.append(def_card)

                        if subcommand == 'e': command = 'e'
                        # elif subcommand_ not in ['e','t']: cprint('\nwrong command','red')
                         
                if command == 't':
                    if  att_card == None and subcommand!='e':
                        cprint('you cant do this','red')
                        continue
                    
                    att_card = None
                    result = None 
                    self.turn_take_cards(def_card,subcommand)
                    self.att_quantity += 1 
                    att_card = None
                    def_card= None
                    command = 'e'

                if command == 'e':
                    if att_card != None:
                        cprint("You cant do this",'red')
                    else:
                        self.end_of_turn(att_card)
                        self.turn_cards = []
                        att_card = None
                        def_card = None
                        subcommand = None
                        subcommand_ = None



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
                            att_card = BotDanil(second_deck).bot_attack(att_card,self.turn_cards)
                            
                            

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
                            def_card = Player(first_deck,game_deck).defense(self.turn_cards) 
                        else: def_card = BotDanil(second_deck).bot_defense(att_card,self.turn_cards)
                            
                            
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
                        self.correct_card()
                        att_card=None
                        def_card=None
                        command = 'e'
                        
                if command == 't':
                    self.turn_take_cards(def_card,subcommand)
                    

                if command == 'e':
                    self.end_of_turn(att_card)


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

    # some funcitons for commands
    def turn_take_cards(self):
        if self.att_card != None:
            return

        print('you cant do this')
        if self.def_card == None:
            if self.att_card != None:
                buff = [(self.att_card)]
        elif (self.def_card not in self.second_deck) or (self.def_card not  in self.first_deck):
            buff = [(self.att_card),(self.def_card)]
        elif self.def_card in self.first_deck:
            buff = [(self.att_card)]                    
        else:
            buff = [(self.att_card)]
                
            for  i in buff:
                if self.att_quantity % 2 == 1:
                    if i not in self.second_deck:
                        self.second_deck.append(i)
                else:
                    if i not in self.first_deck:
                        self.first_deck.append(i)
            self.att_quantity += 1 
            self.att_card = None
            self.def_card= None
            command = 'e'

    def turn_attack(self):
            self.att_quantity += 1
            att_card = self.get_player().attack(self.turn_cards) 
            return att_card


    def information(self):
        name(self.first_name)
        Card.print_cards(self.first_deck)
        name(self.second_name)
        Card.print_cards(self.second_deck)
        name(f'cards in game deck --> {len(self.game_deck)}')
        Card.print_deck(self.last_card)

    def end_of_turn(self,att_card):
        time.sleep(1)
        os.system("cls")
        Player(self.first_deck,deck_instance.deck).take_cards_from_deck()
        Player(self.second_deck,deck_instance.deck).take_cards_from_deck()
        self.information()

    def turn_take_cards(self,def_card,subcommand):
        buff = []
        while subcommand != 'e':
            subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nflip more card <<c>>/end turn <<e>>: ")
            if subcommand != 'e':
                att_card = self.get_player().flip_card(self.turn_cards)
                result = self.check_posibility_for_flip(att_card)

                if result != 0: 
                    cprint('you cant do this','red')
                    if self.att_quantity % 2 == 1 and att_card not in self.first_deck: self.first_deck.append(att_card)
                    elif self.att_quantity % 2 != 1 and att_card not in self.second_deck: self.second_deck.append(att_card)

        if subcommand != None:
            for n in self.turn_cards:
                buff.append(n)
        else:
            buff = [(att_card),(def_card)]

        for  i in buff:
            if self.att_quantity % 2 == 1:
                if i not in self.second_deck:
                    self.second_deck.append(i)
                else: 
                    if i not in self.first_deck:
                        self.first_deck.append(i)

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

    def correct_card(self):
        print('\n')
        cprint('  ✔  ','light_green','on_green')
        for i in self.turn_cards:
            self.odboy.append(i)

    def check_posibility_for_flip(self, att_card):
        for i in self.turn_cards:
            result = deck_instance.compare_values_of_cards(att_card,i)
        return result

    def sort_deck(self):
        deck = self.get_player().player_deck
        sorted_deck = []
        for _ in range(len(deck)):
            card = deck_instance.min_card(deck)
            ind = deck.index(card)
            deck.pop(ind)
            sorted_deck.append(card)
        deck.clear()
        for i in sorted_deck:
            deck.append(i)
        return deck
    
    def turn_flip_card(self,command):
        subcommand_ = None   
        Card.print_cards(self.turn_cards)
        print('\n')
        att_card = self.get_player().flip_card(self.turn_cards)
        possibility = None
        while possibility != 0 and command != 'e':
            result = self.check_posibility_for_flip(att_card)
            if result == 0: possibility = 0 
                                           

            while possibility != 0 and subcommand != 'e':
                cprint('\nYou cant do this' ,'red')
                if self.att_quantity % 2 == 1 and att_card not in self.first_deck: self.first_deck.append(att_card)
                elif self.att_quantity % 2 != 1 and att_card not in self.second_deck: self.second_deck.append(att_card)
                subcommand = input(Style.BRIGHT+ Fore.CYAN + "\nflip more card <<c>>/end turn <<e>>: ")

                if subcommand != 'e': att_card = self.get_player().flip_card(self.turn_cards)
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
                    if def_card != None:self.second_deck.append(def_card)
                    def_card = self.get_player_for_defense().defense(self.turn_cards)
                else:
                    if def_card != None:self.first_deck.append(def_card)
                    def_card = self.get_player_for_defense().defense(self.turn_cards)
                result = self.result(att_card,def_card)
                                            
                if result != 2:
                    cprint('\nYou cant do this' ,'red')
                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")
                while subcommand_ not in ['d','t']:
                    cprint('\nwrong command','red')
                    subcommand_ = input(Style.BRIGHT+ Fore.CYAN + "\ndefense <<d>>/take-cards <<t>>: ")

                                            
                if subcommand_ == 't':command = 't'


        if subcommand_ == 't':
            command = 't'
    @staticmethod
    def result(att_card,def_card):
        return deck_instance.compare_cards(att_card,def_card)

# deck_instance = Deck()
Duren_instance = Duren(deck_instance.create_deck_for_player(), deck_instance.create_deck_for_player(),deck_instance.deck ,deck_instance)
bot_instance = BotDanil(Duren_instance.second_deck)