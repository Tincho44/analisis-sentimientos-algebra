Objetivo:

Diseñar un algoritmo que mida que tan positivo, neutral o negativo es una frase.

Tecnologías a usar:

Python

Algoritmo:

w = w representa si una palabra de la frase pertenece a las palabras claves
s = s representa la cantidad de palabras positivas, neutrales y negativas una frase posee.


A mencionar:

instalar re por que el input de la data no es el ideal

para mejor funcionamiento del algoritmo tenemos que hacer que cuente no solamente las palabras, sino tambien el conjunto de las mismas, el hacer tan separado
no hace que tengamos un mejor control del resultado de si es positiva o negativa, ejemplo esta frase:

    "Out football team is not at its best, but we are working hard to improve. We will get there",

o esta:

    "We live in a world full of hate and violence, but we can change that. We have the power to make a difference",

Segun el algoritmo esta frase es sumamente negativa:

    "The fishermen know that the sea is dangerous and the storm terrible, but they have never found these dangers sufficient reason for remaining ashore",

Pero enrealidad el mensjae no lo es, por lo que para que el algoritmo funcione de verdad de la mejor manera, deberiamos tener en cuenta el core del mensaje tambien.


sentences = [
    "The beautiful sunrise filled me with hope, but the darkness soon returned",
    "Her kindness is always appreciated, though her anger can be overwhelming",
    "This celebration is a joyful event, despite the sadness in the air",
    "The new policy is beneficial, yet its drawbacks are significant",
    "He was generous with his praise, but his criticism was harsh",
    "The exciting opportunity came with significant risks",
    "She is known for her honesty, although her rudeness is also notorious",
    "The peaceful morning was interrupted by the loud construction noise",
    "The innovative design is impressive, but the execution is flawed",
    "Their collaboration brought success, despite some underlying tension",
    "The generous donation was tainted by ulterior motives",
    "The serene atmosphere was ruined by an unexpected argument.",
    "The optimistic outlook was dampened by the reality of the situation",
    "The bright future is promising, though uncertainty remains",
    "The supportive community faced challenges, but persevered through adversity"
]

key_words = {
    "positive_words" : ["beautiful", "hope", "kindness", "joyful", "beneficial", "generous", "exciting", "honesty", "peaceful", "innovative", "success", "serene", "optimistic", "bright", "supportive"],
    "neutral_words" : ["policy", "morning", "design", "execution", "collaboration", "situation", "reality", "argument", "future", "community"],
    "negative_words" : ["darkness", "anger", "sadness", "drawbacks", "harsh", "risks", "rudeness", "noise", "flawed", "tension", "ulterior", "ruined", "dampened", "uncertainty", "adversity"]
}