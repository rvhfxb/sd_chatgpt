import openai
import modules.scripts as scripts
import gradio as gr
import modules.ui

openai.api_key = "{openai token}"
content = """
Examples of {explanation of prompt} are

- {example1}} 
- {example2} 
- {example3} 

"""
def formatPrompt(str):
    if str.startswith("- "):
        return str[2:]
    if str[1:].startswith(". "):
        return str[3:]
    return str

def completion(start = "1girl"):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":"user",
            "content":content+f"Give me a example starts with '{start}''."
        }]
    )
    print(response)
    prompts = response["choices"][0]["message"]["content"].split("\n")
    prompts = [formatPrompt(x) for x in prompts if x != '']
    return prompts[0]


class Script(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return 'ChatGPT'

    def show(self, is_img2img):
        if not is_img2img:
            return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion('ChatGPT', open=True):
                btn_completion = gr.Button(value="Completion")
                txt_prompt = gr.Textbox(visible=False)
                

        btn_completion.click(
            fn = completion,
            _js = "pre_completion",
            inputs = [txt_prompt],
            outputs = [txt_prompt],
        )
        txt_prompt.change(
            fn = lambda x:None,
            _js = "post_completion",
            inputs = [txt_prompt]
        )
        return [btn_completion]
    
    def process(self):
        pass