
import React from "react";

class JavaScriptExpressions extends React.Component {

    constructor(props){
        super(props)
    }

    render(){

        let count = 5;

        let person = {
            name : "Vinay",
            qualification : "MCA",
            job : "SSE"
        }

        let styles = {
            color : "red",
            fontStyle : "italic"
        }

        let values = {
            num1 : 25,
            num2 : 30
        }
        return(
            <div style={{backgroundImage : `url(${process.env.PUBLIC_URL} '/building.jpg')`, height:"300px"}}>
                <h3>{count} * {count} is  : {count * count}</h3>
                <h4 style={{color:"blue"}}>Person Details : </h4>
                <ul typeof="disc" style={styles}>
                    <li> Name  : {person.name}</li>
                    <li> Qualification  : {person.qualification}</li>
                    <li> Job  : {person.job}</li>
                </ul>

                <span> {values.num1} &lt; {values.num2}  : </span><span>{ values.num1  < values.num2  ? "True" : "False"}</span>
            </div>
        )
    }
}

export default JavaScriptExpressions;