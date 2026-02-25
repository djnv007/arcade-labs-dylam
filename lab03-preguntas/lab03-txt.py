def extraer_pregunta(pregunta: str) -> dict:
    separador=pregunta.split("|")
    diccionario={}
    diccionario["pregunta"]=separador[0]
    diccionario["correcta"]=separador[1]
    diccionario["opciones"]=separador[1:]
    return diccionario
#def juego(lista_preguntas):
    

with open ("preguntas.txt" , encoding="utf-8") as texto:
     pregunta=texto.readlines()
     lista_preguntas=[]
     for i in pregunta:
        lista_preguntas.append(extraer_pregunta(i))
#juego(lista_preguntas)
print(lista_preguntas)