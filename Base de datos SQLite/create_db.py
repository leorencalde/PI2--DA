import pandas as pd
import sqlite3

def create_database(file_path):
    # Cargar los datos desde el archivo Excel
    hechos_df = pd.read_excel(file_path, sheet_name='HECHOS')
    victimas_df = pd.read_excel(file_path, sheet_name='VICTIMAS')

    # Crear la conexión a la base de datos SQLite
    conn = sqlite3.connect('siniestros_viales.db')
    cursor = conn.cursor()

    # Crear la tabla 'hechos'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hechos (
        ID TEXT PRIMARY KEY,
        N_VICTIMAS INTEGER,
        FECHA TEXT,
        AAAA INTEGER,
        MM INTEGER,
        DD INTEGER,
        HORA TEXT,
        HH INTEGER,
        LUGAR_DEL_HECHO TEXT,
        TIPO_DE_CALLE TEXT,
        NOMBRE_DE_CALLE TEXT,
        ALTURA REAL,
        CRUCE TEXT,
        DIRECCION_NORMALIZADA TEXT,
        COMUNA INTEGER,
        XY_CABA TEXT,
        POS_X REAL,
        POS_Y REAL,
        PARTICIPANTES TEXT,
        VICTIMA TEXT,
        ACUSADO TEXT
    )
    ''')

    # Crear la tabla 'victimas'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS victimas (
        ID_hecho TEXT,
        FECHA TEXT,
        AAA INTEGER,
        MM INTEGER,
        DD INTEGER,
        ROL TEXT,
        VICTIMA TEXT,
        SEXO TEXT,
        EDAD INTEGER,
        FECHA_FALLECIMIENTO TEXT,
        FOREIGN KEY (ID_hecho) REFERENCES hechos (ID)
    )
    ''')

    # Ingestar los datos en la tabla 'hechos'
    hechos_df.to_sql('hechos', conn, if_exists='replace', index=False)

    # Ingestar los datos en la tabla 'victimas'
    victimas_df.to_sql('victimas', conn, if_exists='replace', index=False)
    
    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    print("Base de datos creada y datos ingresados exitosamente.")

if __name__ == "__main__":
    file_path = 'C:/Users/aleja/OneDrive/Escritorio/Data Science/2. Labs/PI2 -DA/Datasets/homicidios.xlsx'
    create_database(file_path)

