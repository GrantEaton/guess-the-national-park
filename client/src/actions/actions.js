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

export const getPhoto = state => dispatch =>
  fetch(`${process.env.REACT_APP_API_URL}/api/get-photo`).then(response => {
    response.arrayBuffer().then(buffer => {
      var base64Flag = "data:image/jpeg;base64,";
      var imageStr = arrayBufferToBase64(buffer);
      if (response.headers.has("imageHash")) {
        dispatch(saveImageHash(response.headers.get("imageHash")));
      } else {
        // error
      }
      document.querySelector("img").src = base64Flag + imageStr;
    });
  });

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
