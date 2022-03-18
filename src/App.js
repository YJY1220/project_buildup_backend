import logo from './logo.svg';
import './App.css';
import RestAPI from "./RestAPI.js";
import React from "react";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <RestAPI />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="http://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;