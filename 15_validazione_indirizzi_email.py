# Realizziamo una funzione che, prendeno in input una lista di indirizzi email
# ritorni una nuova lista degli indirizzi email validi ordinati alfabeticamente.
# un indirizzo email è valido se:
#     - ha il formato nomeutente@dominio.estensione.
#     - il nome utente contiene soltanto lettere, numeri, lineette(-) e trattini bassi(_)
#     - il dominio contiene soltanto lettere e numero.
#     - la lunghezza massima dell'estensione è 3 ccaratteri.

def valide_email(email):
    parts = email.split("@")

    if len(parts)!=2:
        return False
    
    name, parts = parts

    parts = parts.split(".")

    if len(parts)!=2:
        return False
    
    domain, ext = parts

    if name.replace("-","").replace("_","").isalnum():
        return False
    
    if not domain.isalnum():
        return False
    
    if len(ext)>3:
        return False
    
    return True

def filter_emails(emails):
    valid_emails = list(filter(valide_email, emails))
    valid_emails.sort()
    return valid_emails







