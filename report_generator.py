import os
import config
from datetime import datetime

class ReportGenerator:
    def __init__(self, bilans):
        self.bilans = bilans
        self.filepath = os.path.join(config.REPORT_DIR, "rapport_generation.txt")

    def generer(self):
        """Génère un rapport textuel propre d'exécution."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(f"===================================================\n")
            f.write(f"  RAPPORT DE GÉNÉRATION PIPELINE SQL*LOADER\n")
            f.write(f"  Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"===================================================\n\n")
            
            for table, info in self.bilans.items():
                f.write(f"📌 TABLE : {table}\n")
                f.write(f"   -> Lignes extraites : {info['lignes']}\n")
                if info['anomalies']:
                    f.write(f"   ⚠️ Anomalies détectées :\n")
                    for ano in info['anomalies']:
                        f.write(f"      - {ano}\n")
                else:
                    f.write(f"   ✅ Structure et données saines.\n")
                f.write("-" * 40 + "\n")