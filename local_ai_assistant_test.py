import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_model(prompt, model="phi"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from model.")

    except request.exception.RequestException as e:
        return f"Error: {e}"

def main():
    print("\nLocal Privacy AI Assistant Test\n")

    user_input = "What is encryption?"
    answer = ask_model(user_input)
    print(f"Q: {user_input}\nA: {answer}")

if __name__ == "__main__":
    main()