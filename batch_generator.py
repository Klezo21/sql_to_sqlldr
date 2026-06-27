import os
import config

class BatchGenerator:
    def __init__(self, tables_traitees):
        self.tables_traitees = tables_traitees
        self.filepath = os.path.join(config.OUTPUT_DIR, "run_loader.bat")

    def generer(self):
        """Génère le fichier de commande .bat orchestré selon config.LOADING_ORDER."""
        # On ne trie que les tables qui ont été effectivement parsées et générées
        ordre_execution = [t for t in config.LOADING_ORDER if t in self.tables_traitees]
        
        # Ajoute à la fin les tables qui n'auraient pas été spécifiées dans config.LOADING_ORDER
        for t in self.tables_traitees:
            if t not in ordre_execution:
                ordre_execution.append(t)

        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write("@echo off\n")
            f.write("echo ===================================================\n")
            f.write("echo   Lancement du chargement de la base Oracle        \n")
            f.write("echo ===================================================\n\n")
            
            for table in ordre_execution:
                t_lower = table.lower()
                f.write(f"echo Chagement de la table {table}...\n")
                f.write(f"sqlldr userid={config.ORACLE_USER}/{config.ORACLE_PASS}@{config.ORACLE_DSN} "
                        f"control=control/charger_{t_lower}.ctl log=logs/charger_{t_lower}.log\n\n")
            
            f.write("echo ===================================================\n")
            f.write("echo   Chargement terminé ! Vérifiez le dossier logs/   \n")
            f.write("echo ===================================================\n")
            f.write("pause\n")