# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated data (replace with actual data sources/APIs in a real implementation)
water_usage = {
    'current': 150,
    'target': 120,
    'savings': 20
}

alerts = [
    {'type': 'Leak Detection', 'message': 'Potential leak detected in sector 3'},
    {'type': 'Water Quality', 'message': 'pH levels slightly above normal in zone 2'}
]

@app.route('/')
def index():
    return render_template('index.html', water_usage=water_usage, alerts=alerts)

@app.route('/api/water-usage')
def get_water_usage():
    return jsonify(water_usage)

@app.route('/api/alerts')
def get_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)