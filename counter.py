from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Ruta para incrementar y mostrar el contador de visitas
def incrementar_contador():
    if not os.path.exists("contador.txt"):
        with open("contador.txt", "w") as file:
            file.write("0")
    
    with open("contador.txt", "r") as file:
        visitas = int(file.read())
    
    visitas += 1
    
    with open("contador.txt", "w") as file:
        file.write(str(visitas))
    
    return visitas

@app.route('/')
def home():
    visitas = incrementar_contador()
    return render_template('index.html')

@app.route('/contador')
def contador():
    with open("contador.txt", "r") as file:
        visitas = file.read()
    return jsonify(visitas=int(visitas))

if __name__ == "__main__":
    app.run(debug=True)
