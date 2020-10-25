from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_beer_consumption', methods=['GET', 'POST'])
def predict_beer_consumption():
    avg_temp = int(request.form['average temperature (c)'])
    min_temp = int(request.form['min temperature (c)'])
    max_temp = int(request.form['max temperature (c)'])
    precip = int(request.form['precipitation (mm)'])
    weekend = int(request.form['weekend'])
    delta_temp = int(request.form['delta temperature (c)'])

    response = jsonify({
        'estimated_consumption': util.get_estimated_consumption(avg_temp, min_temp, max_temp, precip, weekend, delta_temp)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Beer consumption predictor has started...")
    util.load_saved_data()
    app.run()