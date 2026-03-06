import gradio as gr
from tensorflow import keras
import tensorflow as tf
from pathlib import Path

RUNS_DIR = Path("runs")


modelos = {}

for run_folder in RUNS_DIR.iterdir():

    if run_folder.is_dir():

        modelos_en_carpeta = list(run_folder.glob("*.keras"))

        if modelos_en_carpeta:

            modelo_path = modelos_en_carpeta[0]

            nombre_modelo = f"{run_folder.name} | {modelo_path.stem}"

            modelos[nombre_modelo] = keras.models.load_model(modelo_path)

print("Modelos encontrados:")
for m in modelos:
    print(m)



def clasificar_texto(texto, modelo_nombre):

    if texto.strip() == "":
        return {"Error": 1.0}

    modelo = modelos[modelo_nombre]

    pred = modelo.predict(tf.constant([texto]), verbose=0)[0][0]

    return {
        "Negativo": float(1 - pred),
        "Positivo": float(pred)
    }


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# Clasificador de Reviews de Steam")
    gr.Markdown(
        "Introduce una review y selecciona el modelo que quieres probar."
    )

    with gr.Row():

        with gr.Column():

            selector_modelo = gr.Dropdown(
                choices=list(modelos.keys()),
                value=list(modelos.keys())[0] if modelos else None,
                label="Modelo"
            )

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
        inputs=[entrada, selector_modelo],
        outputs=salida
    )

    gr.Markdown(
        "El modelo puede fallar con sarcasmo o jergas nuevas."
    )

if __name__ == "__main__":
    demo.launch()