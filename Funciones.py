import pymysql


def consultar(usuario:str, contra:str):
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
                lista_usuarios = cursor.fetchall() #(usuario, nombre)
                usuarios = lista_usuarios[0]
                nombre = lista_usuarios[1]

                usuario_correcto = True
                print(usuarios)

        finally:
            conexion.close()
            return usuarios
            return nombre
            return usuario_correcto
            print("cerrando")

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)