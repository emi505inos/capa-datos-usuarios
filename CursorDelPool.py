from logger_base import log
from conexion import Conexion
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta método __exit__')
        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {exc_val}, {exc_type}, {exc_tb}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
