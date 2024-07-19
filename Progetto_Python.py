import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
class DataSet: # classe DataSet

    def __init__(self,nome_file): # classe costruttore dove gli passo il percorso del file
        try:
            self.df = pd.read_csv(nome_file) # col percorso legge il file csv e lo salva in un DataFrame
            self.nome_file = nome_file
            print(f"\nFile: {nome_file} Caricato con successo!")
        except FileNotFoundError:
            print(f"\nFile: {nome_file} non trovato!")
        except:
            print("\nErrore, non è stato possibile caricare il File!")
    
    def save_csv(self,nome_file): # metodo che salva il DataFrame in csv
        try:
            self.df.to_csv(nome_file,index=False)
            print(f"\nFile: {nome_file} Salvato con successo!")
        except:
            print(f"\nErrore: il file {nome_file} non è stato salvato!")
    
    def info(self): # metodo che stampa l'esplorazione dei dati, le info generali del dataframe, le statistiche dei dati, e il count del numero dei clienti in compagnia e non
        try:
            print("\nDescrizione generale del Dataset:\n")
            print(f"Informazioni:\n{self.df.info()}\n")
            print(f"Statistiche:\n{self.df.describe()}\n")
            print(f"Stato clienti nella compagnia:\n{self.df['Churn'].value_counts()}\n")
        except:
            print("\nErrore, non è stato possibile eseguire l'operazione!")

    def pulizia_dati(self): # metodo che pulisce i dati del DataFrame
        # Sostituzione valori mancanti nelle colonne Tariffa Mensile e Dati Consumate
        try:
            self.df['Tariffa_Mensile'].fillna(self.df['Tariffa_Mensile'].median(), inplace=True)
            self.df['Dati_Consumati'].fillna(self.df['Dati_Consumati'].mean(), inplace=True)

            # Eliminazione delle righe con valori mancanti rimasti
            self.df.dropna(inplace=True)
            print("Eliminate righe con Valori mancanti rimasti\n")

            # Correzione di anomalie
            self.df = self.df[self.df['Età'] > 0]
            self.df = self.df[self.df['Tariffa_Mensile'] > 0]
            self.df = self.df[self.df['Dati_Consumati'] >= 0]

            print("DataSet Pulito con successo!\n")
            self.save_csv(self.nome_file)
        except:
            print("\nErrore, non è stato possibile eseguire la pulizia dei dati!")

    def aggiungi_colonna_costo_per_GB(self): # metodo che aggiunge una colonna al DataFrame
        try:
            self.df['Costo_per_GB'] = self.df['Tariffa_Mensile'] / self.df['Dati_Consumati']
            self.save_csv(self.nome_file)
            print("Colonna aggiunta con successo!")
        except:
            print("\nErrore, non è stato possibile aggiungere la colonna!")

    def esplorazione_dati(self): # metodo che esplora i dati del DataFrame, facendo una relazione tra i clienti che sono in compagnia e quelli no, con la media dell'età,durata abbonamento e tariffa mensile, ed effettua una correlazione tra tutti i dati
        try:
            relazione = self.df.groupby("Churn").mean()[['Età', 'Durata_Abonnamento', 'Tariffa_Mensile']]
            self.df['Churn'] = self.df['Churn'].map({'No': 0, 'Sì': 1}) # sostituisco momentaneamente le stringhe NO e SI con 0 e 1 per verificare le possibili correlazioni
            correlazioni = self.df.corr()
            self.df['Churn'] = self.df['Churn'].map({0: "No", 1: "Sì"})
            print(f"\nTabella di relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn:\n{relazione}\n")
            print(f"\nCorrelazioni tra variabili:\n{correlazioni}\n")
        except:
            print("\nErrore, non è stato possibile effettuare l'operazione!")

    def preparazione_dati(self): # metodo che prepara i dati per la modellazione
        try:
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
        except:
            print("\nErrore, non è stato possibile normalizzare le colonne!")
    
    def visualizza_statistiche_età(self):
        try:
            plt.figure(figsize=(10,6)) # inizializzo le dimensioni della figura
            sns.histplot(self.df["Età"],bins=30,kde=True) # Creo un Istogramma della colonna età con 30 bin, cioè che il range di valori sarà suddiviso in 30 intervalli uguali
            plt.title("Distribuzione delle Età:") # definisco il titolo
            plt.xlabel("Età") # Asse X definisco Età
            plt.ylabel("Frequenza") # Asse Y definisco Frequenza
            plt.show() # per mostrare il grafico
        except:
            print("\nErrore, non è stato possibile visualizzare le statistiche relative all'età!")

    def visualizza_statistiche_tariffe_mensili(self):
        try:
            plt.figure(figsize=(10,6)) # inizializzo le dimensioni della figura
            sns.boxplot(x = "Tariffa_Mensile",data=self.df) # Creo un Boxlot 
            plt.title("Grafico Tariffe Mensili") # definisco il titolo
            plt.xlabel("Tariffa Mensile") # definisco il nome dell'asse X
            plt.show() # per mostrare il grafico
        except:
            print("\nErrore, non è stato possibile visualizzare le statistiche relative le tariffe mensili!")

    def regressione_logistica(self):
        # si separano le caratteristiche dall'etichetta
        X = self.df.drop("Churn", axis=1)
        y = self.df["Churn"]
        
        # si dividono i dati in seti di allenamento e di test, la funzione train_test_split divide i dati in set di allenamento e uno per il test
        # test_size = 0.2 indica che il 20% dei dati lo utilizza per il test e il restante per l'allenamento
        # random_state = 42 fa si che la divisione si ripeta
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)

        # con la funzione LogisticRegression() crea un'istanza del modello di regressione logistica cioé l'algoritmo che andremo a utilizzare
        modello = LogisticRegression()

        # con modello.fit si vanno ad addestrare i dati sull'istanza del modello che abbiamo inizializzato
        modello.fit(X_train,y_train)

        # con la funzione predict() restituisce le previsioni binarie per il set di test
        y_pred = modello.predict(X_test)

        # con la funzione predict_proba() restituisce una matrice con 2 colonne, la prima contiene la probabilità per 0, la seconda per 1, utilizzo [:,1] per selezionare la seconda colonna
        y_pred_proba = modello.predict_proba(X_test)[:,1]

        # con la funzione accuracy_score serve a calcolare l'accuratezza del modello e va a confrontare le etichette reali
        accuratezza = accuracy_score(y_test,y_pred)
        print(f"Livello di Accuratezza: {accuratezza}")

        # con la funzione roc_auc_score andiamo a misurare le performance del modello
        # un modello perfetto avrà un AUC di 1.0, invece un modello meno efficace potrebbe essere uguale a 0.5, più questo numero si avvicina a 1 e migliore è la performance del modello

        AUC = roc_auc_score(y_test,y_pred_proba)
        print(f"Livello di AUC: {AUC}")

        # con la funzione classification_report va a stampare un report dettagliato delle metriche di valutazione
        print(f"Rapporto di Classificazione:\n{classification_report(y_test,y_pred)}")