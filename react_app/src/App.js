import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import React from 'react';

import Login from './components/Login/login';
import JavaScriptExpressions from './components/Javascript_Expressions/javascriptExpressions';
import CondtionalRendering from './components/Conditional_Rendering/conditionalRendering';
import MapIterations from './components/Looping/mapIteration';
import Counter from './components/State_and_Props/State/state';

class App extends React.Component{
  render(){
    return(
      <div >
        <Counter/>
        {/* <MapIterations /> */}
        {/* <CondtionalRendering /> */}
        {/* <JavaScriptExpressions /> */}
        {/* <Login /> */}

      {/* <header className="App-header">
        {React.createElement("h1",{}, "This is session on React")}
        <h1>This is Session on React</h1>
      </header> */}
    </div>
    )
  }
}

export default App;

