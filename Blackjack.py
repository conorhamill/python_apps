#global variables and imports

import random

suits = ('hearts','clubs','diamonds','spades')

ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')

values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 
            'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':1}


print("Welcome to blackjack, if you dont know the rules... to bad. Let's play")
    

class Card:
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for i in suits:
            for j in ranks:
                new_card = Card(i,j)
                
                self.all_cards.append(new_card)
                
    def shuffle(self):
        
        random.shuffle(self.all_cards)

class Player:
    
    def __init__(self):
        
        self.player_hand = []
        
    def show_hand(self):
        
        for i in range(len(self.player_hand)):
            print(self.player_hand[i])
    
    def hand_value(self):
        
        total_value = 0 
        
        for i in range(len(self.player_hand)):
            total_value = total_value + self.player_hand[i].value
            
        return total_value

class Pot:
    
    def __init__(self):
        
        input_needed = True

        while input_needed:

            self.current_pot = input('How much would you like to start with?')

            if self.current_pot.isdigit() == False:
                print('incorrect input, try again')
            elif int(self.current_pot) <= 0:
                print('Pot must be > 0 ')
            else:
                self.current_pot = int(self.current_pot)
                print(f'Total pot: {self.current_pot}')
                input_needed = False
        
        
    def place_bet(self):
    
        input_needed = True

        while input_needed:

            self.current_bet = input('Place bet:')

            if self.current_bet.isdigit() == False:
                print('incorrect input, try again')
            elif int(self.current_pot) < int(self.current_bet):
                print(f'Bet must equal or less than current pot: {self.current_pot}')
            else:
                self.current_bet = int(self.current_bet)
                print(f'Bet: {self.current_bet}')
                input_needed = False
        
    def win_bet(self):
        
        self.current_pot = self.current_pot + 2*self.current_bet
        
    def lose_bet(self):
        
        self.current_pot = self.current_pot - self.current_bet
        
    def cash_out(self):
        
        #from IPython.display import clear_output
        
        #clear_output()
        
        input_needed = True

        while input_needed:

            next_move = input('play or cashout?')

            if next_move not in ['play','cashout']:
                print('incorrect input, try again')
            elif next_move == 'play':
                return True
                input_needed = False
            else:
                print(f'cashed out at {self.current_pot}')
                return False
                input_needed = False
        
    def __str__(self):
        return f"current pot: {self.current_pot}"

#different functions needed

def ShowTable():
    
    from IPython.display import clear_output
    
    clear_output()
    
    print(f'Computer hand: \n')
    print(computer.player_hand[0])
    print('*Face down card*')

    print('\n')

    print(f'Your hand: Value = {main_player.hand_value()} \n')
    main_player.show_hand()


def ShowFullTable():
    
    from IPython.display import clear_output
    
    clear_output()
    
    print(f'Computer hand: Value = {computer.hand_value()}\n')
    computer.show_hand()

    print('\n')

    print(f'Your hand: Value = {main_player.hand_value()} \n')
    main_player.show_hand()
    
    
def PlayerMove():

    input_needed = True

    while input_needed:

        next_move = input('hit or stay?')

        if next_move not in ['hit','stay']:
            print('incorrect input, try again')
        elif next_move == 'hit':
            return 'hit'
            input_needed = False
        else:
            return 'stay'
            input_needed = False
            
            
# game setup 
    
from IPython.display import clear_output

player_pot = Pot()

#main game loop

match_on = True


while match_on:

    clear_output()
    
    #place initial bet
    
    player_pot.current_bet= ''
    player_pot.place_bet()

    #deal cards
    
    game_deck = Deck()
    game_deck.shuffle()
    
    main_player = Player()
    computer = Player()

    for i in range(2):
        main_player.player_hand.append(game_deck.all_cards.pop(0))
        computer.player_hand.append(game_deck.all_cards.pop(0))
    
    ShowTable()

    #game starts 
    
    game_on = True 

    while game_on:
        
        #if the player decides to stay the computer will continue to hit until it wins or loses

        if PlayerMove() == 'stay':
            
            print('computers turn')
            
            computer_game_on = True
            
            while computer_game_on:
            
                #deal card for computer and show computer cards

                computer.player_hand.append(game_deck.all_cards.pop(0)) 
                ShowFullTable()

                #check to see if the computer hand value is equal or above 21

                if computer.hand_value() >= 21:

                    print('\nComputer BUST! You win')

                    player_pot.win_bet()
                    print(player_pot)

                    game_on = False
                    break

                #check to see if the computer hand is greater than player i.e. between 21 and player hand

                elif computer.hand_value() > main_player.hand_value():

                    print('\nBUST! Computer wins')

                    player_pot.lose_bet()
                    print(player_pot)

                    game_on = False
                    break

                else:
                    pass
            
            #once computer has bust or won the game is over
            
            game_on = False
            break
        
        #if the player decides to hit        

        else:
            
            #deal card for player

            main_player.player_hand.append(game_deck.all_cards.pop(0))     
            ShowTable()
            
            #check to see if player has value equal or above 21, computer wins

            if main_player.hand_value() >= 21:
                
                print('\nBUST! Computer wins')
                
                player_pot.lose_bet()
                print(player_pot)
                
                game_on = False
                break
                
            #if value still below 21 player can have another move
            
            else:
                pass

    #when game is over check if pot is gone or player wants to cashout
    
    if player_pot.current_pot == 0:
        
        print('Game over, you have no money left')

        match_on = False
        break
    
    elif player_pot.cash_out() == False:

        match_on = False
        break
        
    else:
        pass
    
    