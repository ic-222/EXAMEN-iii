# config.py

class Config:
    SECRET_KEY = 'clave_secreta_para_proteger_sesiones'
    DEBUG = True

    # Configuración de la base de datos MS Access
    DATABASE_CONNECTION_STRING = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=RUTA DE LA BASE DE DATOS;'

    ### EJEMPLO DE LA RUTA: DBQ=C:\USER\EXAMEN-iii-main\EXAMEN-iii-main\DB.accdb;'


    @staticmethod
    def init_app(app):
        pass
