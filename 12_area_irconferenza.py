# Definisci una funzione che, prendendo in input il raggio, restituisce l'area della circonferenza.

def circle_area( R ):
    return 3.14*(R**2)

R = float(input("inserisci il valore del raggio: "))

area = circle_area( R )

print(f"Area della circonferenza di raggio {R} è pari a {area}")


















