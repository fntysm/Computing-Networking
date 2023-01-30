# this is to practice python

def create_spend_chart(categories):
    # The percentage spent should be calculated only with withdrawals
    bar_chart = "Percentage spent by category\n"
    percentage = 100
    while not percentage<0:
        bar_chart += str(percentage).rjust(3) + "|\n"
        percentage -= 10
    return bar_chart
def rounded_withdraws(categories):
    withdrawsRespectively = []
    for eachCategory in categories:
        withdrawsRespectively.append(round(abs(eachCategory.amount_spent()),-1))
    print(withdrawsRespectively)

class Category:
    # the ledger contain various objects, in the form of {"amount": amount, "description": description}
    # passing in the name of the category
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.ledger = list()
    def __str__(self):
        title = f"{self.categoryName:*^30}\n"
        items = ""
        total = self.get_balance()
        output = title
        for eachObject in self.ledger:
            desc = eachObject.get("description")
            amount = eachObject.get("amount")
            items += desc[0:23].ljust(23) + f"{amount:>7.2f}" + "\n"
        output += items + "Total: "+ str(total)
        return output

    def deposit(self, amount, description=""):
        ledgerObject = {"amount": amount, "description": description}
        self.ledger.append(ledgerObject)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            ledgerObject = {"amount": amount * (-1), "description": description}
            self.ledger.append(ledgerObject)
            return True
        else:
            return False

    def get_balance(self):
        currentBalance = 0
        # return the current balance of the category based on the deposits and the withdrawals
        for eachObject in self.ledger:
            currentBalance += eachObject.get("amount")
        return currentBalance

    def transfer(self, amount, anotherCategory):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + anotherCategory.categoryName)
            self.deposit(amount, "Transfer from " + self.categoryName)
            return True
        else:
            return False
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    def amount_spent(self):
        # we need this method, for the create_spend_chart function, to know the amount of the money spent for each
        # category
        withdrawTotal = 0
        for eachOperation in self.ledger:
            if eachOperation.get("amount") < 0:
                withdrawTotal += eachOperation.get("amount")
        return withdrawTotal