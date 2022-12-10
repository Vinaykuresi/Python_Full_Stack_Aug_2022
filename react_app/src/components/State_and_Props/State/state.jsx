
import React from "react";
import CounterValue from "../Props/counter";

import {Link} from "react-router-dom";

class Counter extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            count : 1
        }
    }

    handleCount(typo){
        if(typo === "add"){
            this.setState({
                count : this.state.count + 1
            })
        }else{
            this.setState({
                count : this.state.count - 1
            })
        }
    }

    render(){
        return(
            <div className="container counter">
                {console.log("Count : ", this.state.count)}
                {/* <p>{this.state.count}</p> */}
                <CounterValue value={this.state.count} />
                <button type="button" class="btn btn-success" onClick={() => this.handleCount("add")}>Increase(+)</button><span>&nbsp;&nbsp;</span>
                <button type="button" class="btn btn-danger" onClick={() => this.handleCount("sub")}>Decrease(-)</button><br/>
                <Link to="/amazon">Amazon Website</Link><br/>
                <Link to="/redux">React Redux Concept</Link>
            </div>
        )
    }
}

export default Counter;