@echo off
echo ===================================================
echo   Lancement du chargement de la base Oracle        
echo ===================================================

echo Chagement de la table MAGASIN...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_magasin.ctl log=logs/charger_magasin.log

echo Chagement de la table CLIENT...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_client.ctl log=logs/charger_client.log

echo Chagement de la table EMPLOYE...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_employe.ctl log=logs/charger_employe.log

echo Chagement de la table CATEGORIE...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_categorie.ctl log=logs/charger_categorie.log

echo Chagement de la table PRODUIT...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_produit.ctl log=logs/charger_produit.log

echo Chagement de la table PROMOTION...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_promotion.ctl log=logs/charger_promotion.log

echo Chagement de la table STOCKER...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_stocker.ctl log=logs/charger_stocker.log

echo Chagement de la table VENTE...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_vente.ctl log=logs/charger_vente.log

echo Chagement de la table LIGNE_VENTE...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_ligne_vente.ctl log=logs/charger_ligne_vente.log

echo Chagement de la table LOG_ACTIVITE...
sqlldr userid=SaintVil/Mura99son@localhost:1521/FREEPDB1 control=control/charger_log_activite.ctl log=logs/charger_log_activite.log

echo ===================================================
echo   Chargement terminé ! Vérifiez le dossier logs/   
echo ===================================================
pause
