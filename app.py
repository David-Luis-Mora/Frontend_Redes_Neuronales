import gradio as gr
import numpy as np
import pickle
from tensorflow import keras


# Cargar modelo entrenado
model = keras.models.load_model("modelo/modelo_texto.h5")

# Cargar vectorizador
with open("modelo/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)




ETIQUETAS = ["Negativo", "Positivo"]



def clasificar_texto(texto):

    if texto.strip() == "":
        return {"Error": 1.0}

    texto_vectorizado = vectorizer([texto])

    prediccion = model.predict(texto_vectorizado)

    if prediccion.shape[1] == 1:
        prob = float(prediccion[0][0])

        resultado = {
            "Negativo": 1 - prob,
            "Positivo": prob
        }

    else:
        probs = prediccion[0]
        resultado = {
            ETIQUETAS[i]: float(probs[i])
            for i in range(len(ETIQUETAS))
        }

    return resultado



with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# Clasificador de Texto con Deep Learning")
    gr.Markdown(
        "Introduce un texto y el modelo lo clasificará automáticamente."
    )

    with gr.Row():
        with gr.Column():
            entrada = gr.Textbox(
                lines=5,
                placeholder="Escribe aquí tu texto...",
                label="Texto de entrada"
            )

            boton = gr.Button("Clasificar")

        with gr.Column():
            salida = gr.Label(label="Probabilidades por clase")

    boton.click(
        fn=clasificar_texto,
        inputs=entrada,
        outputs=salida
    )

    gr.Markdown(
        "⚠️ El modelo puede fallar con ironías, jergas o expresiones nuevas."
    )


if __name__ == "__main__":
    demo.launch()