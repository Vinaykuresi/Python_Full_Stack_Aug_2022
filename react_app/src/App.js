import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import React from 'react';

import Login from './components/login';

class App extends React.Component{
  render(){
    return(
      <div className="App">
        <Login />
      {/* <header className="App-header">
        {React.createElement("h1",{}, "This is session on React")}
        <h1>This is Session on React</h1>
      </header> */}
    </div>
    )
  }
}

export default App;

  
// function App() {

//   const [timer, setTimer] = useState(0);
//   var time = 0

//   const timerFunction = () => {
//     time++
//     setTimer(time)
//     // setInterval(() => {
//     //   setTimer(() => timer++)
//     // }, 1000)
//   }

//   useEffect(() => {
//     const timer_refernce = setInterval(() => timerFunction(), 1000);
//     return () => clearInterval(timer_refernce)
//   },[])
//   return (
//     <div className="App">
//       <header className="App-header">
//         <span>The Timer Component : </span><span>{timer}</span>
//       </header>
//     </div>
//   );
// }

