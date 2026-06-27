import os

# --- Structure des Dossiers ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

DATA_DIR = os.path.join(OUTPUT_DIR, "data")
CONTROL_DIR = os.path.join(OUTPUT_DIR, "control")
LOGS_DIR = os.path.join(OUTPUT_DIR, "logs")
BAD_DIR = os.path.join(OUTPUT_DIR, "bad")
DISCARD_DIR = os.path.join(OUTPUT_DIR, "discard")
REPORT_DIR = os.path.join(OUTPUT_DIR, "report")

# --- Configuration Oracle ---
ORACLE_USER = "SaintVil"
ORACLE_PASS = "Mura99son"
ORACLE_DSN = "localhost:1521/FREEPDB1"

# --- Ordre de chargement des tables (Contraintes d'intégrité) ---
# Mettez les tables indépendantes en premier, et les tables dépendantes (ventes, détails) à la fin.
LOADING_ORDER = [
    "MAGASIN",
    "CLIENT",
    "EMPLOYE",
    "CATEGORIE",
    "PRODUIT",
    "PROMOTION",
    "STOCKER",
    "VENTE",
    "LIGNE_VENTE",
    "LOG_ACTIVITE"
]

def initialiser_dossiers():
    """Crée l'arborescence des dossiers si elle n'existe pas."""
    dossiers = [INPUT_DIR, DATA_DIR, CONTROL_DIR, LOGS_DIR, BAD_DIR, DISCARD_DIR, REPORT_DIR]
    for d in dossiers:
        os.makedirs(d, exist_ok=True)