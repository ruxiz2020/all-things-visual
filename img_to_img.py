import gradio as gr
from src.img_clipping.img_clipping import imgClipping

def show_image(img):
    print(type(img))
    return img

def img_clipping(img_path):

    ic = imgClipping(img_path)
    ic.remove_background()
    return ic.output_img


app = gr.Interface(
    title="Upload image to remove background",
    fn=img_clipping,
    inputs=gr.Image(label="Input Image Component", type="filepath"),
    outputs=gr.Image(label="Output Image Component"),
)

app.launch()
