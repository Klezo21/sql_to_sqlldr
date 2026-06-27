import os
import csv
import config

class CSVGenerator:
    def __init__(self, table_name, colonnes, donnees):
        self.table_name = table_name.lower()
        self.colonnes = colonnes
        self.donnees = donnees
        self.filepath = os.path.join(config.DATA_DIR, f"{self.table_name}.csv")

    def generer(self):
        """Écrit les données nettoyées dans le fichier CSV cible."""
        with open(self.filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            # Pas d'en-tête pour faciliter l'intégration brute dans SQL*Loader
            writer.writerows(self.donnees)
        return len(self.donnees)