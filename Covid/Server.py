from flask import Flask, request, jsonify
import Covid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})

@app.route('/get_location',methods=['POST'])
def get_location() :
    hsp = request.form['hsp']
    response = jsonify({
        'Hospital': Covid.get_hospital(hsp)
    })
    return response

if __name__ == "__main__" :
    print('Real_Estate_Price_Prediction')
    Covid.load_saved_artifacts()
    app.run()