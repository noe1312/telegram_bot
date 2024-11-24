import re

def process_message(message, response_array, response):
    # Dividir el mensaje y la puntuacion dentro del array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())
    
    # Puntua el conjunto de palabras en el mensaje
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1
            
    # Retorna las respuestas y el score de la respuesta 
    print(score, response) #Esto es solamente para debbuging
    return (score, response)

def get_response(message):
    # Agrega tu respuesta personalizada
    response_list = [
        process_message(message, ['hola', 'buenos dias', 'buenas noches','buenas', ], 'Hola! Como estas?'),
        process_message(message, ['como', 'cómo','como estas vos','Como estas', 'Como estas?', 'Bien y vos?','bien y vos'],'Yo estoy bien, muchas gracias! en que puedo ayudarte'),
        process_message(message, ['chau', 'adios', 'hasta luego','nos vemos'], 'Chau, que la pases bien!'),
        process_message(message, ['me', 'puedes', 'ayudar', 'help', 'me'], 'Si, en que puedo ayudarte? No dudes en decirnos tus dudas aqui (http://148.100.78.147/index.php/contacto/) siempre estamos dispuestos a mejorar!'),
        process_message(message, ['Quisiera', 'saber', 'sobre','los','relojes','que','tiene','en','venta','Que relojes tiene?','Que relojes tiene','que relojes tiene','que relojes tiene?' ],'Aqui tiene un catalogo con todos nuestros precios y ofertas de relojes, te dejamos un link que te llevara a nuestra pagina: [Ver pagina](http://148.100.78.147/index.php/inicio/)'),
        process_message(message, ['quienes son','de que trata','de','Quienes son','Quienes son?','quienes son?','De que trata?'],'Nosotros somos una relojeria y buscamos la perfeccion y la más alta calidad, para mas informacion sobre nosotros aqui te dejamos un link que te llevara a saber mas de nosotros. (http://148.100.78.147/index.php/nosotros/)'),
        
    ]
    
    # Rsvisa todas las respuestas score y retorna la mejor conexion posible
    response_score = []
    for response in response_list:
        response_score.append(response[0])
        
    # Obtener el mayor valor posible para la mejor respuesta y almacenarlo dentro de una variable
    winning_response = max(response_score)
    matching_response = response_list[response_score.index(winning_response)]
    
    # Retorna el matching response al usuario
    if winning_response == 0:
        bot_response = 'Perdon, no logro entender lo que escribiste'
    else:
        bot_response = matching_response[1]
        
    print('La respuesta del Bot:', bot_response)
    return bot_response