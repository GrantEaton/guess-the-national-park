import React, { Component } from "react";
import ReactDOM from "react-dom";
import "./styles.css";
import "react-responsive-carousel/lib/styles/carousel.min.css";

import { Carousel } from "react-responsive-carousel";

const NpCarousel = () => (
  <div className="image_box">
    <Carousel infiniteLoop={true} useKeyboardArrows={true} emulateTouch={true}>
      <div className="center">
        <img />
      </div>
      <div className="center">
        <img />
      </div>
      <div className="center">
        <img />
      </div>
    </Carousel>
  </div>
);

export default NpCarousel;

// ReactDOM.render(<DemoCarousel />, document.querySelector(".demo-carousel"));
