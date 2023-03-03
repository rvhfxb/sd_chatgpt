# sd_chatgpt
<img width="342" src="https://user-images.githubusercontent.com/116002789/222644753-d42c5f7a-28a7-4d0a-8a50-20177f282889.png">
Generateボタンの下に📝ボタンが追加されます。

このボタンを押すと現在入力されているプロンプトに続けてChatGPTがプロンプトを生成します。

## Config
configフォルダ(stable-diffusion-webui/extensions/sd_chatgpt/config)に以下の2ファイルを設置してください。

### config.json
ChatGPTのAPIを使用するためのキーです。 https://platform.openai.com/account/api-keys
```
{
    "openai_key":"sk-xxxxxxxxxx"
}
```

### content.txt
ChatGPTに送信するメッセージです。`$PROMPT`が画面上のプロンプトに置換されます。

以下のように記述します。自由に書いてください。
```
Examples of high quality prompt for anime style girl illustration for text-to-image models are

- 1girl, solo, ...
- ... 
- ... 

Give me an example starts with "$PROMPT".
```
