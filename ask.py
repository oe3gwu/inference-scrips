import argparse
import requests
import json

def main():
    parser = argparse.ArgumentParser(description="A simple API client for an inference service.")
    parser.add_argument("question", help="The question to ask")

    args = parser.parse_args()

    url = "http://inference.weninger.local:11434/api/generate"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral:7b",
        "prompt": args.question,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        print(actual_response)
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
