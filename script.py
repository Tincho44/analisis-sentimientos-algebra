import re

sentences = [
    "The beautiful day was filled with love and hope, making everyone feel happy and great as they enjoyed the fun and joyful moments together",
    "After a bad day filled with endless struggles, I felt completely tired and drained, knowing that I would lose everything I had worked so hard for",
    "Despite the beautiful weather and the great sense of hope, the bad news left everyone feeling tired and worried that they might lose the happiness they had just found",
    "During the short break, they discussed the slight difference in their approaches to the project",
    "Despite the great efforts and the beautiful setting, the constant noise and harsh criticism created a significant break in the team's spirit",
    
    "the dinner was great, and I love your taste in music",
    "I cant believe how bad my day was, but im still happy its over, now I just want to have some fun",
    "He is very dangerous, he's a bad influence",
    "This show is great, I love the actors and I always have a ton of fun watching it",
    "this place is beautiful, but I hate how tired I am, I think im gonna stop walking before I start feeling bad",
    
    "The community we created is so beautiful and full of hope. We need to keep it that way, otherwise we will lose everything",
    "Our football team is not at its best, but we are working hard to improve. We will get there",
    "We live in a world full of hate and violence, but we can change that. We have the power to make a difference",
    "The fishermen know that the sea is dangerous and the storm terrible, but they have never found these dangers sufficient reason for remaining ashore",
    "Nobody cares how much you know, until they know how much you care"
]

key_words = {
    "positive_words": ["love", "great", "happy", "fun", "beautiful", "hope", "improve"],
    "neutral_words": ["break", "difference", "stop", "music"],
    "negative_words": ["bad", "tired", "lose", "hate", "violence", "dangerous", "storm", "terrible"]
}

vectores_w = []
vectores_s = []
calidad_promedio = []
promedio_sentimiento = []

for phrase in sentences: 

    print("Frase:", phrase)

    phrase_cleaned = re.sub(r'[^\w\s]', '', phrase.lower()) 

    w = [0] * len(key_words["positive_words"] + key_words["neutral_words"] + key_words["negative_words"])
    
    s = [0, 0, 0]  # inicializo s con 0 para positivo, neutro y negativo

    words = phrase_cleaned.split()  # convierto la frase en minúsculas y la divido en palabras

    for i, word in enumerate(key_words["positive_words"] + key_words["neutral_words"] + key_words["negative_words"]):
        if word in words:
            w[i] = 1
            if word in key_words["positive_words"]:  # sumo 1 a la lista s en la posición de positivo
                s[0] += 1
            elif word in key_words["neutral_words"]:  # sumo 1 a la lista s en la posición de neutro
                s[1] += 1
            elif word in key_words["negative_words"]:  # sumo 1 a la lista s en la posición de negativo
                s[2] += 1

    print("W por frase:", w)
    print("S por frase:", s)                      

    avg_w = sum(w) / len(w)  # calculo la calidad promedio
    sentimiento_promedio = (1 * s[0]) + (0 * s[1]) + (-1 * s[2])

    vectores_w.append(w)
    vectores_s.append(s)
    calidad_promedio.append(avg_w)
    promedio_sentimiento.append(sentimiento_promedio)

    sTotal = sum(s)  # sumo todos los valores que están en S

    if sTotal > 0:  # verifico que tenga palabras clave
        # Calculo el porcentaje de palabras positivas, neutrales y negativas
        positivas = (s[0] / sTotal) 
        neutrales = (s[1] / sTotal)
        negativas = (s[2] / sTotal)
    else:
        # Si sTotal es 0, significa que no hay palabras clave en la frase
        positivas = 0
        neutrales = 0
        negativas = 0

    # Estadísticas por palabra recorrida de todas las frases
    print("Sentimiento Promedio por frase:", sentimiento_promedio)
    print("Calidad promedio por frase:", avg_w)
    print("Índice de Palabras positivas:", positivas)
    print("Índice de Palabras neutrales:", neutrales)
    print("Índice de Palabras negativas:", negativas)
    print(" ")

# Resultados finales
print("Frase más positiva:", sentences[promedio_sentimiento.index(max(promedio_sentimiento))])
print(" ")
print("Frase más negativa:", sentences[promedio_sentimiento.index(min(promedio_sentimiento))])
print(" ")
print("Frase con mayor calidad promedio:", sentences[calidad_promedio.index(max(calidad_promedio))])
print(" ")
print("Frase con menor calidad promedio:", sentences[calidad_promedio.index(min(calidad_promedio))])
print(" ")
print("Frase con mayor promedio de sentimiento:", sentences[promedio_sentimiento.index(max(promedio_sentimiento))])
print(" ")
print("Frase con menor promedio de sentimiento:", sentences[promedio_sentimiento.index(min(promedio_sentimiento))])
