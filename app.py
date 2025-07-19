from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Aplikasi DevOps berhasil berjalan!"})

@app.route('/add', methods=['GET'])
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Input tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
