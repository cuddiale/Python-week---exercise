#Scriviamo un programma che richieda i tuoi dati e li stampi su schermo
#i dati che il programma deve richiedere sono:
#-Nome e Cognome
#-Anno di nascita
#-Luogo di nascita
#-Altezza (in metri)
#-Peso (in kg)

#infine il programma dovrà stampare tutte queste informazioni, 
#con altezza e peso arrotondate a 2 cifre dopo la virgola
#insieme all'età della persona.

#Imposto gli input per la raccolta dati.

Nome = str(input("Inserisci il tuo nome: "))
Cognome = str(input("Inserisci il tuo Cognome: "))
Anno_Nascita = int(input("Inserisci il tuo Anno di nascita: "))
Luogo_Nascita = str(input("Inserisci il luogo dove sei nato: "))
Altezza = float(input("Inserisci la tua altezza (m): "))
Peso = float(input("Inserisci il tuo peso (kg): "))

#stampo le variabili

print(Nome)
print(Cognome)
print(Anno_Nascita)
print(Luogo_Nascita)
print(Altezza)
print(Peso)