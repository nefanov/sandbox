TOKEN_LIST = ["any any","any assign_const"]

class Term: # for terminal and non-terminal symbols
  def __init__(self, N="A"):
    self.name = N
    self.repeatable = False
    self.optional = False
    return
  
  def repeatable(self, cond=True):
    self.repeatable = cond
    return

  def optional(self, cond=True):
    self.optional = cond
    
class Grammar:
  def __init__(self):
    self.P = list()
    pass
  
  def add_rule(self, L, R)
    left_side = L
    for r in R:
      if r.releatable:
        pass
      if r.optional:
        pass
    
    self.P += rules_chain
    return rules_chain
  
  def add_alternative(self, rule, right):
    add_rule(rule[0], right)
    return
