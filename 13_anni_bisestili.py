# Ogni 4 anni aggiungiamo un giorno al mese più breve dell'anno, cioè febbraio,
# quest'anno è chiamato bisestile.
# I criteri utilizzati per definire se un anno è bisestile sono i seguenti:
# -l'anno è divisibile per 4, allora è bisestile a meno che: 
#     - l'anno è divisibile per 100, allora non è bisestile a meno che: 
#         - l'anno è divisibile per 400

# scrivi una funziona per verificare se un anno è bisestile


def is_leap(year):
    leap = False

    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True
        
        else:
            leap = True

    return leap

year = int(input("Inserisci l'anno: "))
leap = is_leap(year)

if leap:
    print(f"il {year} è bisestile")

else:
    print(f"il {year} NON è bisestile")
    