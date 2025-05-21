#Config_FR.py

import sys
from datetime import datetime

# Assignation des arguments
year = "sys.argv[1]"
ssis_user = "sys.argv[2]"
ssis_password = "sys.argv[3]"
postgres_user = "sys.argv[4]"
postgres_password = "sys.argv[5]"

#Année
YEAR_START=2020
YEAR_END=int(datetime.now().year)

#URL de connexion
URL_SERVER_VT="Serveur VT"
DATABASE_VT="DB VT"
URL_SERVER_POSTGRE="Serveur Postgre"
DATABASE_POSTGRE="DB Postgre"



# Messages de sortie
OK_MESSAGE = "Le nombre de transactions est OK."
KO_MESSAGE = "Le nombre de transactions est KO."

# Messages et configuration directement nécessaires pour vérifier les arguments
USAGE_MESSAGE = (
    "Il faut 5 paramètres : python script.py <année> <id_VT> <mdp_VT> <id_postgre> <mdp_postgre>\n"
    "Exemple : python script.py 2023 user_VT pass_VT user_pg pass_pg"
)
ERROR_YEAR = "Le 1er argument doit être une année valide (4 chiffres, >= 2020)."


INFO_MESSAGE_NO_PARAM=" Il n'y a pas de paramètres"