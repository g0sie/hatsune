import React, { useState, useEffect } from "react";
import axios from "axios";

import "./App.css";

function App() {
  const [data, setData] = useState("");

  const fetchData = () => {
    axios
      .get("http://localhost:8000/test/", {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        response.status === 200 && setData(response.data.data);
      });
  };

  useEffect(fetchData, []);

  return (
    <div className="App">
      <div>data: {data}</div>
      <button onClick={fetchData}>fetch</button>
    </div>
  );
}

export default App;
