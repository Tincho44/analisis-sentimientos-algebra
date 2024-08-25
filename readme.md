# Análisis de Sentimientos con Algoritmo de Palabras Clave

## Objetivo
El objetivo de este proyecto es diseñar un algoritmo que evalúe qué tan positiva, neutral o negativa es una frase, basándose en la presencia de palabras clave predefinidas.

## Tecnologías utilizadas
- **Lenguaje**: Python 3

## Descripción del Algoritmo
El algoritmo analiza una lista de frases y determina la cantidad de palabras positivas, neutrales y negativas en cada una. Los resultados se presentan mediante los vectores `w` y `s`:

- **Vector `w`**: Es un vector binario que indica si una palabra clave está presente en la frase (`1`) o no (`0`).
- **Vector `s`**: Es un vector que cuenta cuántas palabras positivas, neutrales y negativas contiene la frase. El formato es `[positivas, neutrales, negativas]`.

### Decisiones Lógicas
1. **Procesamiento de texto**:
   - Se utiliza la función `re.sub` para limpiar las frases de signos de puntuación, permitiendo que las palabras clave se detecten correctamente.

2. **Vector `w`**:
   - `w` se inicializa como un vector de ceros con una longitud igual al número total de palabras clave (positivas, neutrales y negativas).
   - A medida que se recorren las palabras clave, si una de ellas está presente en la frase, la posición correspondiente en `w` se establece en `1`.

3. **Vector `s`**:
   - `s` se inicializa como un vector `[0, 0, 0]`, donde cada posición representa la cantidad de palabras positivas, neutrales y negativas, respectivamente.
   - Cada vez que una palabra clave se encuentra en la frase, se incrementa el valor en la posición correspondiente de `s`.

4. **Calidad Promedio y Sentimiento Promedio**:
   - **Calidad Promedio (`avg_w`)**: Es la proporción de palabras clave que aparecen en la frase respecto al total de palabras clave.
   - **Sentimiento Promedio**: Se calcula como la diferencia entre el número de palabras positivas y negativas en la frase.

5. **Índices de Palabras Positivas, Neutrales y Negativas**:
   - Se calculan como la proporción de palabras positivas, neutras y negativas respecto al total de palabras clave encontradas en la frase.

### Ejecución del Proyecto
Para correr el proyecto, sigue los siguientes pasos:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/analisis-sentimientos-algebra.git
   cd analisis-sentimientos-algebra

2. **Instalar Python**
    Descargar la ultima version (3) de python aca:
    https://www.python.org/downloads/

3. **Correr el script** 
   ```bash
    python3 script.py
