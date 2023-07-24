import requests

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = ADD_YOUR_API_KEY
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}
request_input=input("Ask Your Queries?\n")
request_data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "system", "content": request_input}]
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)
if(response.status_code == 200):
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("Something Went Wrong")