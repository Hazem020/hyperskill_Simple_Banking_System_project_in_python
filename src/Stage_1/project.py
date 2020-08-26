import random


class Account:
    IIN = 400000

    def __init__(self):
        identifier = str(random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)).strip("[]").replace(',', '').replace(' ',
                                                                                                                 '')
        self.pin = str(random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)).strip("[]").replace(',', '').replace(' ',
                                                                                                              '')
        self.card_number = '400000' + identifier
        self.Balance = 0

    def get_card_number(self):
        return self.card_number

    def get_balance(self):
        return self.Balance

    def get_pin(self):
        return self.pin


class Bank:
    def __init__(self):
        self.Accounts = []
        self.Accounts_details = {}

    def run(self):
        while True:
            choice = input('1. Create an account \n2. Log into account\n0. Exit\n')
            if choice == '1':
                Bank.create_account(self)
            elif choice == '2':
                card = input('Enter your card number:\n')
                pin = input('Enter your PIN:\n')
                if Bank.check_account(self, card, pin):
                    print('You have successfully logged in!')
                    Bank.login(self, card)
                else:
                    print('Wrong card number or PIN!')
            else:
                print('Bye!')
                exit()

    def check_account(self, card_number, pin):
        for a in self.Accounts:
            if a.get_card_number() == card_number:
                if a.get_pin() == pin:
                    return True
                else:
                    return False

    def create_account(self):
        a = Account()
        self.Accounts.append(a)
        self.Accounts_details[a.get_card_number()] = a
        print('Your card number:')
        print(a.get_card_number() + '\n')
        print('Your card PIN:')
        print(a.get_pin() + '\n')

    def login(self, card):
        while True:
            choice = input('1. Balance \n2. Log out\n0. Exit\n')
            if choice == '1':
                print('Balance:', self.Accounts_details[card].get_balance())
            elif choice == '2':
                print('You have successfully logged out!')
                break
            else:
                print('Bye!')
                exit()


B = Bank()
B.run()
