
import {useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { Increment, Decrement } from "../../actions";

function Redux_Operations_Hooks(){

    const [value, setValue] = useState(0);

    const dispatch = useDispatch();
    const count = useSelector((state) => state.countReducer.count);

    return(
        <div style={{textAlign : "center", marginTop : "20%"}}>
            {console.log("In Redux operations")}
            <input value={value} onChange={(e) => {e.preventDefault(); setValue(e.target.value)} }/><br/>
            <button onClick={(e) => {e.preventDefault();dispatch(Increment(value))}}>Increament</button>
            <button onClick={(e) => {e.preventDefault();dispatch(Decrement(value))}}>Decreament</button>
            <h1>{count}</h1>
        </div>
    )
}

export default Redux_Operations_Hooks;

