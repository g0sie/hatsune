import React, { useState, useEffect } from "react";
import axios from "axios";

import "./App.css";
import { ChangeEvent } from "rollup";

function App() {
  const [data, setData] = useState("");
  const [inputText, setInputText] = useState("");

  const fetchData = () => {
    // fetch("/api/endpoint", {
    //   method: "POST",
    //   mode: "cors",
    //   body: JSON.stringify({ checkboxId: 10 }),
    // });
    axios.get("http://localhost:8000/test").then((response) => {
      response.status === 200 && setData(response.data.data);
    });
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(e.target.value);
  };

  const sendText = () => {
    // fetch("http://localhost:8000/ping", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    //   body: JSON.stringify({ text: inputText }),
    // });
    axios.post("http://localhost:8000/ping", { text: inputText });
  };

  useEffect(fetchData, []);

  return (
    <div className="App">
      <div>
        <div>data: {data}</div>
        <button onClick={fetchData}>fetch</button>
      </div>

      <div>
        <input value={inputText} onChange={handleInputChange} />
        <button onClick={sendText}>send</button>
      </div>
    </div>
  );
}

export default App;
