import pymysql


def consultar(usuario: str, contra: str) -> list:
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db='veterinaria')
        try:
            with conexion.cursor() as cursor:
                print("test")
                consulta = "SELECT username, nombre FROM usuarios WHERE username = %s AND contrasenia = %s;"
                cursor.execute(consulta, (usuario, contra))
                # Con fetchall traemos todas las filas
                lista_usuarios = cursor.fetchall()  # (usuario, nombre)
                print(lista_usuarios[0])
                lista_final = lista_usuarios[0]
                print(lista_final[0])
                print(lista_usuarios)
                print(lista_usuarios[0])
                user = lista_final[0]
                nombre = lista_final[1]
                usuario_correcto = True
                lista_final_final = [user,nombre,usuario_correcto]



        finally:
            conexion.close()
            return usuarios
            return nombre
            return usuario_correcto
            print("cerrando")

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
