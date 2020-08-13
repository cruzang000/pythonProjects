import math


# category class
class Category:

    #  runs on object creation sets category and instantiates ledger list
    def __init__(self, category):
        self.ledger = list()
        self.category = category

    #  adds amount and description to ledger list
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(round(amount, 2)), "description": description})

    #  adds amount as negative and description to ledger list
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": float(amount * -1), "description": description})
            return True

        return False

    # returns balance of transactions
    def get_balance(self):
        return 0 + sum([transaction["amount"] for transaction in self.ledger])

    # checks if funds available then withdraws from current category, deposits to category passed
    # in as arg and returns true or false if transaction complete
    def transfer(self, amount, category):
        category.deposit(amount, ("Transfer from " + self.category))

        return self.withdraw(amount, ("Transfer to " + category.category))

    # checks if amount is less or equal to balance
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # totals a transaction type amount in ledger either deposits or withdrawals returns transaction total
    def totalByTransactionType(self, transactionType):
        transactionTotals = {
            "deposit":
                sum([transactions["amount"] for transactions in self.ledger if transactions["amount"] >= 0]),
            "withdrawal":
                abs(sum([transactions["amount"] for transactions in self.ledger if transactions["amount"] < 0]))
        }

        return transactionTotals[transactionType]

    # returns object info as string
    def __str__(self):
        stars = (30 - len(self.category)) / 2
        firstLine = ("*" * math.floor(stars)) + self.category + ("*" * math.ceil(stars))

        secondLine = ""
        total = 0

        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = str('%.2f' % transaction["amount"])[:7].rjust(30 - len(description))
            secondLine = secondLine + "\n" + description + amount
            total = total + transaction["amount"]

        return firstLine + secondLine + "\nTotal: " + str('%.2f' % total)


# takes categories and returns list of withdrawal totals for transaction type passed in
def getTransactionTotalByType(categories, transactionType):
    return [category.totalByTransactionType(transactionType) for category in categories]


# function takes categories and builds graph using transaction type totals and percentages
def buildGraphData(categories, transactionType):
    # graph data, y axis as rows
    graphData = {
        "100": [],
        "90": [],
        "80": [],
        "70": [],
        "60": [],
        "50": [],
        "40": [],
        "30": [],
        "20": [],
        "10": [],
        "0": [],
    }

    # call function to get transaction totals for a specific transaction type for all categories
    withdrawalTotals = getTransactionTotalByType(categories, transactionType)

    # fill y axis rows with o's to build bar graph using percentages
    for point in graphData:
        for total in withdrawalTotals:
            percentage = total / sum(withdrawalTotals) * 100
            graphData[point].append(
                ("o" if percentage >= int(point) else " ")
            )

    return graphData


# function adds line break to string
def addLineBreak(string):
    return string + "\n"


# function takes graph dictionary and returns string of graph
def graphToString(graphData):
    rowCount = 0
    chart = ""

    for (row, cols) in graphData.items():
        chart = chart + row.rjust(3) + "|"
        for col in range(len(cols)):
            chart = chart + " " + cols[col] + ("  " if col == (len(cols) - 1) else " ")

        if rowCount != (len(graphData.items())):
            chart = addLineBreak(chart)

        rowCount = rowCount + 1

    return chart


# builds key columns for row using categories
def buildRowColumns(row, categories):
    chart = ""

    for col in range(len(categories)):
        isLastColumn = col == len(categories) - 1
        if row == 0:
            chart = chart + ("----" if isLastColumn else "---")
        else:
            index = row - 1

            if index < len(categories[col].category):
                currentLetter = categories[col].category[index]
            else:
                currentLetter = " "

            chart = chart + f" {currentLetter} " + (" " if isLastColumn else "")

    return chart


# takes categories and returns graph string with keys as x axis
def buildGraphKeys(categories):
    chart = ""
    rows = max(len(category.category) for category in categories)

    for row in range(rows + 1):
        chart = chart + "    " + buildRowColumns(row, categories)

        if row != rows:
            chart = addLineBreak(chart)

    return chart


# creates spending chart by category using categories list passed in
def create_spend_chart(categories):
    # call function to build graph data dictionary passing in categories and transaction type
    graphData = buildGraphData(categories, "withdrawal")

    # start building chart string
    chart = "Percentage spent by category\n" + graphToString(graphData) + buildGraphKeys(categories)

    return chart
