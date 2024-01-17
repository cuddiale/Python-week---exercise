#Inserisci un numero intero n in input:
#-Se n è dispari stampa weird
#-Se n è pari e contenuto all'interno del range che va da 2 a 5 stampa Not Weird
#-Se n è pari e incluso nel range che va da 6 a 20 stampa weird
#-se n è pari e maggiore di 20 stampa not weird


n = int(input("inserisci un numero intero: "))

if n%2 == 1:
    print("Weird")

elif n%2 == 0 and n>= 2 and n<=5:
    print("not weired")

elif n%2 == 0 and n>= 6 and n<=20:
    print("weired")

elif n%2 == 0 and n>= 20:
    print("not weired")

