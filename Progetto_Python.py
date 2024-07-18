import pandas as pd
import numpy as np

class DataSet:
    def __init__(self,nome_file):
        self.df = pd.read_csv(nome_file)
        self.nome_file = nome_file
    
    def save_csv(self,nome_file):
        self.df.to_csv(nome_file,index=False)
        print("Salvato con successo!")
    
    def esplorazione_dati(self):
        print("\nDescrizione generale del Dataset:\n")
        print(f"Informazioni:\n{self.df.info()}\n")
        print(f"Statistiche:\n{self.df.describe()}\n")
        print(f"Stato clienti nella compagnia:\n{self.df['Churn'].value_counts()}\n")

    def pulizia_dati(self):
        # Sostituzione valori mancanti nelle colonne Tariffa Mensile e Dati Consumate
        self.df['Tariffa_Mensile'].fillna(self.df['Tariffa_Mensile'].median(), inplace=True)
        self.df['Dati_Consumati'].fillna(self.df['Dati_Consumati'].mean(), inplace=True)

        # Eliminazione delle righe con valori mancanti rimasti
        self.df.dropna(inplace=True)
        print("Eliminate righe con Valori mancanti rimasti\n")

        # Correzione di anomalie
        self.df = self.df[self.df['Età'] > 0]
        self.df = self.df[self.df['Tariffa_Mensile'] > 0]
        self.df = self.df[self.df['Dati_Consumati'] > 0]

        print("DataSet Pulito con successo!\n")
        self.save_csv(self.nome_file)






a = DataSet("Corso Python/Giovedì 18/Progetto_Python_1.csv")

#a.esplorazione_dati()

