import requests

# Define API endpoint
API_ENDPOINT = "http://localhost:8000/predict"

# Example text for prediction
text = "This movie was great!"

# Send POST request
response = requests.post(API_ENDPOINT, json={"text": text})

# Print response
print(response.json())
