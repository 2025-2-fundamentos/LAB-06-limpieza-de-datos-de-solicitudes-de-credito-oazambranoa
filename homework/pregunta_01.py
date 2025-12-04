"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import glob
import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    
    for column in df.select_dtypes(include = ["object"]).columns:
        df[column] = df[column].str.lower()
        df[column] = df[column].str.replace("_", " ")
        df[column] = df[column].str.replace("-", " ")
        df[column] = df[column].str.replace(",", "")
        df[column] = df[column].str.replace("$", "")
        df[column] = df[column].str.replace(".00", "")

    
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], 
        format = "%d/%m/%Y", 
        errors = "coerce").combine_first(
            pd.to_datetime(df["fecha_de_beneficio"], 
                           format = "%Y/%m/%d", 
                           errors = "coerce"
                           ))

    df = df.drop_duplicates()
    df = df.dropna()

    print(df.sexo.value_counts().tolist())

    if os.path.exists("files/output"):
        for file in glob.glob("files/output/*"):
            os.remove(file)
    else:
        os.makedirs("files/output")
    
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

pregunta_01()