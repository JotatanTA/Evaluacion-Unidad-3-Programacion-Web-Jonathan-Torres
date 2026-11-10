from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# --- Ejercicio 1 ---

def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def estado(promedio, asistencia):
    if promedio >= 40 and asistencia >= 75:
        return "APROBADO"
    else:
        return "REPROBADO"


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = round(calcular_promedio(nota1, nota2, nota3), 1)
        resultado_estado = estado(promedio, asistencia)

        return render_template(
            'ejercicio1.html',
            nota1=nota1,
            nota2=nota2,
            nota3=nota3,
            asistencia=asistencia,
            promedio=promedio,
            estado=resultado_estado
        )
    return render_template('ejercicio1.html')


# --- Ejercicio 2 ---

def obtener_nombre_mas_largo(nombre1, nombre2, nombre3):
    nombres = [nombre1, nombre2, nombre3]


    mas_largo = nombres[0]

    for nombre in nombres:
        if len(nombre) > len(mas_largo):
            mas_largo = nombre

    caracteres = len(mas_largo)
    return mas_largo, caracteres


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        mas_largo, longitud = obtener_nombre_mas_largo(nombre1, nombre2, nombre3)

        return render_template(
            'ejercicio2.html',
            nombre1=nombre1,
            nombre2=nombre2,
            nombre3=nombre3,
            mas_largo=mas_largo,
            longitud=longitud
        )
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)