import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import ErrorHandler from "./components/LifeCycleMethods/ErrorHandling/errorHandler"

import "bootstrap/dist/css/bootstrap.min.css";

import Increment_Decrement from "./components/State_and_Props/State/state"
import Ajax from "./components/Ajax_and_Axios/ajax"

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <ErrorHandler>
    <React.StrictMode>
      <Router>
        <Routes>
          <Route path="/" element={<Increment_Decrement />} />
          <Route path="/amazon" element={<Ajax />} />
        </Routes>
      </Router>
    </React.StrictMode>
  </ErrorHandler>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
