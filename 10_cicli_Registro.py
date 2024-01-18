# Hai a disposizione un record di N studenti.
# Ogni record contiene il nome dello studente e il suo voto in Matematica, Fisica e Chimica.
# I voti possono essere nnumeri con la virgola.
# Un utente inserisce un intero N seguito da il nome e i voti di N studenti.
# Il programma deve salvare i record in un dizionario.
# Alla fine l'utente inserirà il none di uno studente, il programma dovrà dare l'output la media dei voti di tale studente arrotondata a due cifre dopo la virgola.

student_marks = {}

n = int(input())

for _ in range(n):      #il trattino è perche non usiamo i
    record = input()
    record = record.split()
    name = record[0]
    marks = list(map(float, record[1:]))
    student_marks[name] = marks

query_name = input()
avg_mark = sum(student_marks[query_name])/len(student_marks[query_name])           #sum fa la somma
print(f"{avg_mark:2.f}")