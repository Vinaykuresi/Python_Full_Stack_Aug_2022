

import React from "react";
import "./mapIteration.css";

import Data from "../Json_Content/data.json"

const headerStyle = { backgroundColor: "black", color: "white" }

class MapIterations extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {

        let employees = [
            {
                empId: 1001, empName: "Vinay", designation: "SSE"
            },
            {
                empId: 1002, empName: "Sandhya", designation: "Tech Lead"
            },
            {
                empId: 1003, empName: "Nani", designation: "Manager"
            }
        ]


        return (
            <div className="tableForm">
                {console.log("Data : ", Data)}
                <table className="table table-bordered">
                {/* <thead style={headerStyle} className="thead-dark"> */}
                    <thead style={{ backgroundColor: "black", color: "white" }} className="thead-dark">
                        <tr>
                            <th scope="col">Item</th>
                            <th scope="col">EDesciption</th>
                            <th scope="col">Price</th>
                        </tr>
                        {/* <tr>
                            <th>Employee Id</th>
                            <th>Employee Name</th>
                            <th>Employee Designation</th>
                        </tr> */}
                    </thead>
                    <tbody>

                        {/* With Map Looping */}

                        {
                            Data.length ? Data.map(item => {
                                return (
                                    <tr key={item.product_id}>
                                        <td><img width={300} height={100} src={item.img} /></td>
                                        <td>{item.description}</td>
                                        <td>{item.price}</td>
                                    </tr>
                                )
                            }) : <td rowSpan={3}>Content Not Found</td>
                        }
                        {/* {
                            employees.length ? employees.map(employee => {
                                return (
                                    <tr key={employee.empId}>
                                        <td>{employee.empId}</td>
                                        <td>{employee.empName}</td>
                                        <td>{employee.designation}</td>
                                    </tr>
                                )
                            }) : <td rowSpan={3}>Content Not Found</td>
                        } */}

                        {/* without Loop */}
                        {/* <tr>
                            <td>{employees[0].empId}</td>
                            <td>{employees[0].empName}</td>
                            <td>{employees[0].designation}</td>
                        </tr> */}
                    </tbody>
                </table>
            </div>
        )
    }
}

export default MapIterations;

