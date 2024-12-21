from flask import Flask, url_for, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
import os
from encodings import utf_8
from urllib import parse



app = Flask(__name__)
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'root'
app.config["MYSQL_DB"] = 'app_2'
app.config["MYSQL_CURSORCLASS"] = 'DictCursor'
app.config["MYSQL_CHARSET"] = 'utf8mb4'

db = MySQL(app)


def init_db():
    try:
        with open(os.path.join(os.getcwd(), 'src', 'db.sql'), 'r', encoding='utf-8') as file:
            query = file.read()
            db.connection.autocommit(True)
            db.connection.query(query)
    except Exception as e:
        print(f"No se pudo inicializar la base de datos | {e}")

with app.app_context():
    try:
        db.connection.query('SELECT * FROM asignatura')
    except:
        init_db()

@app.get('/')
def home():
    cursor = db.connection.cursor()
    cursor.execute("SELECT c.id as id, a.nombre as asignatura, nota, grado FROM calificacion c JOIN asignatura a ON c.id_asignatura = a.id JOIN semestre s ON a.id_semestre = s.id")
    calificaciones = list(cursor.fetchall())
    calificaciones.sort(key=lambda x: x["grado"])
    print(calificaciones)
    return render_template('index.html', calificaciones=calificaciones)

@app.get('/api/asignaturas')
def obtener_asignaturas():
    semestre = request.args.get('semestre')
    cursor = db.connection.cursor()
    if semestre:
        cursor.execute("SELECT * FROM asignatura WHERE id_semestre = %s", (semestre,))
    else:
        cursor.execute("SELECT * FROM asignatura")
        
        
    
    asignaturas = cursor.fetchall()
    return jsonify(asignaturas)

@app.get('/api/nota')
def obtener_nota():
    id_asignatura = request.args.get('asignatura')
    cursor = db.connection.cursor()
    nota = None
    if id_asignatura:
        cursor.execute("SELECT * FROM calificacion WHERE id_asignatura = %s", (id_asignatura,))
        res_query = cursor.fetchall()
        if len(res_query):
            nota = res_query[0].get('nota')
    
    return jsonify(nota=nota)
        

@app.route('/api/calificacion', methods=['GET', 'POST', 'PUT', 'DELETE'])
def crud_calificaciones():
    cursor = db.connection.cursor()
    if request.method == "POST":
        id_asignatura = request.json.get('asignatura')
        nota = request.json.get('nota')
        cursor.execute('INSERT INTO calificacion (id_asignatura, nota) VALUES (%s, %s)', (id_asignatura, nota))
        db.connection.commit()
    elif request.method == "PUT":
        id_asignatura = request.json.get('asignatura')
        nota = request.json.get('nota')
        cursor.execute('UPDATE calificacion SET nota = %s WHERE id_asignatura = %s', (nota, id_asignatura))
        db.connection.commit()
    elif request.method == "DELETE":
        id_calificacion = request.json.get('id_calificacion')
        cursor.execute('DELETE FROM calificacion WHERE id = %s', (id_calificacion,))
        db.connection.commit()
    return jsonify(message="Success")



if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)