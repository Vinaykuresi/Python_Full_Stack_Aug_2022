

import React from "react";

class Updates extends React.Component{

    constructor(props){
        super(props)
    }

    shouldComponentUpdate(newProps, newState){
        if(this.props.time < 5){
            console.log("ShouldComponentUpdate : ", newProps)
            return true
        }else{
            return false
        }
    }

    componentDidUpdate(newProps, prevState, snapShot){
        console.log("Previous value destroyed : ", prevState)
        console.log("Updated")
    }

    render(){
        return(
            <div>
                {console.log(this.props)}
                <h2>Timer : {this.props.time}</h2>
            </div>
        )
    }
}

export default Updates;