from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen bei Trollpicks!"

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "Backend läuft!"})

if __name__ == '__main__':
    app.run(debug=True)
