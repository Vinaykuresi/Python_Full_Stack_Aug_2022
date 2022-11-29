
import React from "react";

class CounterValue extends React.Component {

    constructor(props){
        super(props);
    }

    render(){
        return(
            <div>
                <p>{this.props.value}</p>
            </div>
        )
    }
}

export default CounterValue;