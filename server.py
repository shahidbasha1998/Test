from flask import Flask, request
from flask_cors import CORS

from utils import *

app = Flask("Medical Sample collection process Streamline")
CORS(app)

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()

        age = data['age']
        time_taken_for_sample_collection = data['sampleCollectionTime']
        lab_location = data['labLocation']
        time_taken_to_reach_lab = data['travelTime']
        gender = data['gender']
        test_name = data['testName']
        sample_storage = data['sampleStorage']
        traffic_conditions = data['trafficConditions']

        res = get_predict(
            age,
            gender,
            test_name,
            sample_storage,
            traffic_conditions,
            time_taken_for_sample_collection,
            lab_location,
            time_taken_to_reach_lab
        )

        Prediction = "No"
        if (res == 1): Prediction = "Yes"

        return { "success": True, "prediction": Prediction }
    except:
        return { "success": False, "message": "Enter all values correctly" }

if __name__ == '__main__':
    load_saved_artifacts()
    
    # debug = False
    debug = True
    port = 5000

    app.run(debug=debug, port=port)