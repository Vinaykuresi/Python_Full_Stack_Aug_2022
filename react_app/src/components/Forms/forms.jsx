
import React from "react";


class Form extends React.Component {
    constructor(props){
        super(props);
        this.state={
            data : ""
        }
    }

    handleClick = () => {
        window.alert(`Submitted the form of ${this.state.data}`)
    }

    updateData = (event) => {
        this.setState({
            data : event.target.value
        })
    }

    render(){
        return(
            <div>
                <input type="text" onChange={this.updateData}  value={this.state.data}/>
                <button type="submit" onClick={this.handleClick}>Submit</button>
            </div>
        )
    }
}

export default Form;