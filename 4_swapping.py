#Lo swapping consiste nell'invertire il valore di due variabili
#-prendi in input due valori e assegnali a due variabili A e B 
#-Stampa le variabili su schermo
#-Assegna il valore di A a B ed il valore di B ad A
#-Stampa le variabili su schermo

#Creo le variabili in input

A = input("inserisci un Valore: ")
B = input("inserisci un Valore: ")

#Stampo le due variabili

print("Questo è il tuo primo valore: ", A)
print("Questo è il tuo secondo valore: ", B)

#inverto i due valori

A,B = B,A

#Stampo le variabili invertite

print("Questo è il tuo primo valore: ", A)
print("Questo è il tuo secondo valore: ", B)
