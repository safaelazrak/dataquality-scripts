#Functions_FR.py
import pyodbc
import sys
import psycopg2
import Config_FR


# Fonctions de connexion
def connect_to_ssis():
    ssis_conn_str = f'DRIVER={{SQL Server}};SERVER={Config_FR.URL_SERVER_VT};DATABASE={Config_FR.DATABASE_VT};UID={Config_FR.ssis_user};PWD={Config_FR.ssis_password}'
    return pyodbc.connect(ssis_conn_str)

def connect_to_postgres():
    return psycopg2.connect(
        host=Config_FR.URL_SERVER_POSTGRE,
        database=Config_FR.DATABASE_POSTGRE,
        user=Config_FR.postgres_user,
        password=Config_FR.postgres_password
    )

def NoArgument():
        if len(sys.argv) < 6:  # Vérifie qu'il y a bien 5 arguments en plus du nom du script
            print(Config_FR.INFO_MESSAGE_NO_PARAM)
            print("Nombre d'arguments insuffisant.")
            print(Config_FR.USAGE_MESSAGE)
            sys.exit(1)




def check_year_argument(year_arg):
    """
    Vérifie que le 1er argument est une année valide (4 chiffres, >= 2020).
    :param year_arg: Le premier argument fourni au script.
    """
    if not (year_arg.isdigit() and len(year_arg) == 4 and int(year_arg) >= 2020):
        print(Config_FR.ERROR_YEAR)
        print(Config_FR.USAGE_MESSAGE)
        sys.exit(1)



