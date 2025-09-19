from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/FormularioCalculoCompras', methods=['GET', 'POST'])
def formulariocalculocompras():
    if request.method == 'POST':
        nombre = request.form['txtNombre']
        edad = int(request.form['Edad'])
        cant_tarros = int(request.form['cant_tarros_pintura'])
        valor_tarro = 9000
        precio_total = valor_tarro * cant_tarros

        if edad >= 18 and edad <= 30:
            descuento = float(precio_total * 0.15)
            precio_final = precio_total - descuento
        elif edad > 30:
            descuento = float(precio_total * 0.25)
            precio_final = precio_total - descuento
        else:
            descuento = 0
            precio_final = precio_total

        return render_template('FormularioCalculoCompras.html', nombre=nombre, edad=edad, cant_tarros=cant_tarros, precio_total=precio_total, descuento=descuento, precio_final=precio_final)
    return render_template('FormularioCalculoCompras.html')

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/FormularioInicioSesion', methods=['GET', 'POST'])
def formulariologin():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if usuario in usuarios and usuarios[usuario] == password:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('FormularioInicioSesion.html', usuario=usuario, password=password, mensaje=mensaje)
    return render_template('FormularioInicioSesion.html')
if __name__ == '__main__':
    app.run(debug=True)