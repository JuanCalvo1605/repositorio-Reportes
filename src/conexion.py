from flask import Flask, jsonify, request
import pyodbc
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app) 

# Configuración del servidor
server = '172.19.10.8'
database = 'base_reportes'
username = 'user_1'
password = 'Andes2015*'
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'


@app.route('/login', methods=['GET'])
def obtener_credeciales():
    try:
        
        #obtener credenciales
        correo = request.args.get('correo')
        password = request.args.get('contra')
        
        # Establecer la conexión
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre,apellido,contraseña,correo FROM t_usuarios where correo = ? and contraseña = ?",(correo,password))
        usuario = cursor.fetchone()
        
        if not usuario:
            return jsonify({'valido': False}), 401
        
        print(correo,password)
        
        
        
        #nombre, apellido, password = cursor.fetchone()
        conn.close()         
        
        # Si se encontró el usuario, devolver un booleano en True
        return jsonify({'valido': True})
    

    except Exception as e:
        return f'Error: {e}', 500
    
@app.route('/', methods=['GET'])
def obtener_nombres():
    try:
        # Establecer la conexión
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM t_reportes")
        
        # Obtener todas las filas de la consulta
        rows = cursor.fetchall()
        
        # Construir una lista de diccionarios con los resultados
        
        informes = []
        for row in rows:
            informe = {'nombre': row.nombre}
            informes.append(informe)
        
        conn.close()         
        
        # Retornar los datos como JSON
        return jsonify(informes)

    except Exception as e:
        return f'Error: {e}', 500
    
@app.route('/informe', methods=['GET'])
def obtener_reportes():
    try:
        # Establecer la conexión
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre FROM t_reportes")
        codigo_pwi, nombre = cursor.fetchone()
        conn.close()         
        # Retornar los datos como JSON
        return jsonify({'codigo_pwi': codigo_pwi, 'nombre': nombre})
    
    except Exception as e:
        return f'Error: {e}', 500

if __name__ == '__main__':
    serve(app, host='172.19.10.8', port=5000, threads=2)
