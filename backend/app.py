from flask import Flask, jsonify #import libraries

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_articles():
    return jsonify({"Hello" : "World"})

if __name__ == "__main__":
    app.run(deubg = True)