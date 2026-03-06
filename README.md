# 🎮 Clasificador de Reviews de Steam con Redes Neuronales

Aplicación web interactiva para **clasificar reviews de Steam como positivas o negativas** utilizando **redes neuronales entrenadas con TensorFlow/Keras**.

La aplicación cuenta con una **interfaz interactiva creada con Gradio**, que permite introducir una review y probar distintos modelos entrenados guardados en la carpeta `runs/`.

---

# 📌 Características

* Clasificación de **sentimiento (positivo / negativo)** de reviews de Steam
* Interfaz web interactiva con **Gradio**
* Carga automática de **modelos entrenados**
* Posibilidad de **probar distintos modelos**
* Visualización de **probabilidades de predicción**

---

# ⚙️ Tecnologías utilizadas

* Python
* TensorFlow
* Keras
* Gradio
* Pathlib

---

# 📂 Estructura del proyecto

```
Frontend_Redes_Neuronales
│
├── app.py
├── requirements.txt
├── README.md
│
└── runs/
    └── 20260306_002354/
        ├── accuracy.png
        ├── confusion_matrix.png
        ├── loss.png
        ├── config.json
        ├── metrics.json
        └── ModeloLSTMEmbedReducidoV1.keras
```

Cada carpeta dentro de `runs/` representa **una ejecución de entrenamiento** y contiene:

* 📈 Gráfica de accuracy
* 📉 Gráfica de loss
* 🔀 Matriz de confusión
* 📊 Métricas del modelo
* 🧠 Modelo entrenado en formato `.keras`

---

# 🚀 Instalación

Clonar el repositorio:

```
git clone https://github.com/David-Luis-Mora/Frontend_Redes_Neuronales.git
cd Frontend_Redes_Neuronales
```

Instalar dependencias:

```
pip install -r requirements.txt
```

---

# ▶️ Ejecutar la aplicación

```
python app.py
```

Gradio lanzará automáticamente una interfaz web en:

```
http://127.0.0.1:7860
```

---

# 🧠 Funcionamiento

Cuando se inicia la aplicación:

1. Se recorren todas las carpetas dentro de `runs/`
2. Se busca un archivo `.keras`
3. Se carga el modelo con TensorFlow/Keras
4. Los modelos disponibles aparecen en un selector

Fragmento de código principal:

```python
modelos[nombre_modelo] = keras.models.load_model(modelo_path)
```

---

# 🖥️ Interfaz de usuario

La interfaz permite:

* Seleccionar el modelo
* Introducir una review
* Clasificar el texto
* Visualizar la probabilidad de cada clase

Resultado mostrado:

```
Negativo: 0.23
Positivo: 0.77
```

---

# 📊 Ejemplo

Entrada:

```
This game is amazing, I can't stop playing it!
```

Salida:

```
Positivo: 0.92
Negativo: 0.08
```

---

# ⚠️ Limitaciones

El modelo puede fallar en algunos casos como:

* sarcasmo
* ironía
* jerga reciente
* textos demasiado cortos

---

