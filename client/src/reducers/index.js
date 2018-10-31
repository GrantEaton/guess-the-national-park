import { combineReducers } from "redux";
import npGuesser from "./npGuesserReducer";

const compareApp = combineReducers({
  npGuesser
});

export default compareApp;
