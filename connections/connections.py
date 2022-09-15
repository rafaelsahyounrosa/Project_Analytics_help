import cx_Oracle
import pandas as pd

dsn_tns = cx_Oracle.makedsn('ip', port, sid='SID') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user='ESTUDO_ANALYTICS', password='senhaqualquer', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

def monta_df(query):
    c = conn.cursor()
    #query = 'SELECT * FROM VWWEB_TOTE'
    df = pd.read_sql(query, conn)
    conn.close()
    return df
