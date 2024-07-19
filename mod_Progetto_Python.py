import Progetto_Python as P

def menu(): # funzione menù che stampa le possibili scelte e richiede all'utente la selezione
    info = """1: Visualizza DataSet
2: Informazioni DataSet    
3: Aggiungi Colonna Costo_per_GB
4: Pulisci i Dati
5: Prepara i Dati alla modellazione
6: Esplorazione dei Dati
7: Visualizza statistiche Età
8: Visualizza statistiche Tariffe Mensili
9: Analisi Statistica e Predittiva
0: Exit
Indicare la scelta: """
    s = input(info)
    return s

def main(): # funzione main che richiama tutte le altre funzioni e il modulo importato
    df = P.DataSet("Corso Python/Giovedì 18/Progetto_Python_1.csv")
    try:
        print(f"\nAnteprima Dataset Importato:\n{df.df.head()}\n")
        while True:
            s = menu()
            if s == "1":
                print(f"\nIl Tuo Dataset:\n{df.df}")
            elif s == "2":
                df.info()
            elif s == "3":
                df.aggiungi_colonna_costo_per_GB()
            elif s == "4":
                df.pulizia_dati()
            elif s == "5":
                df.preparazione_dati()
            elif s == "6":
                df.esplorazione_dati()
            elif s == "7":
                df.visualizza_statistiche_età()
            elif s == "8":
                df.visualizza_statistiche_tariffe_mensili()
            elif s == "9":
                df.regressione_logistica()
            elif s == "0":
                print("\nArrivederci!")
                break
            else:
                print("\nErrore!\n")
    except:
        pass

main()
