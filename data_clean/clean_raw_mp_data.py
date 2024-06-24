import pandas as pd
def clean_mp_raw(df):

    df_cleaned = df.copy()
    df_cleaned['a'] = 0
    df_cleaned['b'] = 0
    df_cleaned['c'] = 0
    df_cleaned['alpha'] = 0
    df_cleaned['beta'] = 0
    df_cleaned['gamma'] = 0
    
    for i in range(len(df_cleaned)):
            
        df_cleaned['nsites'][i] = float(df_cleaned['nsites'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['elements'][i] = df_cleaned['elements'][i].replace('(','').replace(')','').replace("'","").replace('[', '').replace(']','').replace(', Element','').split(' ')[1:]
        df_cleaned['nelements'][i] = float(df_cleaned['nelements'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['composition'][i] = df_cleaned['composition'][i].split("'")[-2].replace(' ','')#.replace(')','').replace("'","").replace(' ', '')#.split(',')[1]
        df_cleaned['composition_reduced'][i] = df_cleaned['composition_reduced'][i].split("'")[-2].replace(' ','')#.
        df_cleaned['formula_pretty'][i] = df_cleaned['formula_pretty'][i].split("'")[-2]#.replace(' ','')#.
        df_cleaned['formula_anonymous'][i] = df_cleaned['formula_anonymous'][i].split("'")[-2]#.
        df_cleaned['chemsys'][i] = df_cleaned['chemsys'][i].split("'")[-2]#.
        df_cleaned['volume'][i] = float(df_cleaned['volume'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['density'][i] = float(df_cleaned['density'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['density_atomic'][i] = float(df_cleaned['density_atomic'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['symmetry'][i] = df_cleaned['symmetry'][i].split("=")[1].replace("'",'').replace('>','').replace(',','').split(' ')[-2]#.
    
        df_cleaned['material_id'][i] = df_cleaned['material_id'][i].replace("('","").replace("', MPID(", " ").replace('))','').split(" ")[-1]#.
        df_cleaned['a'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[4]) 
        df_cleaned['b'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[5]) 
        df_cleaned['c'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[6]) 
        df_cleaned['alpha'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[8]) 
        df_cleaned['beta'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[9]) 
        df_cleaned['gamma'][i] = float(df_cleaned['structure'][i].replace("\n","").replace(":","").replace("    "," ").replace("  "," ").split(" ")[10]) 
    
        df_cleaned['uncorrected_energy_per_atom'][i] = float(df_cleaned['uncorrected_energy_per_atom'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['energy_per_atom'][i] = float(df_cleaned['energy_per_atom'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['formation_energy_per_atom'][i] = float(df_cleaned['formation_energy_per_atom'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['energy_above_hull'][i] = float(df_cleaned['energy_above_hull'][i].replace('(','').replace(')','').replace("'","").replace(' ', '').split(',')[1])
        df_cleaned['is_stable'][i] = df_cleaned['is_stable'][i].replace(')','').split(", ")[-1]#.
    
    return df_cleaned 
