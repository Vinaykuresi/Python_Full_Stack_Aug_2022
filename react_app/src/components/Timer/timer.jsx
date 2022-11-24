

function App() {

  const [timer, setTimer] = useState(0);
  var time = 0

  const timerFunction = () => {
    time++
    setTimer(time)
    // setInterval(() => {
    //   setTimer(() => timer++)
    // }, 1000)
  }

  useEffect(() => {
    const timer_refernce = setInterval(() => timerFunction(), 1000);
    return () => clearInterval(timer_refernce)
  },[])
  return (
    <div className="App">
      <header className="App-header">
        <span>The Timer Component : </span><span>{timer}</span>
      </header>
    </div>
  );
}

export default App;