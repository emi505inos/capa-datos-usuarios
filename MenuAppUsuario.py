import CursorDelPool as cursor
from logger_base import log
from UsuarioDao import UsuarioDAO
import psycopg2
from usuario import Usuario
''' conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
opcion = None
while opcion != 5:
    try:
        print(Opciones:
    1. Listar usuarios.
    2. Agregar usuarios.
    3. Modificar usuarios.
    4. Eliminar usuarios.
    5. Salir)
        opcion= int(input('Escribe tu opcion (1-5):'))
        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                print(usuario)
        elif  opcion == 2:
            id_usuario = (input('Proporcione el id:'))
            nombre = str(input('Proporcione el nombre:'))
            password = str(input('Proporcione contraseña:'))
            usuarios = Usuario(nombre, password)
            usuarios_insertados = UsuarioDAO.insertar(usuarios)
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Saliendo....')

 '''
opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar ususarios.')
    print('2. Agregar ususarios.')
    print('3. Modificar ususarios.')
    print('4. Eliminar ususarios.')
    print('5. Salir.')
    opcion = int(input('Escribe tu opcion (1-5):'))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el username:')
        password_var = input('Escribe el password:')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_username_var = int(input('Escribe el id:'))
        username_var2 = int(input('Escribe el username:'))
        password_var2 = int(input('Escribe el password:'))
        usuario_mod = Usuario(id_username_var,username_var2, password_var2)
        usuarios_modi = UsuarioDAO.actualizar(usuario_mod)
        log.info(f'Usuarios modificados: {usuarios_modi}')
    elif opcion == 4:
        id_username_var2 = int(input('Poporcione el id:'))
        usuario_el = Usuario(id_usuario=id_username_var2)
        usuario_elim = UsuarioDAO.eliminar(usuario_el)
        log.info(f'Usuario eliminado: {usuario_elim}')
else:
    log.info('Salimos de la aplicacion')