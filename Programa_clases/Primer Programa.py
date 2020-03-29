import pymongo
import pprint


def funcion():
    print('hola mundo')


if __name__ == '__main__':
    funcion()
    print(pymongo.version)

    client = pymongo.MongoClient("mongodb+srv://admin:zxcv123456@prueba-lprhj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.bd_prueba
    coleccion = db.coleccion

    persona = {
        "name": "Maria",
        "edad": 39,
        "trabajo": "Electronico",
        "opciones": ["casa1", "garaje1", "garaje2"],
        "vistas": 12
    }

    coleccion.insert_one(persona)
    # coleccion_id = coleccion.insert_one(persona).inserted_id
    # print(coleccion_id)

    # print(coleccion.find_one())
    #pprint.pprint(coleccion.find_one())
    pprint.pprint(coleccion.find_one({"vistas": 12}))

    for documento in coleccion.find():
        pprint.pprint(documento)

    numero = coleccion.count_documents({})
    print("Numero de documentos " + str(numero))

    coleccion.count_documents({"vistas": 12})
    print("Numero de documentos " + str(numero))

