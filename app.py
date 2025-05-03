from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({'message': 'Tarea agregada'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
