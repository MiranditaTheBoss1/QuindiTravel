import random
import nltk # py -m pip install nltk
from sklearn.feature_extraction.text import CountVectorizer #py -m pip install -U scikit.learn.
from sklearn.naive_bayes import MultinomialNB

# Respuestas del chatbot
saludos = ["Hola", "Hola", "¿cómo estás?", "¡Bienvenido!", "buenas", "hola"]
lugares_turisticos = ["Parque del café", "El Museo quimbaya del oro", "El mariposario", "Panaca", "Parque de los arrieros",
                      "Recuca", "mano de Acaime, en cocora", "mirador de filandia"]
actividades = ["Montar a caballo", "Parapentes", "Caminata por el parque de la vida en armenia", "tintear"]
alojamientos = ["Hotel Karlaca", "Hotel Mocawa", "Hotel Armenia", "Hotel Marriot", "Hotel Mocawa resort"]
#Respuestas por municipio.
respuestas_por_municipio = [
    "Armenia es la capital del departamento del Quindío y se conoce como la Ciudad Milagro, Algunos de sus atractivos turísticos incluyen el Parque de la Vida y el Museo del Oro Quimbaya.",
    "Si visitas Armenia, asegúrate de probar el café quindiano y de dar un paseo por la Calle de la Amargura, una calle llena de bares y restaurantes.",
    "¿Sabías que Armenia es la ciudad más importante en Colombia en producción de café?",
    "Calarcá es un municipio ubicado en el Valle del río Quindío. Algunos de sus atractivos turísticos incluyen el Jardín Botánico del Quindío, el parque recuca y el monte Peñas blancas.",
    "Calarcá es conocido por ser el lugar donde se celebra el tradicional reinado nacional del Café, que se lleva a cabo cada año en junio.",
    "El Puente de Occidente, construido en Calarcá a principios del siglo XX, es una importante obra de ingeniería que conecta a este municipio con el vecino departamento de Risaralda.",
    "Montenegro es un municipio ubicado en el corazón del eje cafetero colombiano. Algunos de sus atractivos turísticos incluyen el Parque Nacional del Café y la Finca Hotel El Rosario.",
    "Montenegro es conocido por ser el lugar donde se encuentra el Parque Nacional del Café, un parque temático que celebra la cultura cafetera y que atrae a miles de turistas cada año.",
    "Si visitas Montenegro, no te pierdas la oportunidad de tomar un tour por una finca cafetera y aprender todo sobre el proceso de producción del café."
]

historial = []
#agrupar y agregar categorias

#Despues agregar restaurantes

# Función para procesar la entrada del usuario y dar una respuesta
def responder(mensaje):
    # Clasificar la pregunta del usuario en una categoría
    texto_procesado = vectorizer.transform([mensaje])
    categoria = clasificador.predict(texto_procesado)[0]
    print (categoria) #--> para saber que categoria tiene el texto agregado.
    
    respuesta = ""
    # Responder en función de la categoría
    if categoria == "saludos":
    
        respuesta = random.choice(saludos)
        historial.append((mensaje,respuesta ))
        print(historial)
        return respuesta
    
    elif categoria == "lugares turísticos":
        
        respuesta = "Algunos de los lugares turísticos más populares son: " + ", ".join(lugares_turisticos)
        historial.append((mensaje,respuesta ))
        
        return respuesta
  
    elif categoria == "actividades":
       
        respuesta = "Algunas actividades populares incluyen: " + ", ".join(actividades)
        historial.append((mensaje,respuesta ))
        return respuesta
  
    elif categoria == "alojamientos":
        
        respuesta="Algunos de los mejores hoteles en la zona son: " + ", ".join(alojamientos)
        historial.append((mensaje,respuesta ))
        return "Algunos de los mejores hoteles en la zona son: " + ", ".join(alojamientos)
  
    elif categoria == "respuestas_por_municipio":
    
        respuesta = random.choice(respuestas_por_municipio)
        historial.append((mensaje,respuesta ))
        return random.choice(respuestas_por_municipio)
    
    elif categoria=="Historial":

        print(historial)
        return null
    
    
    else:
        return "Lo siento, no entiendo lo que quieres decir. ¿Podrías reformular tu pregunta?"
    
# Datos de entrenamiento
datos = [
    ("saludos", "hola"),
    ("saludos", "buenas"),
    ("saludos", "Hola"),
    ("lugares turísticos", "¿Cuáles son los lugares turísticos más populares?"),
    ("lugares turísticos", "¿Qué sitios turísticos debería visitar?"),
    ("actividades", "¿Qué actividades hay para hacer en la zona?"),
    ("actividades", "¿Cuáles son las mejores cosas para hacer en la ciudad?"),
    ("actividades", "que puedo hacer?"),
    ("alojamientos", "¿Cuáles son los mejores hoteles para hospedarse?"),
    ("alojamientos", "¿Dónde puedo encontrar alojamiento en la ciudad?"),
    ("respuestas_por_municipio", "cuentame de los pueblos."),
    ("respuestas_por_municipio", "cuentame del Quindio."),
    ("respuestas_por_municipio", "hablame del quindio."),
    ("Historial","Historial")
]

# Entrenamiento del modelo de clasificación de texto
corpus = [texto for categoria, texto in datos]
categorias = [categoria for categoria, texto in datos]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
clasificador = MultinomialNB()
clasificador.fit(X, categorias)


# Loop principal del chatbot
while True:
    mensaje = input("Usuario: ")
    if mensaje.lower() == "adios":
        print("Chatbot: ¡Hasta luego! Espero haber sido de ayuda.")
        break
    elif mensaje in respuestas_por_municipio:
        respuesta = random.choice(respuestas_por_municipio[mensaje])
        print("Chatbot: " + respuesta)
    else:
        respuesta = responder(mensaje)
        print("chatBot: " + respuesta)


'''
# Función para procesar la entrada del usuario y dar una respuesta
def responder(mensaje):
    if "hola" or "buenas" in mensaje.lower():
        return random.choice(saludos)
    elif "lugares turísticos" in mensaje.lower():
        return "Algunos de los lugares turísticos más populares son: " + ", ".join(lugares_turisticos)
    elif "actividades" in mensaje.lower():
        return "Algunas actividades populares incluyen: " + ", ".join(actividades)
    elif "alojamientos" in mensaje.lower():
        return "Algunos de los mejores hoteles en la zona son: " + ", ".join(alojamientos)
    else:
        return "Lo siento, no entiendo lo que quieres decir. ¿Podrías reformular tu pregunta?"
'''