import random
import sqlite3


class Account:
    IIN = 400000

    def __init__(self):

        self.pin = str(random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)).strip("[]").replace(',', '').replace(' ', '')
        self.card_number = str(Account.luhn_algorithm(self)).strip("[]").replace(',', '').replace(' ', '')

    def luhn_algorithm(self):
        card = [4, 0, 0, 0, 0, 0] + random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
        temp = card.copy()
        index = 0
        for digit in temp:
            if (index + 1) % 2 != 0:
                temp[index] = digit * 2
            index += 1
        index = 0
        for digit in temp:
            if digit > 9:
                temp[index] = digit - 9
            index += 1
        total = sum(temp)
        card.append((total * 9) % 10)
        return card

    def get_card_number(self):
        return self.card_number

    def get_pin(self):
        return self.pin


class Bank:
    def __init__(self):
        self.Accounts = []
        self.Accounts_details = {}
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance INTEGER DEFAULT 0
            );
            ''')
        self.conn.commit()

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
        self.cur.execute('SELECT * FROM card')
        bank_data = self.cur.fetchall()
        for a in bank_data:
            if a[1] == card_number:
                if a[2] == pin:
                    return True
                else:
                    return False

    def create_account(self):
        a = Account()
        self.cur.execute(f"INSERT INTO card(number, pin, balance) VALUES({a.get_card_number()}, {a.get_pin()}, 0)")
        self.conn.commit()
        print('Your card number:')
        print(a.get_card_number() + '\n')
        print('Your card PIN:')
        print(a.get_pin() + '\n')

    def login(self, card_number):
        self.cur.execute(f'SELECT * FROM card WHERE number = {card_number}')
        card = self.cur.fetchall()
        while True:
            choice = input('1. Balance \n2. Log out\n0. Exit\n')
            if choice == '1':
                print('Balance:', card[0][3])
            elif choice == '2':
                print('You have successfully logged out!')
                break
            else:
                print('Bye!')
                exit()


B = Bank()
B.run()
