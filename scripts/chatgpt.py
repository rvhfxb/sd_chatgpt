import openai
import modules.scripts as scripts
import gradio as gr
import modules.ui
import pathlib
import json
import os

txt_content = None
content = ""

def formatPrompt(str):
    if str[-1] == ".":
        str = str[:-1]
    if str.startswith("- "):
        return str[2:]
    if str[1:].startswith(". "):
        return str[3:]
    return str

def completion(text, start = "1girl"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"user",
            "content":text.replace("$PROMPT", start)
        }]
    )
    print("ChatGPT:")
    print(response)
    prompts = response["choices"][0]["message"]["content"].split("\n")
    prompts = [formatPrompt(x) for x in prompts if x != '']
    return text, prompts[0]

class Script(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return 'ChatGPT'

    def show(self, is_img2img):
        if not is_img2img:
            return scripts.AlwaysVisible

    def ui(self, is_img2img):
        p = pathlib.Path(__file__).parts[-4:-2]
        config_json = os.path.join(p[0], p[1], 'config', 'config.json')
        if os.path.exists(config_json):
            with open(config_json) as f:
                config = json.load(f)
                openai.api_key = config.get("openai_key")
        else:
            print("config.json not found")
        config_content = os.path.join(p[0], p[1], 'config', 'content.txt')
        if os.path.exists(config_content):
            with open(config_content) as f:
                content = f.read()
        else:
            print("content.txt not found")

        with gr.Group():
            with gr.Accordion('ChatGPT', open=True):
                txt_content = gr.Textbox(value=content, show_label=False)
                btn_completion = gr.Button(value="Completion",elem_id="btn_sd_chatgpt_completion")
                txt_prompt = gr.Textbox(visible=False)

        btn_completion.click(
            fn = completion,
            _js = "pre_completion",
            inputs = [txt_content, txt_prompt],
            outputs = [txt_content, txt_prompt],
        )
        txt_prompt.change(
            fn = None,
            _js = "post_completion",
            inputs = [txt_prompt]
        )
        return [txt_content,btn_completion,txt_prompt]