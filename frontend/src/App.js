import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [currentDate, setCurrentDate] = useState(0);
  useEffect(() => {
  fetch(' http://0.0.0.0:8000/about/dt/').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
      setCurrentDate(data.date)
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
      <p>The date is {currentDate} and the time is {currentTime}.</p> <br/>
          <img src="http://0.0.0.0:8000/media/programs/Screenshot_from_2023-08-09_14-21-05.png" alt="SH"></img>
      </header>
    </div>
  );
}

export default App;

