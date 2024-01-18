# Leggi un intero N compreso fra 1 e 20 in input. 
# Per tutti gli interi non negativi i<N stampare i^2.


n = int(input("inserisci un numero compreso fra 1 e 20: "))
        
if n<1 or n>20:
    print("Il numero deve essere compreso fra 1 e 20")

else:
    for i in range (n):
        print(i**2)

