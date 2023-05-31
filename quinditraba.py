import random
import nltk # py -m pip install nltk
import json
from sklearn.feature_extraction.text import CountVectorizer #py -m pip install -U scikit.learn.
from sklearn.naive_bayes import MultinomialNB
import json
import subprocess

# Respuestas del chatbot
saludos = ["Hola, gracias por visitarnos!", "Hola, bienvenidos al Quindio.", "¡Bienvenido!, en que te puedo ayudar.", "buenas, pa' donde vamos?", "¿Que se dice padrecitos, pa' onde vamos?"]


lugares_turisticos = ["naturales", "cafes", "tematicos", "centros comerciales"]
lugares_naturales = ["cocora", "la mano de acaime", "mirador de Filandia", "mirador de Circacia", "Panaca", "Preñas blancas",
                     "Boquia", "Bosque de palma de cera", "Parque de la vida en Armenia"]
lugares_cafe = ["Lucerna", "café Quindio", "caoncorde", "la Morelia", "san Alberto", "el Domo", "soñarte",
                "café De Carlos", "tertulia", "la ruana", "café sorrento", "pan y chocolate", "pan y miel",
                "casa Bernal", "la finca", "casa willys", "cafe el barco"]
lugares_tematicos = ["parque del cafe", "recuca", "parque de los arrieros", "parque de la guadua", "parque de la pisicultura",
                     "museo del oro Quimbaya", "las Bailarinas", "soleden", "cenexpo"]
lugares_centrosComerciales = ["protal del Quindio", "unicentro", "plaza flora", "san sur", "centro comercial Bolivar", "la calle de los abuelos",
                             "mall zona oro", "mall privilegio", "mall de los naranjos", "containers", "armenia plaza", "cielos abiertos"]



actividades = [" pueden ser extremas o culturales, cual te intereza mas?"]
actividades_extremas = ["parapente en Calarcá", "parapente en buena vista", "karts en plaza flora", "balsaje en el rio la vieja",
                        "cabalgata en salento", "canopy Caracolies", "yeep panoramico", "resortera gigante en Salento", "cuatrimotos en Boquia",
                        "escalada en peñas blancas", "cenexpo", "bunjie jumping", "paseo en globo aeroestatico", "pintball"]
actividades_culturales = ["coffe tour", "tour al nevado santa isabel", "senderismos en peñas blancas", "fiestas de Armenia", "reinado nacional del café", "la feria del libro",
                          "museo del disco", "la estación del ferrocarril", "tour arquitectonico por el Quindio", "teatro azul", "cementerio libre",
                          "museo fotografico del Quindio", "artesanias de Filandia", "avistamiento de avers", "siembra de palma cera", "tour de barranquismo"]


alojamientos = ["Hotel Karlaca", "Hotel Mocawa", "Hotel Armenia", "Hotel Marriot", "Hotel Mocawa resort", "las camelias",
                "Biohabitad", "glamping las cascadas", "glamping la cima", "la riviera", "soleden"]
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
    #print (categoria) #--> para saber que categoria tiene el texto agregado.

    respuesta = "" #Se inicializa una variable para agregar las respuestas.
    # Responder en función de la categoría
    if categoria == "saludos":

        respuesta = random.choice(saludos)
        historial.append((mensaje,respuesta ))
        return respuesta


    elif categoria == "lugares turísticos":
        historial.append((mensaje,respuesta ))
        return "El Quindio cuenta con varios tipos de lugares turisticos, dime de cual quieres saber." + ", ".join(lugares_turisticos)
    elif categoria =="lugares_naturales":
        historial.append((mensaje,respuesta ))
        return "Algunos lugares naturales son: " + ", ".join(lugares_naturales)
    elif categoria =="lugares_cafe":
        historial.append((mensaje,respuesta ))
        return "Algunos lugares de café son: " + ", ".join(lugares_cafe)
    elif categoria =="lugares_tematicos":
        historial.append((mensaje,respuesta ))
        return "Algunos lugares tematicos son: " + ", ".join(lugares_tematicos)
    elif categoria =="lugares_centrosComerciales":
        historial.append((mensaje,respuesta ))
        return "Algunos centros comerciales son: " + ", ".join(lugares_centrosComerciales)


    elif categoria == "actividades":
        respuesta = "Algunas actividades populares " + ", ".join(actividades)
        historial.append((mensaje,respuesta ))
        return respuesta
    elif categoria =="actividades_extremas":
        historial.append((mensaje,respuesta ))
        return "Algunas actividades extremas son: " + ", ".join(actividades_extremas)
    elif categoria =="actividades_culturales":
        historial.append((mensaje,respuesta ))
        return "Algunas actividades culturales son: " + ", ".join(actividades_culturales)



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
        return "aca tienes el historial de mensajes"

    else:
        return "Lo siento, no entiendo lo que quieres decir. ¿Podrías reformular tu pregunta?"

# Datos de entrenamiento
datos = [
    ("saludos", "hola"),
    ("saludos", "buenas"),
    ("saludos", "Hola"),


    ("alojamientos", "¿Cuáles son los mejores hoteles para hospedarse?"),
    ("alojamientos", "¿Dónde puedo encontrar alojamiento en la ciudad?"),

    ("respuestas_por_municipio", "cuentame de los pueblos."),
    ("respuestas_por_municipio", "cuentame del Quindio."),
    ("respuestas_por_municipio", "hablame del quindio."),

    ("lugares turísticos", "¿Cuáles son los lugares turisticos más populares?"),
    ("lugares turísticos", "¿Qué sitios turísticos debería visitar?"),
    ("lugares_naturales","quiero saber más de los lugares naturales."),
    ("lugares_naturales","Lugares naturales."),
    ("lugares_cafe","quiero saber más de los lugares de cafe."),
    ("lugares_cafe", "cafes"),
    ("lugares_tematicos", "quiero ir a los parques tematicos"),
    ("lugares_tematicos", "lugares tematicos"),
    ("lugares_centrosComerciales", "quiero saber mas de los centros comerciales"),
    ("lugares_centrosComerciales", "centro comerciales"),

    ("actividades", "¿Qué actividades hay para hacer en la zona?"),
    ("actividades", "actividades"),
    ("actividades", "¿Cuáles son las mejores cosas para hacer en la ciudad?"),
    ("actividades", "que puedo hacer?"),
    ("actividades_extremas", "actividades extremas"),
    ("actividades_extremas", "quiero saber de las actividades extremas"),
    ("actividades_culturales", "actividades culturales"),
    ("actividades_culturales", "quiero saber de las actividades culturales"),

    ("Historial","Historial"),
    ("Historial", "historial")
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


# Abrir un archivo con el modo de escritura
with open('datos.json', 'w') as archivo:

    # Usar la función json.dump() para escribir la lista en el archivo JSON
    json.dump(historial, archivo)

# Cerrar el archivo
archivo.close()