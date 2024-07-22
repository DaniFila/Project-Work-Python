import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Parco:
    def __init__(self):
        self.df = self.crea_df()
    
    def crea_df(self):
        incremento = np.linspace(0,10,365) # creo un array con numeri da 0 a 2 di 365 che sommerrò ai visitatori
        visitatori_giornalieri = np.random.normal(2000,500,365) + incremento # creo un array con numero di visitatori casuali che stanno di media intorno i 2000 con una deviazione standard di 500 e ne genero in totale 365 e aggiungo l'incremento a ogni giorno
        date = pd.date_range(start="2024-01-01",periods=365) # creo un array di date che partono dal primo gennaio del 2024 e finisco all'ultimo giorno dell'anno
        df = pd.DataFrame(visitatori_giornalieri,index=date,columns=["Visitatori"]) # creo il dataframe con la colonna date come indice e con i visitatori giornalieri messi in colonna Visitatori
        return df
    
    def visitatori_per_mese(self):
        visitatori_medi_per_mese = self.df["Visitatori"].resample("ME").mean()
        visitatori_medi_per_mese_df = visitatori_medi_per_mese.to_frame(name="Media Visitatori Mensili")
        return visitatori_medi_per_mese_df
    def deviazione_standard_mensile(self):
        deviazione_standard_mensile = self.df["Visitatori"].resample("ME").std()
        deviazione_standard_mensile_df = deviazione_standard_mensile.to_frame(name="Deviazione Standard Mensile")
        return deviazione_standard_mensile_df
    def media_mobile(self):
        # sfrutto un metodo di pandas per creare una nuova colonna dove inserirò la media mobile a 7 giorni dei visitatori
        self.df["Media Mobile Visitatori 7 giorni"] = self.df["Visitatori"].rolling(window=7).mean()
        print("Colonna creata con successo!")

    def grafico_linee(self):
        plt.figure(figsize=(12,6))
        plt.plot(self.df.index,self.df["Visitatori"],label="Visitatori Giornalieri")
        plt.plot(self.df.index, self.df["Media Mobile Visitatori 7 giorni"], label='Media Mobile 7 Giorni')
        plt.xlabel("Data")
        plt.ylabel("Numero di Visitatori")
        plt.title("Numero di Visitatori Giornalieri con Media Mobile di 7 Giorni")
        plt.show()
    
    def visual_media_mensile(self):
        visitatori_medi_per_mese = self.visitatori_per_mese()
        sns.barplot(x=visitatori_medi_per_mese.index,y="Media Visitatori Mensili",data=visitatori_medi_per_mese)
        plt.xlabel("Data")
        plt.ylabel("Media")
        plt.title("Visitatori Medi Mensili")
        plt.show()
    def visual_deviazione_mensile(self):
        visitatori_deviazione_mensile = self.deviazione_standard_mensile()
        sns.barplot(x=visitatori_deviazione_mensile.index,y="Deviazione Standard Mensile",data=visitatori_deviazione_mensile)
        plt.xlabel("Data")
        plt.ylabel("Deviazione")
        plt.title("Deviazione Standard Mensile")
        plt.show()





