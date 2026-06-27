import re

def decouper_valeurs_sql(bloc_values):
    """
    Découpe une ligne VALUES en respectant les virgules internes des chaînes de caractères.
    Exemple : (1, 'Jean, l''artiste', '2026-06-27') -> [1, "Jean, l'artiste", "2026-06-27"]
    """
    # Expression régulière pour matcher les chaînes entre single quotes (gère l'échappement Oracle '') ou les nombres
    pattern = re.compile(r"'(?:''|[^'])*'|[^,]+")
    elements = pattern.findall(bloc_values)
    
    resultat = []
    for el in elements:
        el_clean = el.strip()
        if el_clean.startswith("'") and el_clean.endswith("'"):
            # Enlève les quotes externes et remplace les doubles single quotes '' par un apostrophe simple
            el_clean = el_clean[1:-1].replace("''", "'")
        elif el_clean.upper() == "NULL":
            el_clean = ""
        resultat.append(el_clean)
        
    return resultat