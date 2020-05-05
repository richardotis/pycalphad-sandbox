# coding: utf-8
from pycalphad import Database, binplot, equilibrium, variables as v

dbf = Database('NI_AL_DUPIN_2001.TDB')
comps = ['AL', 'NI', 'VA']
phases = ['BCC_B2']
eq = equilibrium(dbf, comps, phases, {v.P: 101325, v.T: 1804, v.N: 1, v.X('AL'): 0.4798})
print(f'GM {eq.GM.values.squeeze():0.3f}')
print(f'MU {eq.MU.values.squeeze()}')
print(f'X {eq.X.values.squeeze()[0]}')
print(f'Y {eq.Y.values.squeeze()[0]}')

# sundman-solver (84146d5)
# GM -146559.061
# MU [-146954.58402776 -146194.25536231]
# Y [4.79789087e-01 5.20188169e-01 2.27438002e-05 4.79789087e-01
# 5.20188169e-01 2.27438002e-05 1.00000000e+00]

# vectorize-parameters (4ff8ef97)
# GM -154338.129
# MU [-167636.23828324 -142072.78310493]
# Y [9.49718498e-01 5.02814978e-02 4.35555687e-09 1.49677184e-03
# 9.81027763e-01 1.74754652e-02 1.00000000e+00]

