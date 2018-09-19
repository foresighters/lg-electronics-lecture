class Account(object):
    num_acount = 0

    def __init__(self, name, money):
        self.name = name
        self.total_money = money
        Account.num_acount += 1

    def __del__(self):
        Account.num_acount -= 1

    def withdraw(self, money):
        print(str(money) + "을 출금했습니다.")
        self.total_money -= money
        return None

    def deposit(self, money):
        print(str(money) + "을 입금했습니다.")
        self.total_money -= money
        return None

    @classmethod
    def count(cls):
        return Account.num_acount

    @staticmethod
    def hello_world():
        print("Hello World")


if __name__ == "__main__":
    lee = Account('lee', 10000)
    kim = Account('kim', 20000)

    print(lee.name, kim.name)

    lee.withdraw(300)
    lee.deposit(500)

    print(Account.num_acount)

    del lee

    print("Account 개수: ", str(Account.num_acount))
    print("Account 개수: ", str(Account.count()))
    print("Account 개수: ", str(kim.num_acount))

    kim.hello_world()

