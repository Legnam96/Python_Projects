class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()
    self.spent = 0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)):
      self.spent += amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i["amount"]
    return balance

  def transfer(self, amount, category):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  def check_funds(self, amount):
    if (self.get_balance() >= amount):
      return True
    return False

  def __str__(self):
    tittle = f"{self.name:*^30}\n"
    items = str()
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:7.2f}" + '\n'
      total += item['amount']

    output = tittle + items + "Total: " + str(total)
    return output


def create_spend_chart(categories):
  total = 0
  final = "Percentage spent by category\n"
  for i in categories:
    total += i.spent
  final += f"100|          \n"
  for i in range(90, -10, -10):
    if i == 0:
      final += " "
    final += f" {i}|"
    for j in categories:
      if round(j.spent / 10) * 10 / total * 100 >= i:
        final += " o "
      else:
        final += "   "
    final += " \n"
  final += "    " + "-" * ((len(categories) * 3) + 1)
  fails = greatest = 0
  for i in categories:
    if len(i.name) > greatest:
      greatest = len(i.name)
  for j in range(greatest):
    fails = 0
    final += "\n     "
    for i in categories:
      try:
        if fails > 0:
          final += "   "
        final += i.name[j] + "  "
      except:
        fails += 1
  return final
