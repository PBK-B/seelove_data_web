import React, { useState, useEffect } from "react";
import { WordCloud } from "@ant-design/charts";

import "./App.css";
import originData from "./data/data.json";

function App() {
  const [data, setData] = useState([]);
  useEffect(() => {
    setData(originData);
  }, []);
  var config = {
    data: data,
    wordField: "name",
    weightField: "value",
    colorField: "name",
    wordStyle: {
      fontFamily: "Verdana",
      fontSize: [8, 52],
      rotation: 0,
    },
    random: function random() {
      return 0.5;
    },
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="header-title">看看爱情真实的模样。</h1>
        <p className="header-title header-sub-title">
          See what love looks like.
        </p>
      </header>
      <div>
        <WordCloud {...config} />
      </div>
    </div>
  );
}

export default App;
