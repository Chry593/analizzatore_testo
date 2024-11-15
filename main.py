import pdfminer
import pdfplumber

def lista_parole_da_pdf(path: str) -> list[str]:
    risultato = ""
    with pdfplumber.open(path) as pdf:
        for pagina in pdf.pages:
            risultato += pagina.extract_text()
    return risultato.lower().split()
    

def lista_parole_da_txt(path: str) -> list[str]:
    with open(path,"r") as f:
        return f.read().lower().split()
    


def conta_parole(lista_parole : list[str]) -> dict[str,int]:
    conteggio = {}
    for parola in lista_parole:
        if parola not in conteggio:
            conteggio[parola] = 1
        else:
            conteggio[parola] += 1
    return dict(sorted(conteggio.items(), key=lambda item: -item[1])[:6])


def crea_grafico(lista_parole,conteggio_parole):
    import matplotlib.pyplot as plt
    
    plt.bar(lista_parole,conteggio_parole)
    plt.title("Grafico conteggio delle parole")
    plt.xlabel("Parole")
    plt.ylabel("Numero di volte che la parola e' presente nel testo")
    plt.show()

def main():
    scelta = int(input("Analizzatore di testi, che tipo di file vuoi analizzare:\n1 Pdf\n2 txt\n"))
    if scelta == 1:
        path = str(input("Inserisci il path completo del file pdf:\n"))
        try:
            risultato = conta_parole(lista_parole_da_pdf(path))
            print(f"Le 5 parole piu' presenti nel file sono: {risultato}")
        except FileNotFoundError:
            print("Path errato, riprova")
        except pdfminer.pdfparser.PDFSyntaxError:
            print("Tipo di file errato")
    elif scelta == 2:
        path = str(input("Inserisci il path completo del file txt:\n"))
        try:
            risultato = conta_parole(lista_parole_da_txt(path))
            print(f"Le 5 parole piu' presenti nel file sono: {risultato}")
        except FileNotFoundError:
            print("Path errato, riprova")
        except UnicodeDecodeError:
            print("Tipo di file errato")
    else:
        print("Scelta non valida")

    crea_grafico(list(risultato.keys()),list(risultato.values()))

if __name__ == "__main__":
    main()
        
    
