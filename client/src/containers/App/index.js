import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

import { Home, NotFound } from "../";

class App extends Component {
  render() {
    return (
      <div className="app">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route component={NotFound} />
        </Switch>
      </div>
    );
  }
}

export default App;
