import os.path
import random
import imageio

from flask import Flask
from flask import send_from_directory, request, make_response, jsonify
app = Flask(__name__)
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


@app.route("/get-photo", methods=['GET'])
def get_photo():
    
    np_dir, filename = get_random_photo_dir() 
    response = send_from_directory(np_dir, filename)
    response.headers['key'] = filename
    return response

@app.route("/guess-photo", methods=['POST'])
def guess_photo():
    data = request.form
    
    if 'imageHash' in data and 'guess' in data:
        image_hash = data['imageHash']
        guess = data['guess']
    
        np_dirs = [x[0] for x in os.walk("./data/")]
        # loop through all NPs
        for np in np_dirs:
            img_dirs = [x[2] for x in os.walk(np)]
            # loop through all images in park
            for img in img_dirs[0]:
                if image_hash in img:
                    msg = {}

                    # check if guess is the same as np directory
                    if guess.lower() == np.lower().replace("_", " ").split("/")[-1]:
                        msg = jsonify({'is_guess_correct': 'true'})
                    else:
                        msg = jsonify({'is_guess_correct': 'false'})

                    response = make_response(msg, 200)

    else: 
        response = make_response(jsonify({'Error': 'Request missing `imageHash` or `guess`'}), 400)

    return response

