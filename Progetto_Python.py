import pandas as pd
import numpy as np

class DataSet:
    def __init__(self,nome_file):
        self.df = pd.read_csv(nome_file)
    
    def save_csv(self,nome_file):
        self.df.to_csv(nome_file,index=False)
        print("Salvato con successo!")
    
    def esplorazione_dati(self):
        print("\nDescrizione generale del Dataset:\n")
        print(f"Informazioni:\n{self.df.info()}\n")
        print(f"Statistiche:\n{self.df.describe()}\n")
        print(f"Stato clienti nella compagnia:\n{self.df['Churn'].value_counts()}\n")

    #def pulizia_dati(self):


#a = DataSet("Corso Python/Giovedì 18/Progetto_Python_1.csv")

#a.esplorazione_dati()