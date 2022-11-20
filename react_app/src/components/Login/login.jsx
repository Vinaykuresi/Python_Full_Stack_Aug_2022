
import React from "react";

class Login extends React.Component {

    constructor(props){
        super(props)
    }

    handleSubmit(event) {
        window.alert("Submitted the Form Successfully")
    }
    render(){
        return(
            <div className="form-group">
                <label for="mail">Enter the Email Id</label>
                <input className="form-control" type="email" id="mail" placeholder="Enter the Mail Id"></input>
                <label for="password">Enter the Password</label>
                <input className="form-control" width="100px" type="password" id="password" placeholder="Enter the Password"></input>
                <button type="submit" className="btn btn-primary" onClick={this.handleSubmit}>Login</button>
            </div>
        )
    }
}

export default Login;