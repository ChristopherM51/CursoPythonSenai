import pandas as pd

igm = pd.read_csv("Aula7/igm_modificado.csv")
print(igm['indice_governanca'])

ind_des = igm['indice_governanca']

ind_des_notnull = ind_des.dropna(inplace=True)
print(ind_des_notnull.count())
print(ind_des_notnull.size)