# # Ricevi in input una lista con i punteggi dei partecipanti alla Giornata dello Sport Universitaria, 
# trova il punteggio del secondo classificato.

scores = input("Inserisci una lista: ")
scores = scores.split()

#rimuovo i duplicati

scores = set(map(int, scores))

for i in scores:
    larger = 0
    for j in scores:
        if i<j:
            larger+=1
    
    if larger == 1:
        break

print(i)

#soluzione 2

scores = input("Inserisci una lista: ")
scores = scores.split()
scores = set(map(int, scores))      #rimuovendo i duplicati così perdiamo l'ordine, quindi dobbiamo fare attenzione all'ordine
scores = list(scores)

scores.sort(reverse = True)       #ordiniamo la lista
print(scores[1])


#rimuovere i duplicati mantenendo l'ordine originale

# scores = dict.fromkeys(map(int, scores))












