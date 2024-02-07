from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "This is usecase 4"

@app.route('/how')
def hello():
    return 'Vanakkam da Mapla'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
