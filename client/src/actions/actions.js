import * as types from "../constants/types";

export const getNationalParks = state => dispatch => {
  fetch(`${process.env.REACT_APP_API_URL}/api/get-national-parks`).then(
    response => {
      response.json().then(data => {
        dispatch(saveNationalParks(data.national_parks));
      });
    }
  );
};

export const getPhoto = req => dispatch =>
  fetch(`${process.env.REACT_APP_API_URL}/api/get-photo?req=${req}`).then(
    response => {
      response.arrayBuffer().then(buffer => {
        var base64Flag = "data:image/jpeg;base64,";
        var imageStr = arrayBufferToBase64(buffer);
        if (response.headers.has("imageHash")) {
          dispatch(saveImageHash(response.headers.get("imageHash")));
          dispatch(saveDifficulty("easy"));
        } else {
          // error
        }

        var selectedPhoto = false;
        const images = document.querySelectorAll("img");
        images.forEach((img, i) => {
          if (img.src === "" && !selectedPhoto) {
            img.src = base64Flag + imageStr;
            images[i + images.length / 2].src = base64Flag + imageStr;
            selectedPhoto = true;
          }
        });
      });
    }
  );

function arrayBufferToBase64(buffer) {
  var binary = "";
  var bytes = [].slice.call(new Uint8Array(buffer));

  bytes.forEach(b => (binary += String.fromCharCode(b)));
  return window.btoa(binary);
}

export const sendGuesses = (selectedParks, imageHash) => {
  fetch(`${process.env.REACT_APP_API_URL}/api/guess-photo`, {
    method: "post",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      guesses: selectedParks,
      imageHash: imageHash
    })
  }).then(response => {
    response.json().then(data => {
      console.log(data);
    });
  });
};

export const compare = product => ({
  type: types.COMPARE_PRODUCT,
  product
});

export const saveDifficulty = difficulty => ({
  type: types.SAVE_DIFFICULTY,
  difficulty
});

export const saveNationalParks = nationalParks => ({
  type: types.SAVE_NATIONAL_PARKS,
  nationalParks
});

export const saveImageHash = imageHash => ({
  type: types.SAVE_IMAGE_HASH,
  imageHash
});

export const selectPark = selectedParks => ({
  type: types.SAVE_NP_GUESSES,
  selectedParks
});
