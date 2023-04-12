'''this project is aimed at creating a small text-based blackjack game with a computer dealer and a human player
'''
# first we will declare some global variables and then create a deck of cards
import random
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}  # a small caveat:in actuality ace can either be 11 or 1 but that change will be dealt with in the logic


class Card:

    '''we first create a card class that we will use to create card objects that wiil be used throughout the game play.
    the card class will holds the suit of the card,the rank and the value
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# now we will create the deck class that creates a new deck each time it is called and a method to shuffle it


class Deck:
    def __init__(self):
        self.all_cards = []
        # the for loops below create the entire deck of cards
        for st in suits:
            for rn in ranks:
                self.all_cards.append(Card(st, rn))

    def __str__(self):
        printString = ''
        for cd in self.all_cards:
            printString += f'{cd.rank} of {cd.suit}\n'
        return printString

    def shuffle(self):
        random.shuffle(self.all_cards)

    def remove_one(self):
        # to play blckjack the dealer needs to be able to remove a card from the top of the deck(index zero)
        return self.all_cards.pop(0)

# we also need a player class that will hold all the cards the player has been dealt,his name and bankroll


class Player():
    def __init__(self, name, bank_amount):
        self.name = name
        self.bank_amount = bank_amount
        self.delt_cards = []

    def __str__(self):
        return f"{self.name}'s account balance is {self.bank_amount}ksh"

    def place_bet(self, bet_amount):
        if bet_amount > self.bank_amount:
            print('Sorry! you do not have enough funds, please top up')
        else:
            self.bank_amount -= bet_amount
        return bet_amount

    def top_up(self, top_amount):
        self.bank_amount += top_amount

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.delt_cards.extend(new_cards)
        else:
            self.delt_cards.append(new_cards)

# we also create a dealer class that holds the dealer cards on the table
# it also allows the dealer to deal cards.


class Dealer:
    def __init__(self):
        self.delt_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.delt_cards.extend(new_cards)
        else:
            self.delt_cards.append(new_cards)

# now the gameplay


def gameplay():
    print(len(new_deck.all_cards))
    while True:
        try:
            betAmount = int(input('Please enter your bet amount:'))
        except ValueError:
            print('Whoops that is not a numeral')
        else:
            break

    # print(new_player.bank_amount)
    while betAmount > new_player.bank_amount:
        print('You are betting more than you have')
        while True:
            try:
                topAmount = int(input('Please enter your top up amount:'))
            except ValueError:
                print('Whoops that is not a numeral')
            else:
                break
        new_player.top_up(topAmount)
        print(new_player.bank_amount)
        while True:
            try:
                betAmount = int(input('Please enter your bet amount:'))
            except ValueError:
                print('Whoops that is not a numeral')
            else:
                break
    betVal = new_player.place_bet(betAmount)
    print(f'You have placed a {betVal}sh bet \n lets deal')

    # now we are at the dealing part of the match
    # deal one card from the top of the stack to the player
    new_player.add_cards(new_deck.remove_one())
    # deal one card from the top of the stack to the dealer
    new_dealer.add_cards(new_deck.remove_one())
    # deal one card from the top of the stack to the player
    new_player.add_cards(new_deck.remove_one())
    # deal one card from the top of the stack to the dealer
    new_dealer.add_cards(new_deck.remove_one())

    # showing the cards
    def print_cards(bul):
        print('\tPlayers cards')
        for i in new_player.delt_cards:
            print(i)
        print('\tDealers cards')
        if bul:
            for i in new_dealer.delt_cards:
                print(i)

        else:
            for i in range(len(new_dealer.delt_cards)):
                if i == 0:
                    print('Face down Card')
                else:
                    print(new_dealer.delt_cards[i])
    print_cards(False)

    def hit(playing):
        if playing == 'player':
            try:
                new_player.add_cards(new_deck.remove_one())
            except IndexError:
                print(
                    'all the cards in the deck are used up \nTo restart rerun the script')
                exit()
            else:
                print_cards(False)
        elif playing == 'dealer':
            try:
                new_dealer.add_cards(new_deck.remove_one())
            except IndexError:
                print(
                    'all the cards in the deck are used up \nTo restart rerun the script')
                exit()
            else:
                print_cards(True)

    def check_bust(obj):
        # this is a function to check for a bust
        # we will also implement the two values of ace i.e 11 and 1;recall we assumed the value of ace is 11 initially
        bustVal = 0
        # ace is 11
        for card in obj.delt_cards:
            bustVal += card.value
        # ace is 1
        if bustVal > 21:
            numAce = 0
            for card in obj.delt_cards:
                if card.value == 11:
                    numAce += 1
            while bustVal > 21 and numAce:
                bustVal -= 10
                numAce -= 1
        return bustVal > 21

    def check_val(obj):
        val = 0
        # ace is 11
        for card in obj.delt_cards:
            val += card.value
        # ace is 1
        if val > 21:
            numAce = 0
            for card in obj.delt_cards:
                if card.value == 11:
                    numAce += 1
            while val > 21 and numAce:
                val -= 10
                numAce -= 1
        return val

    # check for a blackJack
    if new_player.delt_cards[0].value + new_player.delt_cards[1].value == 21:
        print('Congrats you have a Blackjack and your payout has been made')
        print(f'You have won {1.5 * betVal}')
        # for a blackjack the payout is a 3 to 2 profit margin
        new_player.top_up(int(2.5*betVal))
        print(new_player)
    else:
        hs = True
        while hs:
            hit_stay = input('Do you want to hit[h] or stay[s]: ')
            hitapprove = True
            while hit_stay.lower() == 'h' and hitapprove:
                hit('player')
                if check_bust(new_player):
                    print('You have busted!Game over')
                    print(new_player)
                    hs = False
                    break
                else:
                    while True:
                        hit_stay = input('Do you want to hit[h] or stay[s]: ')
                        if hit_stay.lower() == 'h':
                            break
                        elif hit_stay.lower() == 's':  # *
                            break
                        else:
                            print('Invalid value, we will prompt you again')

                hs = False
            if hit_stay.lower() == 'h':
                pass
            elif hit_stay.lower() == 's':
                print_cards(True)
                hitapprove = True
                while check_val(new_dealer) < 16 and hitapprove:
                    hit('dealer')
                    check_val(new_dealer)  # revisit
                if check_bust(new_dealer):
                    print('Dealer has busted!')
                    print(f'You have won {betVal}')
                    new_player.top_up(int(2*betVal))  # players have won
                    print(new_player)
                else:
                    if check_val(new_dealer) > check_val(new_player):
                        print('Dealer has won! you have lost')
                        print(new_player)
                    elif check_val(new_dealer) < check_val(new_player):
                        print(f'You have won {betVal}')
                        new_player.top_up(int(2*betVal))
                        print(new_player)
                    else:
                        print('You have broken even')
                        new_player.top_up(int(betVal))
                        print(new_player)
                hs = False
            else:
                print('Invalid value, we will prompt you again')

# we welcome the player and asks if he wants to play


print("Welcome to Jeremiah's casino")
while True:
    in_out = input('Wanna play some Blackjack yes[y] no[n]: ')
    if in_out.lower() == 'n':
        print('To restart rerun the script')
        break
    elif in_out.lower() == 'y':

        # now lets set up the deck and the dealer
        new_deck = Deck()
        new_deck.shuffle()
        new_dealer = Dealer()

        # lets setup the player
        pName = input('Please enter your name: ')
        while True:
            try:
                bankAmount = int(input('Please enter your bankroll amount:'))
            except ValueError:
                print('Whoops that is not a numeral')
            else:
                break
        new_player = Player(pName, bankAmount)
        while True:
            r_start = input('Wanna start a round yes[y] no[n]: ')
            if r_start.lower() == 'n':
                print('To restart rerun the script')
                break
            elif r_start.lower() == 'y':
                new_dealer.delt_cards = []
                new_player.delt_cards = []
                gameplay()
                if len(new_deck.all_cards) < 4:
                    print(
                        'There are not enough cards in the deck, to restart rerun the script')
                    break
            else:
                print('Invalid value, we will prompt you again')
        break
    else:
        print('Invalid value, we will prompt you again')
