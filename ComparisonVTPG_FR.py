
import sys
import Functions_FR
import Config_FR
from Config_FR import YEAR_START, YEAR_END

# Validation des arguments
Functions_FR.NoArgument()  # Vérifie qu'au moins un argument est fourni
print(sys.argv[0])

# Validation spécifique du 1er argument (année)
Functions_FR.check_year_argument(sys.argv[1])  # Vérifie que l'année est valide

# Assignation des arguments après validation
Config_FR.year = sys.argv[1]
Config_FR.ssis_user = sys.argv[2]
Config_FR.ssis_password = sys.argv[3]
Config_FR.postgres_user = sys.argv[4]
Config_FR.postgres_password = sys.argv[5]

# Conversion de l'année en entier
Config_FR.year = int(Config_FR.year)


# Importations supplémentaires après validation des arguments
import traceback
from datetime import datetime, timedelta
import Connexions_FR
import Functions_FR
import Config_FR



def compare_transactions():

    # Connexion aux bases de données
    ssis_conn = Functions_FR.connect_to_ssis()
    postgres_conn = Functions_FR.connect_to_postgres()
    print("Connexion à VT réussie")
    print("Connexion à PostgreSQL réussie")

    #ici, définir une boucle pour l'année :
    while Config_FR.year < YEAR_END:
        try:
            # Comparaison des transactions pour l'année
            print(f"Comparaison pour l'année {Config_FR.year}...")
            ssis_transaction_count = Connexions_FR.Get_Transaction_Number_From_VT(ssis_conn, Config_FR.year)
            postgres_transaction_count = Connexions_FR.Get_Transaction_Number_From_PG(postgres_conn, Config_FR.year)

            print(f"VT: {ssis_transaction_count}, PostgreSQL: {postgres_transaction_count}")

            if ssis_transaction_count == postgres_transaction_count:
                print(Config_FR.OK_MESSAGE)
             #   return True
            else:
                print(Config_FR.KO_MESSAGE)
                # Comparaison par mois
                for month in range(1, 13):
                    print(f"Comparaison pour {Config_FR.year}-{month:02d}...")
                    ssis_month_count = Connexions_FR.Get_Transaction_Number_From_VT(ssis_conn, Config_FR.year, month)
                    postgres_month_count = Connexions_FR.Get_Transaction_Number_From_PG(postgres_conn, Config_FR.year, month)

                    if ssis_month_count != postgres_month_count:
                        print(f"Différence trouvée en {Config_FR.year}-{month:02d}")
                        # Comparaison par jour
                                #Récupère le dernier jour du mois
                        days_in_month = (datetime(Config_FR.year, month, 28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
                        for day in range(1, days_in_month.day + 1):
                            print(f"Comparaison pour {Config_FR.year}-{month:02d}-{day:02d}...")
                            ssis_day_count = Connexions_FR.Get_Transaction_Number_From_VT(ssis_conn, Config_FR.year, month, day)
                            postgres_day_count = Connexions_FR.Get_Transaction_Number_From_PG(postgres_conn, Config_FR.year, month, day)

                            if ssis_day_count != postgres_day_count:
                                print(f"Différence trouvée le {Config_FR.year}-{month:02d}-{day:02d}")
              #                  break
                #        break
               # return False
            Config_FR.year=Config_FR.year+1

        except Exception as e:
            # Afficher le nom de la fonction où l'erreur s'est produite en utilisant traceback
            exc_type, exc_value, exc_tb = sys.exc_info()  # Récupère les détails de l'exception
            function_name = traceback.extract_tb(exc_tb)[-1].name  # Extraire le nom de la fonction à partir de la pile de traceback
            print(f"Erreur critique dans la fonction {function_name}: {e}")  # Affiche l'erreur avec le nom de la fonction

            sys.exit(1)  # Arrêter le script avec le code de sortie 1

    ssis_conn.close()
    postgres_conn.close()

def main():
    # Lecture de l'année en paramètre ou par défaut année actuelle - 1
    year = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().year - 1

    current_year = datetime.now().year
    for y in range(year, current_year + 1):
        if not compare_transactions():
            break


if __name__ == "__main__":
    main()



