function pre_completion(){
    return gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").value
}

function post_completion(prompt){
    gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").value = prompt
    gradioApp().querySelector('#tabs').querySelectorAll('button')[0].click()
    gradioApp().querySelector("#tab_txt2img #txt2img_prompt textarea").dispatchEvent(new Event("input", { bubbles: true }))
}
