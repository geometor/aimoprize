import requests

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/EleutherAI/llemma_7b"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)
