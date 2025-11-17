import mysql.connector #importar libreria MySql
#establcer la conexion a la base de datos
#user, password, host, database, port

conexion = mysql.connector.connect(user = "root", password = "", host = "localhost", database = "escolar", port = 3306)

print("Conexión exitosa a la base de datos", conexion)

#curssor
posicion = conexion.cursor()

#insrtar registros
posicion.execute("INSERT INTO alumnos (	matricula,nombre,carrera,semestre,grupo) VALUES (1, 'Juan Perez', 'Ingeniería', 5, 'A')")

conexion.commit() #guardar cambios

posicion.close() 
conexion.close() #cerrar conexion 
