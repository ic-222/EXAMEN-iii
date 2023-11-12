# app.py

import pyodbc
from flask import Flask, render_template, request, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Establecer la conexión a la base de datos utilizando la configuración
conn = pyodbc.connect(app.config['DATABASE_CONNECTION_STRING'])
cursor = conn.cursor()

conn.commit()

def obtener_gastos():
    cursor.execute('SELECT * FROM Gastos')
    return cursor.fetchall()

def calcular_total_gastado():
    cursor.execute("SELECT SUM(Monto) FROM Gastos")
    total = cursor.fetchone()[0]
    return total if total is not None else 0

def insertar_gasto(nombre, monto, descripcion, categoria):
    cursor.execute("INSERT INTO Gastos (Nombre, Monto, Descripcion, Categoria) VALUES (?, ?, ?, ?)",
                   (nombre, monto, descripcion, categoria))
    conn.commit()

def actualizar_gasto(id, nombre, monto, descripcion, categoria):
    cursor.execute("UPDATE Gastos SET Nombre=?, Monto=?, Descripcion=?, Categoria=? WHERE ID=?",
                   (nombre, monto, descripcion, categoria, id))
    conn.commit()

def eliminar_gasto(id):
    cursor.execute("DELETE FROM Gastos WHERE ID=?", (id,))
    conn.commit()

@app.route('/buscar_gastos', methods=['GET'])
def buscar_gastos():
    palabra_clave = request.args.get('busqueda', '')

    if palabra_clave:
        # Realiza la búsqueda en la base de datos según la palabra clave
        cursor.execute(f"SELECT * FROM Gastos WHERE Nombre LIKE ? OR Descripcion LIKE ? OR Categoria LIKE ?",
                       ('%' + palabra_clave + '%', '%' + palabra_clave + '%', '%' + palabra_clave + '%'))
        gastos = cursor.fetchall()
    else:
        # Si no hay palabra clave, muestra todos los gastos
        cursor.execute("SELECT * FROM Gastos")
        gastos = cursor.fetchall()

    total_gastado = calcular_total_gastado()

    return render_template('mostrar_gastos.html', gastos=gastos, total_gastado=total_gastado)




@app.route('/filtrar_por_categoria', methods=['POST'])
def filtrar_por_categoria():
    categoria_seleccionada = request.form.get('categoria')

    if categoria_seleccionada:
        cursor.execute("SELECT * FROM Gastos WHERE Categoria=?", (categoria_seleccionada,))
        gastos = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM Gastos")
        gastos = cursor.fetchall()

    total_gastado = calcular_total_gastado()

    return render_template('mostrar_gastos.html', gastos=gastos, total_gastado=total_gastado)


@app.route('/ordenar_gastos/<criterio>', methods=['GET'])
def ordenar_gastos(criterio):
    if criterio == 'nombre' or criterio == 'monto':
        cursor.execute(f"SELECT * FROM Gastos ORDER BY {criterio}")
        gastos = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM Gastos")
        gastos = cursor.fetchall()

    total_gastado = calcular_total_gastado()

    return render_template('mostrar_gastos.html', gastos=gastos, total_gastado=total_gastado)



@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']

        insertar_gasto(nombre, monto, descripcion, categoria)

    # Mostrar la lista de gastos después de registrar uno nuevo
    gastos = obtener_gastos()
    total_gastado = calcular_total_gastado()

    return render_template('mostrar_gastos.html', gastos=gastos, total_gastado=total_gastado)


# Ruta para mostrar la lista de gastos
@app.route('/mostrar_gastos')
def mostrar_gastos():
    gastos = obtener_gastos()
    total_gastado = calcular_total_gastado()
    return render_template('mostrar_gastos.html', gastos=gastos, total_gastado=total_gastado)

# Ruta para editar un gasto
@app.route('/editar_gasto/<int:id>', methods=['GET', 'POST'])
def editar_gasto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']

        actualizar_gasto(id, nombre, monto, descripcion, categoria)
        return redirect(url_for('mostrar_gastos'))

    # Obtener el gasto a editar
    cursor.execute("SELECT * FROM Gastos WHERE ID=?", (id,))
    gasto = cursor.fetchone()

    return render_template('editar_gasto.html', gasto=gasto)

# Ruta para eliminar un gasto
@app.route('/eliminar_gasto/<int:id>')
def eliminar_gasto(id):
    try:
        eliminar_gasto_db(id)
    except Exception as e:
        # Maneja la excepción aquí según tu lógica
        print(f"Error al eliminar gasto: {e}")

    return redirect(url_for('mostrar_gastos'))

# Nueva función para eliminar gasto en la base de datos sin redirección
def eliminar_gasto_db(id):
    cursor.execute("DELETE FROM Gastos WHERE ID=?", (id,))
    conn.commit()
if __name__ == '__main__':
    app.run(debug=True)
