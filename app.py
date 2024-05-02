from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_OPENAI_API_KEY"
messages = [{"role": "system", "content": "You are the always sarcastic Deadpool."}]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return jsonify({"response": chatgpt_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
