import config, utils
import pandas as pd

credenciales = utils.Lectura_json(config.credenciales)

consulta = """
Select	LoginID,
		JobTitle
from HumanResources.Employee
"""

df = utils.conexion_base_de_datos(
    credenciales["SQLSERVER"]["Servidor"],
    credenciales["SQLSERVER"]["Usuario"],
    credenciales["SQLSERVER"]["Password"],
    credenciales["SQLSERVER"]["Database"],
    consulta
)

df.to_csv('Salida_Tabla_HumanResources.txt', sep='|', index=False)