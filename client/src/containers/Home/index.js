import React, { Component } from "react";
import { bindActionCreators } from "redux";
import { connect } from "react-redux";

import { NpCarousel } from "../../components";
import { NpGuesser } from "../";
import * as actions from "../../actions/actions";

class Home extends Component {
  componentWillMount() {
    this.props.actions.getNationalParks();
    this.props.actions.getPhoto("test");
    this.props.actions.getPhoto("test");
    this.imageHash = this.props.actions.getPhoto("test");
  }

  render() {
    const { imageHash, nationalParks, selectedParks, actions } = this.props;

    return (
      /*
      <div className="home mt-5">
        <div className="row">
          <div className="col-12">
            <h2 className="mb-3">Compare Products</h2>
          </div>
        </div>
        <ProductList products={products} compare={actions.compare}/>
        {compareProducts.length >= 2 &&
          <Compare products={compareProducts}/>
        }
      </div>
      */
      <div className="home mt-5">
        <NpCarousel />
        <NpGuesser
          sendGuesses={actions.sendGuesses}
          imageHash={imageHash}
          selectedParks={selectedParks}
        />
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    selectedParks: state.npGuesser.selectedParks,
    imageHash: state.npGuesser.imageHash,
    nationalParks: state.npGuesser.nationalParks
  };
};

export default connect(
  mapStateToProps,
  dispatch => ({
    actions: bindActionCreators(actions, dispatch)
  })
)(Home);
