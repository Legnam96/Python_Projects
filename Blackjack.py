import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit            #To assign the suit to the card
        self.rank = rank            #To assign the rank to the card
    def __str__(self):
        return f"{self.rank['Rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self. cards = []                #This is our card
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = [
        {"Rank":"A", "Value": 11},
        {"Rank":"2", "Value": 2} ,
        {"Rank":"3", "Value": 3} ,
        {"Rank":"4", "Value": 4} ,
        {"Rank":"5", "Value": 5} ,
        {"Rank":"6", "Value": 6} ,
        {"Rank":"7", "Value": 7} ,
        {"Rank":"8", "Value": 8} ,
        {"Rank":"9", "Value": 9} ,
        {"Rank":"10", "Value": 10} ,
        {"Rank":"J", "Value": 10} ,
        {"Rank":"Q", "Value": 10} ,
        {"Rank":"K", "Value": 10} 
        ]
                

        for suit in suits:
            for rank in ranks: 
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:     #This checks if there's any cards left
            random.shuffle(self.cards)          #We shuffle the cards
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0 
        self.dealer = dealer

    def  add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards: 
            card_value = int(card.rank["Value"])
            self.value += card_value
            if card.rank["Rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value 

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value", self.get_value())
            print()
class Game:
    def play (self):
        game_number = 0
        games_to_play = 0
        while games_to_play == 0:
            try:
                games_to_play = int(input("How many games do you wanna play? "))
            except:
                print("You must enter a number.")
        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
             
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand'").lower()
                print()
                while choice not in ["s", "stand", "h", "hit"]:
                    choice = input("Please choose '(H)''Hit' or '(S)''Stand'").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue
            player_hand_value =  player_hand.get_value()
            dealer_hand_value =  dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value =  dealer_hand.get_value()
            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print(f"Final Results: ")
            print("Your hand:" , player_hand_value, )
            print("Dealer's hand:" , dealer_hand_value, )

            self.check_winner(player_hand, dealer_hand, True)
        
        print("\nThanks for playing!")

        
            
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You are busted, Dealer Wins! 🥲")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted, You Wins! 😎")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both player have a BlackJack, Tie. 😐")  
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack! You Win! 😎")  
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer have blackjack! You Lose! 🥲")  
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print ("You Win! 😎")
            elif player_hand.get_value() == dealer_hand.get_value():
                print ("Tie! 😐") 
            else:
                print ("Dealer wins. 🥲")
            return True

        return False 

g = Game()
g.play()
