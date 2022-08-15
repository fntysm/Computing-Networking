def create_spend_chart(categories):
    return None

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
            desc = eachObject.get("description")[::23]
            items +=
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