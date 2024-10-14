import pyodbc
import pandas as pd
import json

def lectura_planos (ruta_archivo:str):
    try:
        with open(ruta_archivo) as consulta:
            query = consulta.read()
        return query
    except FileNotFoundError as e:
        return f"Error: El archivo no fue encontrado. {e}"
    except IOError as e:
        return f"Error: Problema al leer el archivo. {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

def Lectura_json (ruta_archivo:str):
    try:
        with open(ruta_archivo) as archivo_json:
            archivo = json.load(archivo_json)
        return archivo
    except FileNotFoundError as e:
        return f"Error: El archivo no fue encontrado. {e}"
    except IOError as e:
        return f"Error: Problema al leer el archivo. {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    
def conexion_base_de_datos(servidor:str,usuario:str,contraseña:str, basededatos:str, Query:str):
    try:
        conexion = pyodbc.connect(f"""DRIVER={{ODBC Driver 17 for SQL Server}};
                          SERVER={servidor};
                          DATABASE={basededatos};
                          UID={usuario};
                          PWD={contraseña}""")
        df = pd.read_sql_query(Query,conexion)
        conexion.close
        return df
    except pyodbc.Error as e:
        conexion.close
        print(f"Error {e}")
        return None
    finally:
        conexion.close