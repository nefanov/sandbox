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

  def __repr__(self):
      return "Term: " + self.name
  
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
    
  def make_repeatable(self, optional=True):
    '''
    properties: idempotency
    usage: make once before grammar finalizing
    '''
    rl = [self]
    last_initial_rule_idx = 0
    for idx, term in enumerate(self.rhs):
      if term.repeatable:
        orig_name = term.name
        new_term_name = term.name + '_' + inc_unique_suffix()
        t = Term(N=new_term_name)
        
        for i, rule in enumerate(rl):
          try:
            if rule.rhs[idx].name == orig_name and last_initial_rule_idx >= i:
              rule.rhs[idx].name = new_term_name
              if optional:
                rl.append(Rule(t,[t,Term(orig_name)]))
                rl.append(Rule(t,[Term("any any")]))
              else:
                print(rl)
                no_opt_name = term.name + '_' + inc_unique_suffix()
                no_opt_name_2 = term.name + '_' + inc_unique_suffix()
                t2 = Term(N=no_opt_name)
                t3 = Term(N=no_opt_name_2)
                rl.append(Rule(t,[t2,Term(orig_name)]))
                rl.append(Rule(t2,[t,t3]))
                rl.append(Rule(t2,[Term("any any")]))
                rl.append(Rule(t3,[Term("any any")]))
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
  
def test3():
  print("#####Test #3#####")
  r = Rule(Term("A"), [Term("X"), Term("Y", repeatable=True)])
  print("Make rule r repeatable on Y:", r)
  rule = r.make_repeatable()
  print(rule)
  
def test4():
  print("#####Test #4#####")
  r = Rule(Term("A"), [Term("X", repeatable=True), Term("Y")])
  print("Make rule r non-optional and repeatable on X:", r)
  rule = r.make_repeatable(optional=False)
  print(rule)
  
def test5():
  print("#####Test #5#####")
  r = Rule(Term("A"), [Term("X"), Term("Y", repeatable=True)])
  print("Make rule r non-optional and repeatable on Y:", r)
  rule = r.make_repeatable(optional=False)
  print(rule)
  
def test6():
  print("#####Test #6#####")
  r = Rule(Term("A"), [Term("X", repeatable=True), Term("Y", repeatable=True)])
  print("Make rule r repeatable on X and Y:", r)
  rule = r.make_repeatable()
  print(rule)
  
def test7():
  print("#####Test #7#####")
  r = Rule(Term("A"), [Term("X", repeatable=True), Term("Y", repeatable=True)])
  print("Make rule r non-optional and repeatable on X and Y:", r)
  rule = r.make_repeatable(optional=False)
  print(rule)
  
if __name__=='__main__':
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
