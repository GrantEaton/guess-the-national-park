import * as types from "../constants/types";

const INITIAL_STATE = {
  imageHash: null,
  selectedParks: []
};

export default function(state = INITIAL_STATE, action) {
  switch (action.type) {
    case types.FETCH_PRODUCTS:
      return {
        ...state,
        products: action.payload.map(product => ({
          ...product,
          compare: false
        }))
      };
    case types.COMPARE_PRODUCT:
      return {
        ...state,
        products: state.products.map(
          product =>
            product.id === action.product.id
              ? { ...product, compare: !product.compare }
              : product
        )
      };
    case types.SAVE_NP_GUESSES:
      return {
        ...state,
        selectedParks: action.selectedParks.map(park => {
          return park.value;
        })
      };
    case types.SAVE_NATIONAL_PARKS:
      return {
        ...state,
        nationalParks: action.nationalParks
      };
    case types.SAVE_DIFFICULTY:
      return {
        ...state,
        difficulty: action.difficulty
      };
    case types.SAVE_IMAGE_HASH:
      return {
        ...state,
        imageHash: action.imageHash
      };
    default:
      return state;
  }
}
