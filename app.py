import gradio as gr
from tensorflow import keras
import tensorflow as tf


model = keras.models.load_model(
    "modelo_cod500kOverfitV2.keras",
    compile=True
)


def clasificar_texto(texto):

    print(type(texto))
    if texto.strip() == "":
        return {"Error": 1.0}
    pred = model.predict(tf.constant([texto]))

    return {
        "Negativo": float(1 - pred),
        "Positivo": float(pred)
    }


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# Clasificador de Reviews de Steam")
    gr.Markdown(
        "Introduce una review y el modelo predecirá si es positiva o negativa."
    )

    with gr.Row():

        with gr.Column():

            entrada = gr.Textbox(
                lines=5,
                placeholder="Write a Steam review...",
                label="Texto"
            )

            boton = gr.Button("Clasificar")

        with gr.Column():

            salida = gr.Label()

    boton.click(
        fn=clasificar_texto,
        inputs=entrada,
        outputs=salida
    )

    gr.Markdown(
        "El modelo puede fallar con sarcasmo o jergas nuevas."
    )


if __name__ == "__main__":
    demo.launch()