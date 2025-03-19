###################### Función para cargar un archivo como un dataframe################################

def Funcion_1(archivo):  #La entrada es un archivo
    import pandas as pd
    import os
    #Si se desea agregar un input se coloca:
#   archivo=input("Por favor, ingresa el nombre del archivo: ")
    extension = os.path.splitext(archivo)[1].lower()
# Cargar el archivo según su extensión
    if extension == '.csv':
        df= pd.read_csv(archivo)
        return (df)
    elif extension == '.html':
        df= pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"“Hola, acabas de ingresar un documento que desconozco, con extensión: {extension}")


#######################Función_primas ########################################
def Funcion_2(df):
    import pandas as pd
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Identificar índices primos
    columnas_primas = [col for i, col in enumerate(df.columns) if es_primo(i)]

    # Sustituir valores nulos
    for col in df.columns:
        if col in columnas_primas and pd.api.types.is_numeric_dtype(df[col]):
            # Para columnas con índice primo y tipo numérico
            df[col].fillna(1111111, inplace=True)
        elif pd.api.types.is_numeric_dtype(df[col]):
            # Para columnas numéricas que no tienen índice primo
            df[col].fillna(1000001, inplace=True)
        else:
            # Para columnas no numéricas
            df[col].fillna("Valor Nulo", inplace=True)
    
    return df

######################Función_Contar_Nulos############################################
def Funcion_3(df):
    # Valores nulos por columna
    valores_nulos_cols = df.isnull().sum()
    # Valores nulos en todo el DataFrame
    valores_nulos_df = df.isnull().sum().sum()
    
    print("Valores nulos por columna:")
    print(valores_nulos_cols)
    print("Valores nulos en el DataFrame:", valores_nulos_df)
    
    # Retornar resultados y el DataFrame original
    return df

#######################Función_Atipicos########################################
def Funcion_4(df):
    import pandas as pd
    # Separar columnas cuantitativas del DataFrame
    cuantitativas = df.select_dtypes(include=['float64', 'int64', 'float', 'int'])

    # Separar columnas cualitativas del DataFrame
    cualitativas = df.select_dtypes(include=['object', 'datetime', 'category'])
    
    #Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
    y=cuantitativas

    percentile25=y.quantile(0.25) #Q1
    percentile75=y.quantile(0.75) #Q3
    iqr= percentile75 - percentile25

    Limite_Superior_iqr= percentile75 + 1.5*iqr
    Limite_Inferior_iqr= percentile25 - 1.5*iqr

    #Obtenemos datos limpios del Dataframe
    data_iqr= cuantitativas[(y<=Limite_Superior_iqr)&(y>=Limite_Inferior_iqr)]
    data_iqr
    
    #Reemplazamos valores atípicos (nulos) del dataframe con "mean"
    #Realizamos una copia del dataframe
    data_iqr=data_iqr.fillna('Valor Atípico')
    data_iqr
    
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo

    Datos_limpios= pd.concat([cualitativas, data_iqr], axis=1)
    Datos_limpios
    
    return(Datos_limpios)