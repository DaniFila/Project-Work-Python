import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Parco:
    def __init__(self): # metodo costruttore
        self.df = self.crea_df()
    
    def crea_df(self): # metodo che crea il dataframe
        incremento = np.linspace(0,10,365) # creo un array con numeri da 0 a 2 di 365 che sommerrò ai visitatori
        visitatori_giornalieri = np.random.normal(2000,500,365) + incremento # creo un array con numero di visitatori casuali che stanno di media intorno i 2000 con una deviazione standard di 500 e ne genero in totale 365 e aggiungo l'incremento a ogni giorno
        date = pd.date_range(start="2024-01-01",periods=365) # creo un array di date che partono dal primo gennaio del 2024 e finisco all'ultimo giorno dell'anno
        df = pd.DataFrame(visitatori_giornalieri,index=date,columns=["Visitatori"]) # creo il dataframe con la colonna date come indice e con i visitatori giornalieri messi in colonna Visitatori
        return df
    
    def visitatori_per_mese(self): # metodo che crea un dataframe con la media mensile dei visitatori per utilizzarlo per generare il grafico
        try:
            visitatori_medi_per_mese = self.df["Visitatori"].resample("ME").mean()
            visitatori_medi_per_mese_df = visitatori_medi_per_mese.to_frame(name="Media Visitatori Mensili")
            return visitatori_medi_per_mese_df
        except:
            print("Errore, non è stato possibile calcolare la media mensile dei visitatori!")
    
    def deviazione_standard_mensile(self): # metodo che crea un dataframe con la deviazione standard dei visitatori per utilizzarlo per generare il grafico
        try:
            deviazione_standard_mensile = self.df["Visitatori"].resample("ME").std()
            deviazione_standard_mensile_df = deviazione_standard_mensile.to_frame(name="Deviazione Standard Mensile")
            return deviazione_standard_mensile_df
        except:
            print("Errore, non è stato possibile calcolare la devianza mensile dei visitatori!")
    
    def media_mobile(self): # metodo che crea la colonna della media mobile dei visitatori di 7 giorni
        try:
            # sfrutto un metodo di pandas per creare una nuova colonna dove inserirò la media mobile a 7 giorni dei visitatori
            self.df["Media Mobile Visitatori 7 giorni"] = self.df["Visitatori"].rolling(window=7).mean()
            print("\nColonna creata con successo!")
        except:
            print("Errore, non è stato possibile creare la nuova colonna!")

    def grafico_linee(self): # metodo che visualizza un grafico a linee con i visitatori giornalieri e al suo interno anche la media mobile
        try:
            plt.figure(figsize=(12,6))
            plt.plot(self.df.index,self.df["Visitatori"],label="Visitatori Giornalieri")
            plt.plot(self.df.index, self.df["Media Mobile Visitatori 7 giorni"], label='Media Mobile 7 Giorni')
            plt.xlabel("Data")
            plt.ylabel("Numero di Visitatori")
            plt.title("Numero di Visitatori Giornalieri con Media Mobile di 7 Giorni")
            plt.show()
        except:
            print("\nCreare prima colonna della Media mobile Visitatori!")
    
    def visual_media_mensile(self): # metodo che visualizza un grafico a barre della media mensile dei visitatori
        try:
            visitatori_medi_per_mese = self.visitatori_per_mese()
            sns.barplot(x=visitatori_medi_per_mese.index,y="Media Visitatori Mensili",data=visitatori_medi_per_mese)
            plt.xlabel("Data")
            plt.ylabel("Media")
            plt.title("Visitatori Medi Mensili")
            plt.show()
        except:
            print("\nErrore, non è stato possibile visualizzare il grafico!")

    def visual_deviazione_mensile(self): # metodo che visualizza un grafico a barre della deviazione standard dei visitatori
        try:
            visitatori_deviazione_mensile = self.deviazione_standard_mensile()
            sns.barplot(x=visitatori_deviazione_mensile.index,y="Deviazione Standard Mensile",data=visitatori_deviazione_mensile)
            plt.xlabel("Data")
            plt.ylabel("Deviazione")
            plt.title("Deviazione Standard Mensile")
            plt.show()
        except:
            print("\nErrore, non è stato possibile visualizzare il grafico!")


def menu(): # funzione che genera un menù e chiede all'utente in input la scelta
    inf = """\n1: Visualizza Anteprima DataFrame
2: Crea colonna Media Mobile
3: Visualizza Grafico dei Visitatori
4: Visualizza Grafico delle media mensile dei Visitatori
5: Visualizza Grafico della deviazione mensile dei Visitatori
0: Exit
"""
    s = input(inf)
    return s

def main(): # funzione main che richiama la classe e la funzione menu con le varie scelte
    p = Parco()
    while True:
        s = menu()
        if s == "1":
            print(f"\nAnteprima DataFrame\n{p.df}")
        elif s == "2":
            p.media_mobile()
        elif s == "3":
            p.grafico_linee()
        elif s == "4":
            p.visual_media_mensile()
        elif s == "5":
            p.visual_deviazione_mensile()
        elif s == "0":
            break
        else:
            print("Error")

main()