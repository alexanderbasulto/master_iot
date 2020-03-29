import json
import urllib.request
import pymongo

def descarga_datos():         #Descargar datos de URL y crear variable diccionario
    url = 'https://api.bsmsa.eu/ext/api/bsm/gbfs/v2/en/station_information'
    contents = urllib.request.urlopen(url).read()
    datos_0 = json.loads(contents.decode('utf-8'))
    return datos_0

def crear_archivo(datos_file):      #Crear y escribir archivo
    file = open('datos.json', 'w')
    file.write(json.dumps(datos_file, indent=4))
    file.close()
    return()

def mongodb_connect():
    client = pymongo.MongoClient("mongodb+srv://admin:zxcv123456@prueba-lprhj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.bd_actividad
    url_dbmongo = db.actividad_1
    return url_dbmongo

def mongodb_send(data_to_send,dbmongo):
    datos_data = data_to_send.get('data')
    datos_stations = datos_data.get('stations')
    dbmongo.insert(datos_stations)
    return()

def get_attr(dbmongo):
    print()
    print("La estaciones con una capacidad de 30 son:")
    for x in dbmongo.find({"capacity": 30}):  # Consulta a MondoGB el atributo de capacidad de la estacion y filtra solo las estaciones con esa capacidad
        print(x)
    return()

def get_top_3(dbmongo):
    print()
    print("Las 3 estaciones con mayor capacidad, de mayor a menor son:")
    for x in dbmongo.find({"capacity": {"$gt": 1}}).sort("capacity", -1).limit(3):
        print(x)
    return()

def get_media(dbmongo):
    print()
    print("Se va calcular la media de la Altitud de todas las estaciones:")
    for x in dbmongo.aggregate([{"$group" : {"_id": 1, "promedio": {"$avg":"$altitude"}, "Total de Estaciones": {"$sum": 1}}}]):
        print(x)
    return()

if __name__ == "__main__":                          #Programa principal
    datos_json = descarga_datos()                   #Llama a la funcion descarga_datos y devuelve el valor a la variable
    crear_archivo(datos_json)                       #Llama a la funcion crear_archivo, para crear el documento .json
    print("Archivo creado....")                     #Imprime en consola que el documento fue creado
    url_mongo = mongodb_connect()                   #Llama a la funcion mongodb_connect para cargar la dirrecion de Mongo en la variable
    mongodb_send(data_to_send=datos_json, dbmongo=url_mongo)    #Llama a la funcion mongodb_send para enviar laos datos
    print("Datos enviados a MongoDB....")           #Imprime en consola que los datos fueron enviados
    get_attr(url_mongo)                             #Consulta sobre un atributo numerico en todos los datos
    get_top_3(url_mongo)                            #Devuelve el top 3 de las estaciones segun el atributo escogido
    get_media(url_mongo)                            #Calcula la media de un atributo de todos los datos
    print("Programa terminado.")
