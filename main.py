from logics import *
P,Q,R = vars ('P','Q','R')
"""formula = (P&Q)
formula.print_truth_table()
print(formula.is_tautology())
formula = Implies((P&Q),(P|Q))
formula.print_truth_table()"""

"""formula = Implies((P|(Implies(P,Q))),Q)
formula.print_truth_table()
print(formula.is_tautology())

print(formula.is_equivalent(Implies((P&Q),(P|Q))))"""
"""formula1 = ~(P&Q)
formula2 = ~P|~Q
formula1.print_truth_table()
formula2.print_truth_table()
print(formula1.is_equivalent(formula2))"""


"""var1 = Implies(P,Q)
var2 = ~P|Q
var1.print_truth_table()
var2.print_truth_table()
print(var1.is_equivalent(var2))"""

"""var1 = Implies(P,Q)
var2 = Implies(var1,P)
var2.print_truth_table()"""

var1 = Implies((P&Q),R)
var2 = Implies(P,Implies(Q,R))
var3 = Iff(var1,var2)
var3.print_truth_table()


