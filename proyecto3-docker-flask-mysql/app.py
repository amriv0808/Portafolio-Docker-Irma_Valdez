import time
import mysql.connector
from flask import Flask, render_template

# ============================================================
# INICIALIZACIÓN DE FLASK
# ============================================================
app = Flask(__name__)

print("Valor de __name__:", __name__)
print("Ruta raíz detectada por Flask:", app.root_path)
print("Carpeta de templates:", app.template_folder)
print("Carpeta static:", app.static_folder)


# ============================================================
# CONEXIÓN CON MYSQL (CON REINTENTOS)
# ============================================================
def get_db_connection():
    # Intenta conectarse hasta 10 veces dando tiempo a MySQL de iniciar
    for i in range(10):
        try:
            connection = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="proyecto",
                connection_timeout=5
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Esperando a MySQL... intento {i+1}/10. Error: {err}")
            time.sleep(3)
    raise Exception("No se pudo conectar a MySQL después de varios intentos.")


# ============================================================
# RUTA PRINCIPAL
# ============================================================
@app.route("/ping")
def ping():
    return "¡El contenedor responde correctamente!"

@app.route("/")

def usuarios():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT nombre, edad FROM usuarios")
    resultados = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "usuarios.html",
        usuarios=resultados
    )


# ============================================================
# ARRANQUE DE LA APLICACIÓN
# ============================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)