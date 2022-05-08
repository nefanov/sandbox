from grammar_editor import *

def test1():
    print("#####Test #1#####")
    print(inc_unique_suffix(), inc_unique_suffix(), index)


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
    r = Rule(Term("A"), [Term("X", repeatable=True, optional=True, repeat_limit=20), Term("Y")])
    print("Make rule r repeatable 20 times on optional X:", r)
    rule = r.make_repeatable()
    print(rule)


def test9():
    print("#####Test #9#####")
    print("grammar for (D(D(D(..(B)..)C)C)C), |(|==|)|==n, braces seq is ok, n in [0, +inf),D,B,C are non-terminals")
    P = Grammar()
    res = P.new_sync_term_rule(between=[Term("D"), Term("B"), Term("C")], facings=None)
    print(res)


def test10():
    print("#####Test #10#####")
    print("grammar for a^nb^n, n in [0, +inf)")
    P = Grammar()
    res = P.new_sync_term_rule(between=None, facings=None)
    print(res)


def test11():
    print("#####Test #11#####")
    print(
        "grammar for E(DE(DE(DE(..E(B)F..)FC)FC)FC), |(|==|)|==n, braces seq is ok, n in [0, +inf),D,B,C,E,F are non-terminals")
    P = Grammar()
    res = P.new_sync_term_rule(between=[Term("D"), Term("B"), Term("C")], facings=[Term("E"), Term("F")])
    print(res)


def test12():
    print("#####Test #12#####")
    g = Grammar([Rule(Term("A"), [Term("B"), Term("B")]), Rule(Term("B"), [Term("b")])])
    g.print(table=True)
    g.print(table=False)


def test13():
    print("#####Test #13#####")
    g = Grammar([Rule(Term("A"), [Term("B"), Term("B")], tag="manual"), Rule(Term("B"), [Term("b")])])
    g.print(table=True, tab_filter=[])
    g.print(table=True, tab_filter=["default"])


def test14():
    print("#####Test #14#####")
    a = Rule(Term("A"), [Term("a")], tag="manual")
    b = Rule(Term("B"), [Term("b")])
    c = Rule(Term("C"), [Term("c")])
    g = Grammar([a, b, c])
    g.print(table=True, tab_filter=[])
    g.finalize(sequence=[a, b, c])
    print("After grammar finalizing:")
    g.print(table=True, tab_filter=[])


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
    test14()