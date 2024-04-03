# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import gurobipy as gp

U = ['OH', 'OC']
C = ['MA', 'HM', 'MB']
# Zijn er veel meer voor nu even alleen deze.
L = ['100', '200', '300', '400', '500']
# Er zijn meer sporen maar dit is effe voor het beeld nu.

model = gp.Model("train scheduling")

N = {}
for u in U:
    for c in C:
        N[u, c] = model.addVar(vtype=gp.GRB.INTEGER, name="N_uc")

objective = 260000 * sum(N['OC', c] for c in C) + 210000 * sum(N['OH', c] for c in C)
model.setObjective(objective, gp.GRB.MINIMIZE)

v = {}
for l in L:
    v[l] = model.addVar(vtype=gp.GRB.BINARY, name="v_l")

for l in L:
    if l == '400':
        model.addConstr(v[l] == 1)
    else:
        model.addConstr(v[l] == 0)



