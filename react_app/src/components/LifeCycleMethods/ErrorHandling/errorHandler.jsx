
import React from "react";

class ErrorHandler extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            error : false,
            errorInfo : null
        }
    }

    componentDidCatch(error, errorInfo){
        this.setState({
            error : error,
            errorInfo : errorInfo
        })
    }

    render(){
        if(this.state.error){
            console.log(this.state.error, this.state.errorInfo)
            return(
                <div>
                    <h5>{this.state.error.toString()}</h5>
                </div>
            )
        }
        return this.props.children;
    }
}

export default ErrorHandler;