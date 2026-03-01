import random
def extraer_pregunta(pregunta: str) -> dict:
    separador=pregunta.split("|")
    diccionario={}
    diccionario["pregunta"]=separador[0]
    diccionario["correcta"]=separador[1]
    diccionario["opciones"]=separador[1:]
    random.shuffle(diccionario["opciones"])
    return diccionario
def letras_opciones(longitud: int) -> list:
    letras=[]
    for i in range(longitud):
        letras.append(chr(97+i))
    return letras
def validar_respuestas(opciones):
    valido=False
    while not valido:
        try:
            respuesta=input("Introduce tu respuesta: ")
            if respuesta not in opciones:raise
            else: return opciones.index(respuesta)
        except:
            print("Respuesta no válida, intenta de nuevo")
        
def juego(lista_preguntas: list) -> None:
    puntos=0
    for pregunta in range(len(lista_preguntas)):
        print(f"{lista_preguntas[pregunta]["pregunta"]}")
        opciones= lista_preguntas[pregunta]["opciones"]
        letras=letras_opciones(len(opciones))
        for opcion in (range(len(opciones))):
            print(f"{letras[opcion]}) {opciones[opcion]}")
        respuesta=validar_respuestas(letras)
        if lista_preguntas[pregunta]["opciones"][respuesta]==lista_preguntas[pregunta]["correcta"]:
            print("¡Respuesta correcta!")
            puntos+=1
        else:
            print("¡Respuesta incorrecta!")
    print(f"Puntos obtenidos: {puntos}")
        
with open ("preguntas.txt" , encoding="utf-8") as texto:
     pregunta=texto.readlines()
     lista_preguntas=[]
     for i in pregunta:
        lista_preguntas.append(extraer_pregunta(i.strip()))
juego(lista_preguntas) 

    