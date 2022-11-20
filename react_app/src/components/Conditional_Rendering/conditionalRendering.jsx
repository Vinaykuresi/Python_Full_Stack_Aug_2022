

import React from "react";

class CondtionalRendering extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {

        let content;

        let loggedIn = true;


        // ternary Operator !! Conditional Operator
        loggedIn ? content = <h1>Welcome</h1> : content = <h1>Please Login</h1>

        return (
            <div style={{ backgroundImage: `url(${process.env.PUBLIC_URL} '/building.jpg')`, height: "300px" }}>
                {content}
            </div>
        )

        // if(!loggedIn){
        //     return(
        //         <div style={{backgroundImage : `url(${process.env.PUBLIC_URL} '/building.jpg')`, height:"300px"}}>
        //             <h1>Welcome</h1>
        //         </div>
        //     )
        // }else{
        //     return(
        //         <div style={{backgroundImage : `url(${process.env.PUBLIC_URL} '/building.jpg')`, height:"300px"}}>
        //             <h1>Please Login</h1>
        //         </div>
        //     )
        // }

    }
}

export default CondtionalRendering;