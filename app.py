from flask import Flask, render_template, jsonify
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Store the latest sensor data in memory
data_store = {
    'location': None,
    'speed': None,
    'acceleration': None,
    'gyro': None
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        payload = request.get_json(force=True)
        data_store.update(payload)
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    self.client.loop_start()
        
    def get_data(self):
        return self.data

mqtt_subscriber = MQTTSubscriber()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return jsonify(mqtt_subscriber.get_data())

if __name__ == '__main__':
    mqtt_subscriber.start()
    app.run(debug=True, port=5000)
