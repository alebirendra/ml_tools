'''this script use pymatgen and matminer to create pandas datafram of features
of list of formulas '''
''' Features are derived from a material’s ElementFraction. '''
''' Composition featurizers for elemental data and stoichiometry. '''

import pandas as pd
import numpy as np
from pymatgen.core import Composition
from matminer.featurizers.composition.element import ElementFraction
ef = ElementFraction()

## lst = ['MnO2', 'LiO2'] list of formulas

def ElementFractionFeaturizer(lst):
    
    '''calculate the atomic fraction of each element in a composition of 
    given list of formulas.

    Returns:
            A pandas dataframe with features of given list.'''
    
    composition_list = []
    composition_list.append([Composition(i) for i in lst])
    feture_list =[]
    feture_list.append([ef.featurize(j) for j in composition_list[0]])
    df = pd.DataFrame(feture_list[0])
    df['formula'] = lst
    df1st = df.pop('formula') 
    df.insert(0, 'formula', df1st)
    return df




from matminer.featurizers.composition.element import TMetalFraction
tmf = TMetalFraction()
# TMetalFraction Class calculate fraction of magnetic transition metals 
# in a composition.

## lst = ['MnO2', 'LiO2'] list of formulas

def TMetalFractionFeaturizer(lst):
    
    '''calculate fraction of magnetic transition metals in a composition of 
    given list of formulas.

    Returns:
            A pandas dataframe with features of given list.'''
    
    composition_list = []
    composition_list.append([Composition(i) for i in lst])
    feture_list =[]
    feture_list.append([tmf.featurize(j) for j in composition_list[0]])
    df = pd.DataFrame(feture_list[0])
    df['formula'] = lst
    df1st = df.pop('formula') 
    df.insert(0, 'formula', df1st)
    return df






from matminer.featurizers.composition.element import Stoichiometry
stochi = Stoichiometry()
# Calculate norms of stoichiometric attributes.

## lst = ['MnO2', 'LiO2'] list of formulas

def StoichiometryFeaturizer(lst):
    
    '''Calculate norms of stoichiometric attributes of 
    given list of formulas.

    Returns:
            A pandas dataframe with features of given list.'''
    
    composition_list = []
    composition_list.append([Composition(i) for i in lst])
    feture_list =[]
    feture_list.append([stochi.featurize(j) for j in composition_list[0]])
    df = pd.DataFrame(feture_list[0])
    df['formula'] = lst
    df1st = df.pop('formula') 
    df.insert(0, 'formula', df1st)
    return df



from matminer.featurizers.composition.element import BandCenter
bc = BandCenter()
# Estimation of absolute position of band center using electronegativity.

## lst = ['MnO2', 'LiO2'] list of formulas

def BandCenterFeaturizer(lst):
    
    '''Estimation of absolute position of band center using electronegativity of 
    given list of formulas.

    Returns:
            A pandas dataframe with features of given list.'''
    
    composition_list = []
    composition_list.append([Composition(i) for i in lst])
    feture_list =[]
    feture_list.append([bc.featurize(j) for j in composition_list[0]])
    df = pd.DataFrame(feture_list[0])
    df['formula'] = lst
    df1st = df.pop('formula') 
    df.insert(0, 'formula', df1st)
    return df

