
import Increment_Decrement from "../State_and_Props/State/state"
import Ajax from "../Ajax_and_Axios/ajax"
import React from "react"

import Redux_Operations_Hooks from "../operations/operation_hooks";

import {BrowserRouter as Router, Routes, Route} from "react-router-dom";

class App_Routes extends React.Component {
    render(){
        return(
            <Router>
                <Routes>
                    <Route path="/" component={<Increment_Decrement/>} />
                    <Route path="/amazon" component={<Ajax/>} />
                    <Route path="/*" component={<Redux_Operations_Hooks/>} />
                </Routes>
            </Router>
        )
    }
}

export default App_Routes;