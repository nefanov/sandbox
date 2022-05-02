from tabulate import tabulate
TOKEN_LIST = ["any any","any assign_const"]

index = 0;
def inc_unique_suffix():
  global index
  index += 1
  return str(index)

class Term: # for terminal and non-terminal symbols
  def __init__(self, N="A", repeatable=False, optional=False, repeat_limit=-1):
    self.name = N
    self.repeatable = repeatable
    self.repeat_limit = repeat_limit # -1 means "inf", or any positive number
    self.optional = optional
    return


  def __repr__(self):
      return "Term: " + self.name
  
  def repeatable(self, cond=True, limit="inf"):
    self.repeatable = cond
    self.repeat_limit = limit
    return

  def optional(self, cond=True):
    self.optional = cond


class Rule:
  '''
  L: left side
  R: right side
  tag: default | manual (written by programmer) | auto (generated)
  '''
  def __init__(self, L, R, tag="default"):
    self.lhs = L
    self.rhs = R
    self.tag = tag
    
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
              if term.repeat_limit == -1:
                if optional:
                  rl.append(Rule(t,[t,Term(orig_name)]))
                  rl.append(Rule(t,[Term("any any")]))
                else:
                  no_opt_name = term.name + '_' + inc_unique_suffix()
                  no_opt_name_2 = term.name + '_' + inc_unique_suffix()
                  t2 = Term(N=no_opt_name)
                  t3 = Term(N=no_opt_name_2)
                  rl.append(Rule(t,[t2,Term(orig_name)]))
                  rl.append(Rule(t2,[t,t3]))
                  rl.append(Rule(t2,[Term("any any")]))
                  rl.append(Rule(t3,[Term("any any")]))
              else:
                if optional:
                  last_term = rule.rhs[idx]
                  temp_name = rule.rhs[idx]
                  for i in range(term.repeat_limit):
                    temp_name = term.name + '_' + inc_unique_suffix()
                    temp_t = Term(temp_name)
                    rl.append(Rule(last_term, [temp_t, Term(orig_name)]))
                    last_term = temp_t
                  rl.append(Rule(last_term, [Term("any any")]))
                else:
                  pass
                  #TODO: non-optional [1,n]
          except:
            pass
        term.repeatable = False
    return rl
    
    def make_repeatable_and_non_optional(self):
        return self.make_repeatable(self, optional=False)


class Grammar:
  def __init__(self, from_list=[]):
    self.P = list() + from_list
    pass
  
  def new_sync_term_rule(self, left_part=Term("A"), lbr=Term("a"), rbr=Term("b"),
                         interrelation="==", optional=True, between=[
                                                                    Term("any any"),
                                                                    Term("any any"),
                                                                    Term("any any")
          ],
                                                            facings=None):
    rl = []
    if interrelation == "==":
      if between:
        new_term_l = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_l2 = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r2 = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r3 = Term(left_part.name + '_' + inc_unique_suffix())
        lt = Term("Term__" + lbr.name)
        rl.append(Rule(left_part, [new_term_l, new_term_r]))
        rl.append(Rule(new_term_l, [new_term_l2, left_part]))
        rl.append(Rule(new_term_l2, [lt, between[0]]))
        if facings:
          lt2 = Term("Term__" + lbr.name + "2")
          rl.append(Rule(lt, [facings[0], lt2]))
          rl.append(Rule(lt2, [lbr]))
        else:
          rl.append(Rule(lt, [lbr]))
        rl.append(Rule(left_part, [between[1], new_term_r3]))

        rl.append(Rule(new_term_r, [between[2], new_term_r2]))
        if facings:
          rt2 = Term("Term__" + rbr.name + "2")
          rl.append(Rule(new_term_r2, [rt2, facings[1]]))
          rl.append(Rule(rt2, [rbr]))
        else:
          rl.append(Rule(new_term_r2, [rbr]))

        rl.append(Rule(new_term_r3, [Term("any any")]))
      else:
        new_term_l = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_l2 = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r2 = Term(left_part.name + '_' + inc_unique_suffix())
        new_term_r3 = Term(left_part.name + '_' + inc_unique_suffix())
        rl.append(Rule(left_part, [new_term_l, new_term_r]))
        rl.append(Rule(new_term_l, [new_term_l2, left_part]))
        rl.append(Rule(new_term_l2, [lbr]))
        rl.append(Rule(new_term_r, [new_term_r2, new_term_r3]))
        rl.append(Rule(new_term_r2, [rbr]))
        rl.append(Rule(new_term_r3, [Term("any any")]))
    if optional:
      rl.append(Rule(left_part, [Term("any any")]))
      
    self.P += rl  
    return rl
   
  def print(self, table=True, tablefmt='orgtbl', tab_filter=[]):
    if table: # required: tabulate
      content = [[i, p.lhs.name, ",".join([z.name for z in p.rhs]), p.tag]  for i, p in enumerate(self.P) if p.tag not in tab_filter]
      header = ["No", "left side", "right side", "tag"]
      print(tabulate(content, headers=header, tablefmt=tablefmt))
    else:
      for idx, p in enumerate(self.P):
        print(idx, p)
    return

  def finalize(self):
    pass


class Editor:
  def newGrammar(self, rules=[], ):
    self.G(rules)

  def add_rule_from_config(self, config):
    rl = [Rule(Term(config['L']['name']), [Term(cont['name'],
                                                       repeatable=cont['repeatable'],
                                                       optional=cont['optional'] ) for cont in config['R']])]
    if (config['make_repeatable']):
      rl = rl[0].make_repeatable(True if config['make_optional'] else False)

  def saveGrammar(self):
    pass

  def printGrammar(self):
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
  
def test8():
  print("#####Test #8#####")
  r = Rule(Term("A"), [Term("X", repeatable=True, repeat_limit=2), Term("Y")])
  print("Make rule r repeatable 2 times on X:", r)
  rule = r.make_repeatable()
  print(rule)
  
def test9():
  print("#####Test #9#####")
  print("grammar for (D(D(D(..(B)..)C)C)C), |(|==|)|==n, braces seq is ok, n in [0, +inf),D,B,C are non-terminals")
  P = Grammar()
  res = P.new_sync_term_rule(between=[Term("D"),Term("B"),Term("C")], facings=None)
  print(res)

def test10():
  print("#####Test #10#####")
  print("grammar for a^nb^n, n in [0, +inf)")
  P = Grammar()
  res = P.new_sync_term_rule(between=None, facings=None)
  print(res)

def test11():
  print("#####Test #11#####")
  print("grammar for E(DE(DE(DE(..E(B)F..)FC)FC)FC), |(|==|)|==n, braces seq is ok, n in [0, +inf),D,B,C,E,F are non-terminals")
  P = Grammar()
  res = P.new_sync_term_rule(between=[Term("D"),Term("B"),Term("C")], facings=[Term("E"), Term("F")])
  print(res)

def test12():
  print("#####Test #12#####")
  g = Grammar([Rule(Term("A"),[Term("B"),Term("B")]) , Rule(Term("B"),[Term("b")])])
  g.print(table=True)
  g.print(table=False)

def test13():
  print("#####Test #13#####")
  g = Grammar([Rule(Term("A"),[Term("B"),Term("B")],tag="manual") , Rule(Term("B"),[Term("b")])])
  g.print(table=True, tab_filter=[])
  g.print(table=True, tab_filter=["default"])



if __name__ == '__main__':
  test1()
  test2()
  test3()
  test4()
  test5()
  test6()
  test7()
  test8()
  test9()
  test10()
  test11()
  test12()
  test13()
