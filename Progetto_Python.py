import pandas as pd
import numpy as np

class DataSet: # classe DataSet
    def __init__(self,nome_file): # classe costruttore dove gli passo il percorso del file
        self.df = pd.read_csv(nome_file) # col percorso legge il file csv e lo salva in un DataFrame
        self.nome_file = nome_file
    
    def save_csv(self,nome_file): # metodo che salva il DataFrame in csv
        self.df.to_csv(nome_file,index=False)
        print("Salvato con successo!")
    
    def info(self): # metodo che stampa l'esplorazione dei dati, le info generali del dataframe, le statistiche dei dati, e il count del numero dei clienti in compagnia e non
        print("\nDescrizione generale del Dataset:\n")
        print(f"Informazioni:\n{self.df.info()}\n")
        print(f"Statistiche:\n{self.df.describe()}\n")
        print(f"Stato clienti nella compagnia:\n{self.df['Churn'].value_counts()}\n")

    def pulizia_dati(self): # metodo che pulisce i dati del DataFrame
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

    def aggiungi_colonna_costo_per_GB(self): # metodo che aggiunge una colonna al DataFrame
        self.df['Costo_per_GB'] = self.df['Tariffa_Mensile'] / self.df['Dati_Consumati']
        self.save_csv(self.nome_file)
        print("Colonna aggiunta con successo!")

    def esplorazione_dati(self): # metodo che esplora i dati del DataFrame, facendo una relazione tra i clienti che sono in compagnia e quelli no, con la media dell'età,durata abbonamento e tariffa mensile, ed effettua una correlazione tra tutti i dati
        relazione = self.df.groupby("Churn").mean()[['Età', 'Durata_Abonnamento', 'Tariffa_Mensile']]
        self.df['Churn'] = self.df['Churn'].map({'No': 0, 'Sì': 1}) # sostituisco momentaneamente le stringhe NO e SI con 0 e 1 per verificare le possibili correlazioni
        correlazioni = self.df.corr()
        self.df['Churn'] = self.df['Churn'].map({0: "No", 1: "Sì"})
        print(f"\nTabella di relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn:\n{relazione}\n")
        print(f"\nCorrelazioni tra variabili:\n{correlazioni}\n")

    def preparazione_dati(self): # metodo che prepara i dati per la modellazione
        self.df['Churn'] = self.df['Churn'].map({'No': 0, 'Sì': 1}) # imposto i valori nella colonna Churn con 0 e 1 al posto di Si e NO
        try: # effettuo questa verifica nel caso in cui non fosse stata creata la colonna Costo_per_GB
            colonne = ["ID_Cliente","Età","Durata_Abonnamento","Tariffa_Mensile","Dati_Consumati","Servizio_Clienti_Contatti","Churn","Costo_per_GB"]
            for colonna in colonne:
                self.df[colonna] = (self.df[colonna]- np.mean(self.df[colonna])) / np.std(self.df[colonna]) # normalizzo le colonne scandendo al lista contenenti i nomi delle colonne e andando a usare la formula del valore - la media del valore tutto diviso la deviazione standard
            print("Colonne normalizzate con successo!")
            self.save_csv("Corso Python/Giovedì 18/Progetto_Python_1_ready_modelling.csv") # salvo in un nuovo file i dataframe in formato csv pronto per la modellazione
        except:
            colonne = ["ID_Cliente","Età","Durata_Abonnamento","Tariffa_Mensile","Dati_Consumati","Servizio_Clienti_Contatti","Churn"]
            for colonna in colonne:
                self.df[colonna] = (self.df[colonna]- np.mean(self.df[colonna])) / np.std(self.df[colonna]) 
            print("Colonne normalizzate con successo!")
            self.save_csv("Corso Python/Giovedì 18/Progetto_Python_1_ready_modelling.csv") 




