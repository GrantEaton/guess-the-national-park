import React from "react";
import Select from "react-select";
import { connect } from "react-redux";
import makeAnimated from "react-select/lib/animated";
import { bindActionCreators } from "redux";

import { selectPark } from "../../actions/actions";

var parks = [];

class Selector extends React.Component {
  handleChange = selectedParks => {
    this.props.selectPark(selectedParks);
  };
  render() {
    const { selectedParks, nationalParks } = this.props;
    if (nationalParks) {
      parks = nationalParks.map(park => {
        return { value: park, label: park };
      });
    }

    return (
      <Select
        ref="selector"
        isMulti
        name="national parks"
        options={
          selectedParks != null && selectedParks.length >= 5 ? [] : parks
        }
        closeMenuOnSelect={false}
        onChange={this.handleChange}
        searchPromptText="selectNationalParks"
        components={makeAnimated()}
        menuIsOpen={true}
        autoFocus={true}
        placeholder={<div>Select Up To 5 Parks...</div>}
        className="basic-multi-select"
        classNamePrefix="select"
      />
    );
  }
}

const mapStateToProps = state => {
  return {
    selectedParks: state.npGuesser.selectedParks,
    nationalParks: state.npGuesser.nationalParks
  };
};

const mapDispatchToProps = dispatch => ({
  selectPark: selectedParks => dispatch(selectPark(selectedParks))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Selector);
