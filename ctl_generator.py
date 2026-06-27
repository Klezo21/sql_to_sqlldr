import os
import config

class CTLGenerator:
    def __init__(self, table_name, colonnes, donnees_exemples):
        self.table_name = table_name.upper()
        self.colonnes = colonnes
        self.donnees_exemples = donnees_exemples
        self.filepath = os.path.join(config.CONTROL_DIR, f"charger_{table_name.lower()}.ctl")

    def _deviner_type_date(self, index_colonne):
        """Regarde la première ligne de données pour identifier si c'est un TIMESTAMP ISO ou une DATE."""
        if not self.donnees_exemples:
            return "DATE"
        valeur = self.donnees_exemples[0][index_colonne]
        if 'T' in valeur and any(char.isdigit() for char in valeur):
            return "TIMESTAMP"
        return "DATE"

    def generer(self):
        """Construit le fichier de contrôle .ctl."""
        colonnes_formattees = []
        for idx, col in enumerate(self.colonnes):
            if "DATE" in col or "TIME" in col or "TIMESTAMP" in col:
                if self._deviner_type_date(idx) == "TIMESTAMP":
                    colonnes_formattees.append(f'{col} TIMESTAMP "YYYY-MM-DD\\"T\\"HH24:MI:SS.FF"')
                else:
                    colonnes_formattees.append(f'{col} DATE "YYYY-MM-DD"')
            else:
                colonnes_formattees.append(col)

        liste_colonnes_txt = ",\n  ".join(colonnes_formattees)
        
        # Définition des chemins relatifs pour l'exécution depuis le dossier output/
        contenu_ctl = f"""OPTIONS (DIRECT=TRUE)
LOAD DATA
CHARACTERSET AL32UTF8
INFILE 'data/{self.table_name.lower()}.csv'
BADFILE 'bad/{self.table_name.lower()}.bad'
DISCARDFILE 'discard/{self.table_name.lower()}.dsc'
APPEND
INTO TABLE {self.table_name}
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
  {liste_colonnes_txt}
)
"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(contenu_ctl)