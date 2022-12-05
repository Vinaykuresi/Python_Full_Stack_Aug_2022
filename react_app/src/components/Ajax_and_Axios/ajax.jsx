import React from "react";

import axios from "axios";

const headerStyle = { backgroundColor: "black", color: "white" }

class AjaxDataHandling extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            data : []
        }
    }

    componentDidMount(){
        axios.get("http://localhost:7000/data")
        .then(result => {
            this.setState({
                data : result.data
            })
        })
        .catch(error => {
            this.setState({
                error : error
            })
        })
    }

    render() {

        return (
            <div className="tableForm">
                {console.log("Data : ", this.state.data)}
                <table className="table table-bordered">
                    <thead style={{ backgroundColor: "black", color: "white" }} className="thead-dark">
                        <tr>
                            <th scope="col">Item</th>
                            <th scope="col">EDesciption</th>
                            <th scope="col">Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            this.state.data.length ? this.state.data.map(item => {
                                return (
                                    <tr key={item.product_id}>
                                        <td><img width={300} height={100} src={item.img} /></td>
                                        <td>{item.description}</td>
                                        <td>{item.price}</td>
                                    </tr>
                                )
                            }) : <tr><td rowSpan={3}>Content Not Found</td></tr>
                        }
                    </tbody>
                </table>
            </div>
        )
    }
}

export default AjaxDataHandling;

