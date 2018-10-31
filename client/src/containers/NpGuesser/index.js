import React, { Component } from "react";
import { Button } from "reactstrap";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";

import "./styles.css";
import { Selector } from "../";
import { sendGuesses } from "../../actions/actions";

class NpGuesser extends Component {
  render() {
    const { imageHash, selectedParks, actions } = this.props;
    return (
      <div className="np_guesser_box">
        <div className="selector_and_button">
          <div className="selector">
            <Selector />
          </div>
          <div className="button">
            <Button
              color="primary"
              onClick={() => sendGuesses(selectedParks, imageHash)}
              disabled={selectedParks.length === 0}
            >
              Guess!
            </Button>{" "}
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    selectedParks: state.npGuesser.selectedParks,
    imageHash: state.npGuesser.imageHash
  };
};

export default connect(mapStateToProps)(NpGuesser);
