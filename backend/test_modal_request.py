import requests

# Replace this with your actual deployed Modal endpoint
BACKEND_URL = "https://kodyt--tinyllama-coding-tutor-flask-app.modal.run/api/ask"

# Example code + question payload
payload = {
    "code": """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)""",
    "question": "What does this function do?"
}

# Send the POST request
response = requests.post(BACKEND_URL, json=payload)

# Handle response
if response.ok:
    print("✅ Response from model:")
    print(response.json()["answer"])
else:
    print("❌ Error:", response.status_code)
    print(response.text)
