from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Store the latest sensor data and max speed in memory
data_store = {
    'location': None,
    'speed': None,
    'acceleration': None,
    'gyro': None
}
max_speed = 0.0

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    response = dict(data_store)
    response['max_speed'] = max_speed
    return jsonify(response)

@app.route('/api/data', methods=['POST'])
def receive_data():
    global max_speed
    try:
        payload = request.get_json(force=True)
        data_store.update(payload)
        speed = payload.get('speed')
        if speed is not None and isinstance(speed, (int, float)):
            if speed > max_speed:
                max_speed = speed
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
