import os
import re
from utils import decouper_valeurs_sql

class SQLParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.table_name = os.path.splitext(self.filename)[0].upper()
        self.colonnes = []
        self.donnees = []
        self.anomalies = []

    def analyser(self):
        """Parse le fichier SQL d'une table."""
        if not os.path.exists(self.filepath):
            return False
            
        with open(self.filepath, 'r', encoding='utf-8') as f:
            contenu = f.read()

        # 1. Extraction des colonnes
        pattern_cols = re.compile(r"INSERT\s+INTO\s+\w+\s*\((.*?)\)", re.DOTALL | re.IGNORECASE)
        match_cols = pattern_cols.search(contenu)
        if match_cols:
            self.colonnes = [c.strip().upper() for c in match_cols.group(1).split(',')]
        else:
            self.anomalies.append("Impossible de détecter la structure des colonnes.")
            return False

        # 2. Extraction des blocs VALUES
        pattern_values = re.compile(r"VALUES\s*\((.*?)\);", re.DOTALL | re.IGNORECASE)
        insertions = pattern_values.findall(contenu)

        for idx, bloc in enumerate(insertions, start=1):
            ligne_data = decouper_valeurs_sql(bloc)
            if len(ligne_data) == len(self.colonnes):
                self.donnees.append(ligne_data)
            else:
                self.anomalies.append(f"Ligne {idx} rejetée : incohérence colonnes ({len(ligne_data)} trouvées, {len(self.colonnes)} attendues).")
                
        return True