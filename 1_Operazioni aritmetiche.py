# inserisci due interi come input e stampa:
# -La somma dei due numeri.
# -La differenza tra i due numeri(primo-secondo)
# -Il prodotto tra i due numero.


# dichiaro l'input

primo_int = int(input("Inserisci un primo numero intero: "))
secondo_int = int(input("Inserisci un secondo numero intero: "))

# dichiaro le variabili

somma = primo_int+secondo_int
differenza = primo_int-secondo_int
prodotto = primo_int*secondo_int

# possibile output

# print(somma)
# print(differenza)
# print(prodotto)

# output alternativo utilizzando la formattazione

print("La somma dei tuoi due numeri è %d, la differenza fra i due numeri è %d, ed il prodotto dei due numero è %d" %(somma, differenza, prodotto))