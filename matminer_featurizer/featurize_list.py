'''this script use pymatgen and matminer to create pandas datafram of features
of list of formulas '''
''' Features are derived from a material’s ElementFraction. '''

import pandas as pd
import numpy as np
from pymatgen.core import Composition
from matminer.featurizers.composition.element import ElementFraction
ef = ElementFraction()

## lst = ['MnO2', 'LiO2'] list of formulas

def featurize_list(lst):
    
    composition_list = []
    composition_list.append([Composition(i) for i in lst])
    feture_list =[]
    feture_list.append([ef.featurize(j) for j in composition_list[0]])
    df = pd.DataFrame(feture_list[0])
    df['formula'] = lst
    df1st = df.pop('formula') 
    df.insert(0, 'formula', df1st)
    return df
