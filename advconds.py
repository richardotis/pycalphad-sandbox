from pycalphad import Database, Model, variables as v
from pycalphad.tests.datasets import ROSE_TDB
from pycalphad import equilibrium
import numpy as np

my_phases_rose = ['TEST']
comps = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F']
comps = sorted(comps)
conds = dict({v.T: 1000, v.P: 101325})
for comp in comps[1:]:
    conds[v.X(comp)] = 1.0/float(len(comps))
dbf = Database(ROSE_TDB)
eqx = equilibrium(Database(ROSE_TDB), comps, my_phases_rose, conds, calc_opts={'pdens': 10}, verbose=True)
