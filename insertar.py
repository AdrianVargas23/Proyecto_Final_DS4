
def insertar(user:str, contra:str, name:str, apellido:str, telefono:str, pregunta:str, respuesta:str):
	import pymysql
	try:
		conexion = pymysql.connect(host='localhost',
								   user='root',
								   password='',
								   db='veterinaria')
		try:
			with conexion.cursor() as cursor:
				consulta = "INSERT INTO (username, contrasenia, nombre, apellido, telefono, pregunta, respuesta) VALUES (%s, %s, %s, %s, $s, %s, %s);"
				# Podemos llamar muchas veces a .execute con datos distintos
				cursor.execute(consulta, (user, contra, name, apellido, telefono, pregunta, respuesta))
			conexion.commit()
		finally:
			conexion.close()
	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)