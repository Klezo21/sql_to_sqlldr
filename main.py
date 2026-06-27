import os
import config
from parser import SQLParser
from csv_generator import CSVGenerator
from ctl_generator import CTLGenerator
from batch_generator import BatchGenerator
from report_generator import ReportGenerator

def exécuter_pipeline():
    print("\U0001f680 Initialisation du pipeline...")
    config.initialiser_dossiers()
    
    fichiers = [f for f in os.listdir(config.INPUT_DIR) if f.endswith('.sql')]
    if not fichiers:
        print(f"❌ Aucun fichier .sql trouvé dans le dossier : {config.INPUT_DIR}")
        return

    bilans = {}
    tables_traitees = []

    for fichier in fichiers:
        chemin_sql = os.path.join(config.INPUT_DIR, fichier)
        parser = SQLParser(chemin_sql)
        
        print(f"⚡ Analyse de {parser.table_name}...")
        if not parser.analyser():
            print(f"   ❌ Échec de l'analyse pour {fichier}")
            continue
            
        # Génération du CSV
        csv_gen = CSVGenerator(parser.table_name, parser.colonnes, parser.donnees)
        total_lignes = csv_gen.generer()
        
        # Génération du CTL
        ctl_gen = CTLGenerator(parser.table_name, parser.colonnes, parser.donnees)
        ctl_gen.generer()
        
        # Stockage du bilan pour le rapport final
        tables_traitees.append(parser.table_name)
        bilans[parser.table_name] = {
            "lignes": total_lignes,
            "anomalies": parser.anomalies
        }
    
    # Génération des fichiers globaux (Orchestration Bat & Rapport)
    print("📦 Création du script d'orchestration Windows (run_loader.bat)...")
    batch_gen = BatchGenerator(tables_traitees)
    batch_gen.generer()
    
    print("📝 Rédaction du rapport d'intégration...")
    report_gen = ReportGenerator(bilans)
    report_gen.generer()
    
    print("\n🎉 Fin du traitement ! Ouvrez le dossier 'output/' pour exécuter votre batch.")

if __name__ == "__main__":
    exécuter_pipeline()