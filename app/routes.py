import os.path
import random
import imageio
import json

from flask import Flask
from flask import send_from_directory, request, make_response, jsonify
from flask_cors import CORS

from data.nationalParks import get_parks

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, expose_headers='imageHash')
app._static_folder = "./data"

def get_random_photo_dir():
    np_dirs = [x[0] for x in os.walk("./data/")]
    np_dir = random.choice(np_dirs[1:])
    file_count = len([x[2] for x in os.walk(np_dir)])
    while (file_count < 3):
        np_dir = random.choice(np_dirs)
        file_count = len([x[2] for x in os.walk(np_dir)][0])
        photo_dirs = [x[2] for x in os.walk(np_dir)]
    filename = random.choice(photo_dirs[0])

    return np_dir, filename


@app.route("/api/get-photo", methods=['GET'])
def get_photo():
    
    np_dir, filename = get_random_photo_dir() 
    response = send_from_directory(np_dir, filename)
    response.headers['imageHash'] = filename
    return response

@app.route("/api/get-national-parks", methods=['GET'])
def get_national_parks():
    response = make_response(jsonify({"national_parks": get_parks()}), 200)
    response.mimetype = "application/javascript"
    return response



@app.route("/api/guess-photo", methods=['POST'])
def guess_photo():
    data = request.json
    msg = None 

    if 'imageHash' in data and 'guesses' in data:
        image_hash = data['imageHash']
        guesses = data['guesses']


        np_dirs = [x[0] for x in os.walk("./data/")]
        # loop through all NPs
        for np in np_dirs:
            img_dirs = [x[2] for x in os.walk(np)]
            # loop through all images in park
            for img in img_dirs[0]:
                if image_hash in img:
                    correct_park = np.lower().replace("_", " ").split("/")[-1]
                    for guess in guesses:
                        # check if guess is the same as np directory
                        if guess.lower() == correct_park:
                            msg = jsonify({'is_guess_correct': 'true', 'correct_park': correct_park})
                        else:
                            msg = jsonify({'is_guess_correct': 'false', 'correct_park': correct_park})
            
    if msg is None:
        response = make_response(jsonify({'Error': 'Request error due to field `imageHash` or `guess`'}), 400)
    else:
        response = make_response(msg, 200)
    response.mimetype = "application/javascript"
    return response

