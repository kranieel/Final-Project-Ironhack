
def alexis():
    return 3

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def rellenar_tabla(risk,fullrisk):
    '''
    Función que rellena la tabla 1 de asteroides con la tabla 2.(Tiene que ser la tabla de la Nasa.)'''
    for i in range(len(fullrisk)):
        valores={'No.':fullrisk['No.'][i],'Object designation':fullrisk['Object designation'][i],
        'Diameter\nin m':fullrisk['Diameter in m'][i],'Impact date/time in UTC':fullrisk['Impact date/time in UTC'][i],
        'IP max':fullrisk['IP max'][i],'PS max':fullrisk['PS max'][i],'TS':0,'Years':fullrisk['Impact date/time in UTC'][i][:4],
        'IP cum':0,'PS cum':0,'Vel. in km/s':fullrisk['Vel. in km/s'][i]}
        risk = risk.append(valores, ignore_index=True)
    return risk

def clean_name(url):
    '''
    Ésta función recoge una url y substrae una lista con todos los nombres de los meteoritos que han caído los últimos años
    '''
    html = requests.get(url).content
    html[0:10000]
    soup = BeautifulSoup(html, "lxml")
    text = soup.find_all('tr')
    names_sucio=soup.find_all('div',{'align':'center'})[10::10]
    name = [d.text for d in names_sucio]
    
    return name

def clean_country(url):
    '''
    Ésta función recoge una url y substrae una lista con todos los países donde han caído meteoritos
    '''
    html = requests.get(url).content
    html[0:10000]
    soup = BeautifulSoup(html, "lxml")
    text = soup.find_all('tr')
    country_sucio=soup.find_all('div',{'align':'center'})[11::10]
    country = [d.text for d in country_sucio]
    
    return country

def is_australia(list):
    ''' 
    Esta función comprueba una lista y sustituye los estados de Australia por el nombre del país.
    '''
    australia=['South Australia','Northern Territory','Queensland','Western Australia','South Australia','New South Wales','Victoria','Tasmania']
    for i in range(len(list)):
        if list[i] in australia:
            list[i]='Australia'
    return list

def add_code(key: pd.Series, value: pd.Series, repl: pd.DataFrame, column: str ):
    '''
    Esta función produce un diccionario temporal con las keys y los values de series escogidas y sustituye, por esos values, los datos
    en un DataFrame que localiza a través de la key del diccionario :)'''
    
    dictio = dict(zip(key, value))
    for i in dictio.keys():
        repl.replace({column : i}, dictio[i], inplace=True)

def na_country(list):
    '''
    Ésta función recoge una lista con el estado y el país y te devuelve una lista con solo el país.
    '''
    list_country=[]
    for i in list:
        a=i.split(",")
        list_country.append(a[1][1:]) #el [1:] Es para quitar el espacio en blanco antes del país
    return list_country

def crear_df(names,columns):
    if len(names)==len(columns):
        df=pd.DataFrame()
        for i in range(len(names)):
            df[names[i]]=columns[i]
        return df
    else:
        return "Error"
    
def del_columns(df:pd.DataFrame,list):    
    '''
    Esta función limpiara las columnas que le pases....Pasen una LISTA. Aunque sea de 1.
    '''
    for i in list:
        df.drop(columns=i,axis=1,inplace=True)
    return df

def rellenar_tabla(risk,fullrisk):
    '''
    Función que rellena la tabla 1 de asteroides con la tabla 2.(Tiene que ser la tabla de la Nasa.)'''
    for i in range(len(fullrisk)):
        valores={'No.':fullrisk['No.'][i],'Object designation':fullrisk['Object designation'][i],
        'Diameter\nin m':fullrisk['Diameter in m'][i],'Impact date/time in UTC':fullrisk['Impact date/time in UTC'][i],
        'IP max':fullrisk['IP max'][i],'PS max':fullrisk['PS max'][i],'TS':0,'Years':fullrisk['Impact date/time in UTC'][i][:4],
        'IP cum':0,'PS cum':0,'Vel. in km/s':fullrisk['Vel. in km/s'][i]}
        risk = risk.append(valores, ignore_index=True)
    return risk

def cost(lista):
    falcon=67000000
    fuel_falcon9=200000
    lista_nueva=[]
    for i in lista:
        # distancia * 0.01% del combustible usado en el despegue + el combustible del despegue
        lista_nueva.append(i*200+fuel_falcon9)
    return lista_nueva

def sigmoid(x, Beta_1, Beta_2):
     y = 1 / (1 + np.exp(-Beta_1*(x-Beta_2)))
     return y  
        
        
def remp_años(lista):
    sucia=[]
    for i in lista:
        sucia.append(i)
        
    final=[]
    for a in sucia:
        final.append(i[:4])
    return final
        

def tiempo_viaje(distancias,vel):
    '''Calcula una estimación del tiempo que tardaría en recorrer x distancia el Falcon 9 a 30.400 km/h'''
    total_tiempo=[]
    for i in distancias:
        res=i/vel
        res=res/24
        if res//365 == 0:
            total=f'{res//365:.0f} años {res%365:.0f} días {res%24:.0f} horas'
        else:
            total=f'{res//365:.0f} años {res%365:.0f} días {res%24:.0f} horas'
        total_tiempo.append(total)
        
    return total_tiempo
        

def save_csv(nombre,path):
    ''' Guarda en csv'''
    nombre.to_csv(path, index=False)
    pass