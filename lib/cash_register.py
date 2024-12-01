#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self,discount=0,total=0,items=None):
    pass
    self.total = total
    self.discount = discount
    self.items = items if items is not None else []
  
  def add_item(self, item, price, quantity=1):
    pass
    self.amount = price
    self.quantity = quantity
    self.total += price * quantity
    for _ in range(quantity):
       self.items.append(item)
  
  def apply_discount(self):
    pass
    if self.discount>0:
      pass
      self.total -= self.total * (self.discount/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      pass
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if (self.items == None):
     self.total = 0.0
    else:
      for _ in range (self.quantity):
        self.items.pop()
        self.total -=  self.amount