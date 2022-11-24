
import React from "react";

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
                <p>{this.state.count}</p>
                <button type="button" class="btn btn-success" onClick={() => this.handleCount("add")}>Increase(+)</button><span>&nbsp;&nbsp;</span>
                <button type="button" class="btn btn-danger" onClick={() => this.handleCount("sub")}>Decrease(-)</button>
            </div>
        )
    }
}

export default Counter;