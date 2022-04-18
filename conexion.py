import pymysql

try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='veterinaria')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
