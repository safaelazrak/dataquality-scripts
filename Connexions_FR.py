#Connexions_FR.py

from Config_FR import HEAD_OFFICE_ID, transaction_categories_sql, excluded_cinemas_sql

def Get_Transaction_Number_From_VT(ssis_conn, year, month=None, day=None):
    ssis_query = f"""
    SELECT COUNT(DISTINCT [Transaction_Header_Id]) AS transaction_count
    FROM [analysis_en].[Transaction_Concession]
    WHERE Revenue_Date >= '{year}-01-01' AND Revenue_Date < '{year+1}-01-01'
        AND Revenue_Date < DATEADD(day, -2, GETDATE())
        
    """

    if month:
        ssis_query += f" AND MONTH(Revenue_Date) = {month}"
    if day:
        ssis_query += f" AND DAY(Revenue_Date) = {day}"

    with ssis_conn.cursor() as cursor:
        cursor.execute(ssis_query)
        return cursor.fetchone()[0]


def Get_Transaction_Number_From_PG(postgres_conn, year, month=None, day=None):
    postgres_query = f"""
    SELECT COUNT(DISTINCT TR."Transaction_Header_Id") AS transaction_count
    FROM public."Ilot_TRANSACTIONS_RETAIL" AS TR
    WHERE TR."Revenue_Date" >= '{year}-01-01' AND TR."Revenue_Date" < '{year+1}-01-01'
    AND TR."Revenue_Date" < NOW() - INTERVAL '2 days'
    """
    if month:
        postgres_query += f"""
            AND TR."Revenue_Date" >= date_trunc('month', DATE '{year}-{month}-01')
            AND TR."Revenue_Date" < date_trunc('month', DATE '{year}-{month}-01') + INTERVAL '1 month'
        """

    if day:
        postgres_query += f"""
            AND TR."Revenue_Date" >= DATE '{year}-{month:02d}-{day:02d}'
            AND TR."Revenue_Date" < DATE '{year}-{month:02d}-{day:02d}' + INTERVAL '1 day'
        """

        #postgres_query += f" AND EXTRACT(DAY FROM TR.\"Revenue_Date\") = {day}"

    with postgres_conn.cursor() as cursor:
        cursor.execute(postgres_query)
        return cursor.fetchone()[0]




