import openai
import re
from flask import Flask, render_template, request

openai.api_key = "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"
app = Flask(__name__)


def generate_response(prompt):
    completions = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()


# Define a function to analyze user input and determine the most relevant response
def analyze_input(input_text):
    # Preprocess the input text
    input_text = input_text.lower()
    input_text = re.sub(r'[^\w\s]','',input_text)
    
    # Use a simple rule-based approach to determine the most relevant response
    if "hello" in input_text:
        return generate_response("Hello!")
    elif "how are you" in input_text:
        return generate_response("I'm doing well, thank you for asking. How can I assist you today?")
    elif "what can you do" in input_text:
        return generate_response("I can provide information, answer questions, and perform various tasks. How can I assist you today?")
    else:
        return generate_response("I'm sorry, I didn't understand. Could you please rephrase your question?")

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = analyze_input(userText)
    
    return str(generate_response(response))


if __name__ == "__main__":
    app.run()
