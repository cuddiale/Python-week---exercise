# Leggi un float a un intero b come input e stampa
# -a elevato b 
# il modulo di a per b  

#creo le variabili input

a = float(input("inserisci un numero: "))
b = int(input("inserisci un numero: "))

#definisco le operazioni

potenza= a**b
modulo = a%b

#stampo a schermo le operazioni

print(potenza)
print(modulo)