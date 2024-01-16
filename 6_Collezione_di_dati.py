#Creiamo una struttura dati in grado di contenere i record di diversi studenti.
#La struttura sarà composta da un dizionario, con come chiave il nome dello studente e come valore una lista.
#La lista deve contenere delle tuple e ogni tupla deve avere alla prima posizione il nome della materia,
#alla seconda il voto e alla terza le ore di assenza.

#- Popola la struttura dati
#-Aggiungi alla struttura dati la pagella di un nuovo studente chiamato Albert einstein, con 10 in tutte le materie e nessuna ora di assenza.
#-Aggiungi Fisica a tutte le pagelle con le seguenti votazioni/assenza:
#    -Giuseppe Gullo 9.5/0, Antonio Barbera 8/1, emiliano ruozzo 8/3, albert einstein 10/0.
#-Stampa la tupla con le informazioni sulla materia Matematica per Giuseppe Gullo
#-Stampa la tupla con le informazioni sulla materia inglese per emiliano Ruozzo 
#-Stampa solo il voto di antonio barbera in Geografia


#Creaiamo la struttura dati

studenti = {
    "Giuseppe Gullo": [("Matematica", 9, 0), ("Italiano", 7,3), ("Inglese", 7.5, 4), ("Storia", 7.5, 4), ("Geografia", 5, 7)],
    "Antonio Barbera": [("Matematica", 8, 1), ("Italiano", 6,1), ("Inglese", 9.5, 0), ("Storia", 8, 2), ("Geografia", 8, 1)],
    "Emiliano Ruozzo": [("Matematica", 7.5, 2), ("Italiano", 6,2), ("Inglese", 4, 3), ("Storia", 8.5, 2), ("Geografia", 8, 2)],
}

#Aggiungiamo un nuovo studente con la sua pagella

studenti["Albert Einstain"] = [("Matematica", 10, 0), ("Italiano", 10,0), ("Inglese", 10, 0), ("Storia", 10, 0), ("Geografia", 10, 0)]

#Aggiungiamo una nuova materia a tutte le pagelle

studenti["Giuseppe Gullo"].append(("Fisica", 9.5, 0))
studenti["Antonio Barbera"].append(("Fisica", 8, 1))
studenti["Emiliano Ruozzo"].append(("Fisica", 8, 3))
studenti["Albert Einstain"].append(("Fisica", 10, 0))

#Stampo la tupla con le informazioni sulla materia Matematica per Giuseppe Gullo

print(studenti["Giuseppe Gullo"][0])

#Stampo la tupla con le informazioni sulla materia inglese per emiliano Ruozzo 

print(studenti["Emiliano Ruozzo"][2])

#Stampo solo il voto di antonio barbera in Geografia

print(studenti["Antonio Barbera"][4][1])
