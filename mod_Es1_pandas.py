import pandas as pd
import numpy as np
class DatiVendite: # classe DatiVendite
    def __init__(self): # metodo costruttore con 3 liste di date, città e prodotti e un attributto che richiama il metodo crea df
        self.date = ["2023-01-01", "2023-05-15","2023-07-22","2023-10-30","2023-12-25"]
        self.città = ["Roma","Milano","Firenze","Napoli"]
        self.prodotti = ["Laptop","Smartphone","Tablet","Smartwatch","Cuffie"]
        self.df = self.crea_df()
    def crea_df(self): # metodo che sceglie randomicamente elementi dalle liste del costruttore e genera un dataframe
        data = {"Data":np.random.choice(self.date,10),
                "Città":np.random.choice(self.città,10),
                "Prodotto":np.random.choice(self.prodotti,10),
                "Vendite":np.random.randint(0,20,10)}
        df = pd.DataFrame(data)
        return df
    def tabella_pivot(self): # metodo per creare la tabella pivot
        tab_pivot = self.df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
        print(f"Le vendite medie dei prodotti per ciascuna città sono:\n{tab_pivot}")
    def appl_groupby(self): # metodo per creare un raggruppamento con groupby
        groupby = self.df.groupby("Prodotto").agg({"Vendite":"sum"})
        print(f"Le vendite totali per ciascun prodotto sono:\n{groupby}")


