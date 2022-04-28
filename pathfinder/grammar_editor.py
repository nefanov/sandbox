TOKEN_LIST = ["any any","any assign_const"]

index = 0;
def inc_unique_suffix():
  global index
  index += 1
  return str(index)

class Term: # for terminal and non-terminal symbols
  def __init__(self, N="A", repeatable=False, optional=False):
    self.name = N
    self.repeatable = repeatable
    self.optional = optional
    return
  
  def repeatable(self, cond=True):
    self.repeatable = cond
    return

  def optional(self, cond=True):
    self.optional = cond
    
class Rule:
  def __init__(self, L, R):
    self.lhs = L
    self.rhs = R
    
  def __repr__(self):
    return "(" + self.lhs.name + " --> " + " ".join([r.name for r in self.rhs]) + ")"
    
  def make_repeatable(self):
    '''
    properties: idempotency
    usage: make once before grammar finalizing
    '''
    rl = [self]
    for idx, term in enumerate(self.rhs):
      if term.repeatable:
        new_term_name = term.name + inc_unique_suffix()
        t = Term(N=new_term_name)
        for rule in rl:
          try:
            if rule.rhs[idx].name == term.name:
              rule.rhs[idx].name == new_term_name
              rl.append(Rule(t,[t,term]))
              rl.append(Rule(t,[Term("any any")]))
          except:
            pass
        term.repeatable = False
    return rl
    
class Grammar:
  def __init__(self):
    self.P = list()
    pass
  
  def add_rule(self, L, R):
    left_side = L
    for r in R:
      if r.repeatable:
        pass
      if r.optional:
        pass
    
    self.P += rules_chain
    return rules_chain
  
  def add_alternative(self, rule, right):
    add_rule(rule[0], right)
    return
  
  def finalize():
    pass

def test1():
  print("#####Test #1#####")
  print(inc_unique_suffix(),inc_unique_suffix(), index)
  
def test2():
  print("#####Test #2#####")
  r = Rule(Term("A"), [Term("X", repeatable=True), Term("Y")])
  print("Make rule r repeatable on X:", r)
  rule = r.make_repeatable()
  print(rule)
  
if __name__=='__main__':
  test1()
  test2()
