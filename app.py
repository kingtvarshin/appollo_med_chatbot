import gradio as gr
import random

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response)

if __name__ == "__main__":
    demo.launch()