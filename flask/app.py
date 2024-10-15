from flask import Flask, render_templates

# Crear la aplicación de Flask
app = Flask(__name__)


# Definir una ruta básica
@app.route("/")
def home():
    mensaje = "Bienvenido a mi aplicación con Flask"
    return render_templates("index.html", mensaje=mensaje)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)