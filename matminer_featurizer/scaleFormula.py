from pymatgen.core import Composition

formula_list=[]
def ScaledFormula(lst):
    '''Converts fractional composition formula to scaled formula'''
    ''' Li0.5O2 returns to Li2O4'''
    [formula_list.append(Composition(i).get_integer_formula_and_factor()[0]) for i in lst]
    
    return formula_list
