
import {useState, useEffect} from "react";
import axios from "axios";

function FunctionalComponent() {

    const [data, setData] = useState([])
    const [value, setValue] = useState("")

    useEffect(() => {
        axios.get("http://localhost:7000/data")
        .then(result => {
           setData(result.data)
        })
        .catch(error => {
            this.setState({
                error : error
            })
        })
    }, [])

    return(
        <div className="tableForm">
                {console.log("Data : ", data)}
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
                            data.length ? data.map(item => {
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
                <input type="text" value={value} onChange={(e) => setValue(e.target.value)} />
            </div>
    )
}

export default FunctionalComponent;