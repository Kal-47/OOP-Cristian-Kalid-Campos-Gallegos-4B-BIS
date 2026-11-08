"""Diagnóstico: ejecuta `python check_db.py` desde la carpeta Lab_7."""
import mysql.connector
from mysql.connector import Error
from Controller.config import DB_config

print("Configuración usada:", {k: v for k, v in DB_config.items() if k != "password"})

try:
    con = mysql.connector.connect(**DB_config)
    print("1) Conexión OK")
except Error as e:
    print("1) FALLÓ la conexión ->", e)
    raise SystemExit(1)

cur = con.cursor(dictionary=True)
try:
    cur.execute("SELECT id_user, username, passw, usr_name FROM users")
    rows = cur.fetchall()
    print(f"2) Tabla 'users' OK, {len(rows)} fila(s):")
    for r in rows:
        print("   ", r)
    if not rows:
        print("   La tabla está vacía: falta el INSERT del usuario admin.")
except Error as e:
    print("2) FALLÓ la consulta ->", e)
con.close()
