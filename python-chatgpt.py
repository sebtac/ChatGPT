import requests
import argparse
import os, time

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save Python script")
args = parser.parse_args()

#api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

model = "text-davinci-003" # WORKS
#model = "gpt-3.5-turbo" # DOES NOT WORK?!?!?
#model = "code-davinci-002" # DOES NOT WORK ?!?!?!?

if model == "text-davinci-003":
    api_endpoint = "https://api.openai.com/v1/completions"
elif model == "gpt-3.5-turbo": # DOES NOT WORK FOR CODE GENERATION
    api_endpoint = "https://api.openai.com/v1/chat/completions"
elif model == "code-davinci-002":
    api_endpoint = "https://api.openai.com/v1/chat/completions"

request_data = {
    "model": model,
    "prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    "max_tokens": 500,
    "temperature": 0.5
}

#"messages": [],
#"prompt": f"Write python script to {args.prompt}. Provide only code, no text",
    
start_time = time.time()
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
    print("File Generated!", "It took", time.time() - start_time, "Seconds")
else:
    print(f"Request failed with status code: {str(response.status_code)}")
