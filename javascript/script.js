function pre_completion(content, prompt){
    return [content, gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").value]
}

function post_completion(prompt){
    gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").value = prompt
    gradioApp().querySelector('#tabs').querySelectorAll('button')[0].click()
    gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").dispatchEvent(new Event("input", { bubbles: true }))
}


onUiUpdate(() => {
    const toolsDiv = gradioApp().querySelector("#txt2img_tools");
    const chatgptButton = gradioApp().querySelector("#btn_sd_chatgpt_action");

    if (chatgptButton){
        return
    }
    
    const button = document.createElement("button");
    button.id = "btn_sd_chatgpt_action";
    button.type = "button";
    button.innerHTML = "📝";
    button.className = "gr-button gr-button-lg gr-button-tool";
    // button.style = `padding-left: 0.1em; padding-right: 0em; margin: 0.1em 0;max-height: 2em; max-width: 6em`;
    button.addEventListener("click", 
        () => gradioApp().querySelector("#btn_sd_chatgpt_completion").click()
    );

    toolsDiv.append(button);
})
