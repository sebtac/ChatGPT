## SEBTAC: GPT Code Generation:

- this is based on https://gitlab.com/nanuchi/python-automation-chatgpt
- works perfectly with model: "text-davinci-003"
- "gpt-3.5-turbo" needs different request_data and API_ENDPOINT -- implemented only in .ipynb!!!
- "code-davinci-002" is supposed to be tailered toward code generation but seems to be depreciated now and API calls fail
 
## This is an accompanying project of YouTube video about Python automation with ChatGPT

#### set environment variable OPENAI_API_KEY before executing python-chatgpt script
    export OPENAI_API_KEY=your-key-here

#### execute the main python-chatgpt script to generate python code from Open AI
    python3 python-chatgpt.py "extract all html headers from a web page, translate to Spanish and save the result into an html file" "extract-translate.py"

    python3 python-chatgpt.py "print hello world" "hello-world.py"
