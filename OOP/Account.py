import datetime
import pytz

class Account:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transactionList=[]
        print("New Account Created for "+self.name)

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            self.show_balance()
            self.transactionList.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0<amount<=self.__balance:
            self.__balance-= amount
            self.transactionList.append((Account._current_time(), -amount))
        else:
            print("You withdraw amount is more than your balance.")
        self.show_balance()

    def show_balance(self):
        print("Account Balance is: {}".format(self.__balance))

    def show_transaction(self):
        for date,amount in self.transactionList:
            if amount > 0:
                tran_type="deposited"
            else:
                tran_type="withdrawn"
                amount *=1
            print("{:6} {} on {} (Local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    a1 = Account("Ashraf",5000)
    a1.show_balance()
    a1.deposit(1000)
    a1.withdraw(2000)
    a1.show_transaction()
    a1._Account__balance = 100
    a1.show_balance()

    


