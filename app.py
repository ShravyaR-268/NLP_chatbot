from flask import Flask, render_template, request, jsonify
from eliza_chatbot import eliza_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = eliza_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
