import requests

# Replace 'API_KEY' with actual API key
api_key = 'API_KEY'

# Define the API endpoint URL
api_url = "https://api.openai.com/v1/chat/completions"

# List of prompts you want responses for
prompts = [
    "Prompt 1: ",
    "Prompt 2: ",
    "Prompt 3: "
]

# Define the request headers with your API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Initialize an empty list to store responses
responses = []

# Loop through each prompt and make API requests
for prompt in prompts:
    data = {
        "model": "text-davinci-002",  # Choose the engine that suits your needs
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Make the POST request to the OpenAI API
    response = requests.post(api_url, json=data, headers=headers)

    # Extract and append the generated response
    if response.status_code == 200:
        response_data = response.json()
        generated_text = response_data["choices"][0]["message"]["content"]
        responses.append(generated_text.strip())
    else:
        responses.append(f"Error: {response.status_code} {response.text}")

# Print the responses
for i, response in enumerate(responses, 1):
    print(f"Response {i}: {response}")

