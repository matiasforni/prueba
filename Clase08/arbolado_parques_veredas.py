import pandas as pd
import matplotlib.pyplot as plt
import os

fname = os.path.join('Data','arboladoenespaciosverdes.csv')
df_parques = pd.read_csv(fname,low_memory=False)
fname = os.path.join('Data','arbolado-publico-lineal-2017-2018.csv')
df_veredas = pd.read_csv(fname,low_memory=False)
df_tipas_parques = (df_parques[['altura_tot','diametro']])[df_parques['nombre_cie'] == 'Tipuana Tipu'].copy()
df_tipas_parques.rename(columns= {'altura_tot':'altura'}, inplace = True)
df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas = (df_veredas[['altura_arbol','diametro_altura_pecho']])[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()
df_tipas_veredas.rename(columns={'altura_arbol':'altura', 'diametro_altura_pecho':'diametro'}, inplace = True)
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas = pd.concat([df_tipas_veredas,df_tipas_parques])
df_tipas.boxplot('diametro', by = 'ambiente')
plt.show()
