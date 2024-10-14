import os
from dotenv import load_dotenv

load_dotenv()

Consulta = os.getenv("Query")
credenciales = os.getenv("credenciales")