# ComparisonVTPG_FR

Ce script Python permet de comparer les nombres de transactions entre la  base de données **VT (SQL Server)** (données brutes) et la base **PostgreSQL** (données transformées) pour s'assurer de la cohérence des données. 

---

    ## Structure du projet

├── ComparisonVTPG_FR.py # Script principal de comparaison
├── Connexions_FR.py # Fonctions d'accès aux bases de données
├── Functions_FR.py # Fonctions utilitaires (connexion, validation)
├── Config_FR.py # Paramètres globaux et messages


    ## Exécution

```bash
python ComparisonVTPG_FR.py <année> <utilisateur_ssis> <mdp_ssis> <utilisateur_pg> <mdp_pg>

Exemple : python ComparisonVTPG_FR.py 2023 ssis_user ssis_pwd pg_user pg_pwd

Avec 
- <année> : Année de départ (au format YYYY, minimum 2020)
- Les identifiants suivants sont nécessaires pour les connexions aux bases de données :
        - SSIS (SQL Server) : utilisateur_ssis + mdp_ssis
        - PostgreSQL : utilisateur_pg + mdp_pg


    ## Fonctionnement

1- Validation des arguments
    - Vérifie qu'au moins 5 arguments sont fournis
    - Vérifie que l'année est au bon format et >= 2020

2- Connexion aux bases de données
    - SQL Server (VT / SSIS)
    - PostgreSQL (PG Retail)

3- Comparaison hiérarchique
    - Comparaison du nombre de transactions :
            - Par année
            - Si différence : par mois
            - Si différence : par jour

4- Messages affichés
    - OK: même nombre de transactions entre les bases
    - KO: différences détectées, précisions affichées

    ## Configuration

La configuration est centralisée dans le fichier Config_FR.py :
    - Informations de connexion
    - Requêtes SQL (cinémas exclus, catégories de transactions, etc.)
    - Messages personnalisés
