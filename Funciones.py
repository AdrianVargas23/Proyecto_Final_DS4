import pymysql
from passlib.handlers.sha2_crypt import sha256_crypt


def consultar(usuario: str, contra: str) -> list:
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db='veterinaria')
        try:
            with conexion.cursor() as cursor:
                print("test")
                consulta = "SELECT username, nombre, contrasenia FROM usuarios WHERE username = %s;"
                cursor.execute(consulta, (usuario, contra))
                # Con fetchall traemos todas las filas
                lista_usuarios = cursor.fetchall()  # (usuario, nombre)
                lista_final = lista_usuarios[0]
                user = lista_final[0]
                nombre = lista_final[1]
                contrasenia = lista_final[2]
                contrasenia_verificada = sha256_crypt.verify(contra, contrasenia)
                lista_final_final = [user,nombre,contrasenia_verificada]

        finally:
            conexion.close()
            print("cerrando")
            return lista_final_final


    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
