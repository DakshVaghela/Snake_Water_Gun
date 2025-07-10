from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.json["choice"]
    
    choice_map = {
        "snake": 1,
        "water": -1,
        "gun": 0
    }
    reverse_map = {
        1: "snake",
        -1: "water",
        0: "gun"
    }

    user_val = choice_map[user_choice.lower()]
    computer_val = random.choice([1, -1, 0])

    result = ""
    if computer_val == user_val:
        result = "DRAW"
    elif (computer_val - user_val) == -1 or (computer_val - user_val) == 2:
        result = "YOU LOSE"
    else:
        result = "YOU WIN"

    return jsonify({
        "computer": reverse_map[computer_val],
        "you": reverse_map[user_val],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
